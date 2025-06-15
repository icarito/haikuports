#!/usr/bin/env python3
"""
resolve_dependencies.py - HaikuPorts Build Dependency Resolver

Purpose:
  This script resolves and lists all unique build-time dependencies
  (BUILD_REQUIRES and BUILD_PREREQUIRES) for one or more HaikuPorter packages.
  It traverses the dependency tree recursively to find all prerequisites.

Usage:
  python3 resolve_dependencies.py <package_name1> [package_name2 ...]

  Example:
    python3 resolve_dependencies.py expat zlib
    python3 resolve_dependencies.py cmd:make sdl2

Arguments:
  package_name: One or more HaikuPorter package names.
                You can provide the base name (e.g., "gcc", "sdl2") or a
                prefixed name (e.g., "cmd:gcc") as found in recipes. The script
                normalizes these for recipe lookup and correctly filters them
                from the final output.

Output:
  The script prints a list of unique prerequisite packages required to build
  the initial set of packages. The list will exclude the packages that were
  initially specified by the user (considering both base and prefixed forms).
  Dependencies are listed with their prefixes (e.g., "cmd:make", "lib:zlib",
  "devel:libfoo") as they appear in recipe files, after cleaning and
  normalization of version/arch specifics.

Assumptions:
  - The script is run from the root directory of a standard HaikuPorts checkout.
  - Recipe files (`.recipe`) are located in '<category>/<package_name_dir>/'
    directories (e.g., 'dev-libs/openssl/openssl-1.1.1t.recipe').
    The <package_name_dir> is what `normalize_package_name_for_find` resolves to.
  - Category directories are identifiable by containing a hyphen in their name
    (e.g., "dev-libs", "app-text").

Key Steps:
  1. Dynamic Category Discovery: Finds category directories within the HaikuPorts root.
  2. Recipe File Location: Locates recipe files based on normalized package names.
  3. Recipe Parsing: Extracts dependencies from BUILD_REQUIRES and BUILD_PREREQUIRES
     sections, handling multi-line definitions and comments.
  4. Name Cleaning & Prefix Retention: Cleans dependency names by stripping versions,
     architecture suffixes, and Haiku-specific variables, while *retaining*
     functional prefixes (cmd:, lib:, devel:).
  5. Recursive Resolution: Traverses the dependency graph to find all direct and
     indirect dependencies, avoiding cycles.
  6. Output Generation: Lists the final set of unique dependencies, excluding initial inputs.
"""

import argparse
import os
import re
import sys

# Constants for HaikuPorts directory structure (adjust if necessary)
HAIKUPORTS_ROOT = "." # Assuming the script is run from the root of haikuports clone
# RECIPE_CATEGORIES list is removed, will be detected dynamically.

def find_recipe_file(package_name):
    """
    Finds the recipe file for a given (normalized) package directory name.

    It dynamically scans `HAIKUPORTS_ROOT` for category-like directories
    (directories assumed to contain a hyphen, e.g., "dev-libs", "app-arch").
    Then, it searches for a sub-directory matching `package_name` within each category.
    Inside this package directory, it looks for any file ending with ".recipe".

    Args:
        package_name (str): The normalized name of the package directory
                            (e.g., "openssl", "python"). This name is typically
                            the output of `normalize_package_name_for_find`.

    Returns:
        str: The full path to the first found recipe file (sorted alphabetically if multiple exist),
             or None if no recipe file is found.
    """
    # print(f"find_recipe_file: Attempting to find recipe for package directory: {package_name}") # Verbose

    dynamically_found_categories = []
    try:
        for entry in os.listdir(HAIKUPORTS_ROOT):
            if os.path.isdir(os.path.join(HAIKUPORTS_ROOT, entry)) and '-' in entry:
                dynamically_found_categories.append(entry)
    except OSError as e:
        print(f"Error listing root directory {HAIKUPORTS_ROOT} to find categories: {e}", file=sys.stderr)
        return None

    if not dynamically_found_categories:
        print(f"No category-like directories (containing '-') found in {HAIKUPORTS_ROOT}.", file=sys.stderr)
        return None

    for category in dynamically_found_categories:
        package_dir_path = os.path.join(HAIKUPORTS_ROOT, category, package_name)
        if os.path.isdir(package_dir_path):
            try:
                # Attempt to find a recipe file. HaikuPorts convention is often <packageName>-<version>.recipe.
                # Some packages might have multiple .recipe files (e.g. different versions or variants).

                recipe_files_in_dir = [f for f in os.listdir(package_dir_path) if f.endswith(".recipe")]

                if not recipe_files_in_dir:
                    continue # No recipe files in this directory, try next category.

                # Prioritize a recipe that starts with the package_name (if package_name is specific, e.g., "expat").
                # This helps in cases like "expat" directory having "expat-2.5.0.recipe".
                for r_file in recipe_files_in_dir:
                    if r_file.startswith(package_name):
                        found_path = os.path.join(package_dir_path, r_file)
                        # print(f"find_recipe_file: Found specific recipe (startswith match): {found_path}") # Verbose
                        return found_path

                # Fallback: return the first .recipe file found in the directory (alphabetically sorted).
                # This is the most common path for normalized package_names (e.g., package_name="python"
                # would find "python3.10-3.10.18.recipe" or similar).
                found_path = os.path.join(package_dir_path, sorted(recipe_files_in_dir)[0])
                # print(f"find_recipe_file: Found generic recipe (first .recipe match): {found_path}") # Verbose
                return found_path
            except OSError as e:
                print(f"Error: Could not read package directory {package_dir_path}: {e}", file=sys.stderr)
                continue # Try next category

    # print(f"find_recipe_file: Recipe for package directory '{package_name}' not found in any category.", file=sys.stderr) # Verbose
    return None


def parse_recipe(recipe_path):
    """
    Parses a HaikuPorts .recipe file to extract build dependencies.

    It looks for BUILD_REQUIRES and BUILD_PREREQUIRES sections, handling
    multi-line variable definitions (lines ending with '\\').
    Dependency strings are cleaned by:
    - Retaining prefixes like "cmd:", "lib:", "devel:".
    - Removing version specifications (e.g., ">=1.0", "==1.2.3").
    - Removing Haiku-specific variables like "$secondaryArchSuffix".
    - Removing common architecture and build suffixes (e.g., "_x86", "_host").

    Args:
        recipe_path (str): The full path to the .recipe file.

    Returns:
        set: A set of unique, cleaned dependency names (strings),
             with prefixes retained. Returns an empty set on error.
    """
    # print(f"parse_recipe: Parsing recipe {recipe_path}...") # Verbose
    dependencies = set()
    current_block_content = ""
    in_block = False
    block_type = None # "BUILD_REQUIRES" or "BUILD_PREREQUIRES"

    try:
        with open(recipe_path, 'r') as f:
            for line_number, line_text in enumerate(f, 1):
                stripped_line = line_text.strip()

                if stripped_line.startswith("#") or not stripped_line: # Skip comments and empty lines
                    if not in_block: # if we are not in a block, comments are fine
                        continue
                    # If inside a block, comments might terminate the block or be part of a multi-line value
                    # For simplicity, we'll assume comments on their own line inside a block are not part of the value list
                    # and that inline comments will be handled during per-dependency cleaning.

                if in_block:
                    # Continuing a block
                    # Remove inline comments first from the line being appended
                    line_text_no_inline_comment = line_text.split('#', 1)[0].rstrip()

                    if line_text_no_inline_comment.endswith('\\'):
                        current_block_content += line_text_no_inline_comment[:-1].strip() + " " # Add with space, remove backslash
                    else:
                        # End of block
                        current_block_content += line_text_no_inline_comment.strip()
                        in_block = False
                else:
                    # Check for new block start
                    if stripped_line.startswith("BUILD_REQUIRES=") or \
                       stripped_line.startswith("BUILD_PREREQUIRES="):
                        in_block = True
                        block_type = stripped_line.split('=',1)[0]
                        content_after_equals = stripped_line.split('=', 1)[1].strip()

                        # Remove inline comments from the first line of the block
                        content_after_equals = content_after_equals.split('#', 1)[0].rstrip()

                        current_block_content = "" # Reset for new block. Crucial for VAR=" then newline cases.

                        if content_after_equals == '"':
                            # This is the case: VAR=" (content starts on the next line)
                            # current_block_content remains empty, in_block is True.
                            # Subsequent lines in the 'elif in_block:' clause will append.
                            pass
                        elif content_after_equals.startswith('"') and content_after_equals.endswith('\\"'):
                            # This is VAR="value \\" (escaped quote, continued) - unlikely for HaikuPorts but robust
                            current_block_content = content_after_equals[1:-2].strip() + " " # remove quote and backslash-quote
                        elif content_after_equals.startswith('"') and content_after_equals.endswith('"'):
                            # This is VAR="value" (single line quoted)
                            current_block_content = content_after_equals[1:-1].strip()
                            in_block = False # Process this single line block immediately
                        elif content_after_equals.startswith('"'):
                            # This is VAR="value (possibly continued without \ but relying on quote)
                            # Or VAR="value \ (shell continuation)
                            current_block_content = content_after_equals[1:] # Remove leading quote
                            if current_block_content.endswith('\\'):
                                current_block_content = current_block_content[:-1].strip() + " "
                            else:
                                # No line continuation via '\', but quote is open. Add space for next line.
                                current_block_content += " "
                            # in_block remains True
                        elif content_after_equals.endswith('\\'):
                            # This is VAR=value \ (unquoted, multi-line via shell backslash)
                            current_block_content = content_after_equals[:-1].strip() + " "
                        else:
                            # This is VAR=value (unquoted, single line) or potentially start of unquoted multi-line block
                            # if the recipe format is unusual. For HaikuPorts, BUILD_REQUIRES are typically quoted.
                            current_block_content = content_after_equals
                            in_block = False # Process this single line block immediately

                if not in_block and current_block_content.strip(): # Ensure there's content to process
                    # Process the collected block content
                    processed_content = current_block_content.strip()

                    # Remove surrounding quotes from the *entire collected block* if they haven't been handled yet
                    # This primarily handles the case where the block was VAR="\n val1\n val2\n" (content started on new line)
                    if processed_content.startswith('"') and processed_content.endswith('"'):
                        processed_content = processed_content[1:-1].strip()
                    elif processed_content.startswith("'") and processed_content.endswith("'"): # Also handle single quotes
                        processed_content = processed_content[1:-1].strip()

                    raw_deps = processed_content.split() # Split by whitespace

                    for dep_item in raw_deps:
                        dep_item = dep_item.strip()
                        if not dep_item or dep_item.startswith('#'): # Skip empty or comments
                            continue

                            continue

                        # Retain prefixes (cmd:, lib:, devel:) but process the rest
                        prefix = ""
                        name_part = dep_item
                        if name_part.startswith(("cmd:", "lib:", "devel:", "hpkg:", "data:", "source:")):
                            parts = name_part.split(":", 1)
                            prefix = parts[0] + ":"
                            name_part = parts[1] if len(parts) > 1 else ""

                        # Remove version specifications and anything after (e.g., comments, options)
                        version_specifiers = ['==', '>=', '<=', '>', '<', '~=', '!=']
                        for spec in version_specifiers:
                            if spec in name_part:
                                name_part = name_part.split(spec)[0]
                        name_part = name_part.split(' ')[0] # Handle cases like 'pkg # comment' or 'pkg ; option'

                        # Remove $secondaryArchSuffix explicitly and other variables
                        name_part = name_part.replace("$secondaryArchSuffix", "")
                        name_part = name_part.replace("${secondaryArchSuffix}", "")
                        name_part = name_part.replace("$arch", "")
                        name_part = name_part.replace("${arch}", "")
                        name_part = name_part.replace("$effectiveTargetArchitecture", "")
                        name_part = name_part.replace("${effectiveTargetArchitecture}", "")

                        # Remove common arch/build suffixes
                        suffixes_to_strip = [
                            "_x86_gcc2", "_x86", "_host", "_build", "_source_kit",
                            "_cross", "_bootstrap", "_tools", "_devel",
                        ]
                        for suffix in suffixes_to_strip:
                            if name_part.endswith(suffix):
                                name_part = name_part[:-len(suffix)]

                        # Reconstruct the cleaned name with its original prefix
                        cleaned_dep_with_prefix = prefix + name_part

                        # Filter out 'haiku' itself (with or without prefix), empty names, or other placeholders
                        if name_part and name_part != "haiku" and not name_part.startswith('$') \
                           and name_part not in ["none", "any", "set", "yes", "no", "true", "false"]:
                            dependencies.add(cleaned_dep_with_prefix)

                    current_block_content = "" # Reset for the next block
                    block_type = None

            # After loop, if still in_block (e.g. file ends with unclosed quote or backslash), process remaining content
            if in_block and current_block_content.strip():
                # print(f"parse_recipe: Processing remaining block content for {block_type}: '{current_block_content}'", file=sys.stderr) # Verbose
                processed_content = current_block_content.strip()
                if processed_content.startswith('"') and processed_content.endswith('"'): # Should already be handled if block ended correctly
                    processed_content = processed_content[1:-1].strip()
                elif processed_content.startswith("'") and processed_content.endswith("'"):
                    processed_content = processed_content[1:-1].strip()
                # If only a leading quote was present (e.g. VAR=" val \n val"), rstrip the final quote if it's there
                if current_block_content.startswith('"') and processed_content.endswith('"'): # Check original start vs current end
                     processed_content = processed_content[:-1].strip()


                raw_deps = processed_content.split()
                for dep_item_raw in raw_deps:
                    dep_item_val = dep_item_raw.strip()
                    if not dep_item_val or dep_item_val.startswith('#'): continue

                    prefix = ""
                    name_part = dep_item_val
                    if name_part.startswith(("cmd:", "lib:", "devel:", "hpkg:", "data:", "source:")):
                        parts = name_part.split(":", 1)
                        prefix = parts[0] + ":"
                        name_part = parts[1] if len(parts) > 1 else ""

                    version_specifiers = ['==', '>=', '<=', '>', '<', '~=', '!=']
                    for spec in version_specifiers:
                        if spec in name_part: name_part = name_part.split(spec)[0]
                    name_part = name_part.split(' ')[0]
                    name_part = name_part.replace("$secondaryArchSuffix", "").replace("${secondaryArchSuffix}", "")
                    name_part = name_part.replace("$arch", "").replace("${arch}", "")
                    name_part = name_part.replace("$effectiveTargetArchitecture", "").replace("${effectiveTargetArchitecture}", "")
                    suffixes_to_strip = ["_x86_gcc2", "_x86", "_host", "_build", "_source_kit", "_cross", "_bootstrap", "_tools", "_devel"]
                    for suffix in suffixes_to_strip:
                        if name_part.endswith(suffix): name_part = name_part[:-len(suffix)]

                    cleaned_dep_with_prefix = prefix + name_part
                    if name_part and name_part != "haiku" and not name_part.startswith('$') and \
                       name_part not in ["none", "any", "set", "yes", "no", "true", "false"]:
                        dependencies.add(cleaned_dep_with_prefix)

    except FileNotFoundError:
        print(f"Error: Recipe file '{recipe_path}' not found.", file=sys.stderr)
        return set() # Return empty set on error
    except Exception as e:
        print(f"Error parsing recipe {recipe_path} (line {line_number}): {e}", file=sys.stderr)
        return set() # Return empty set on error

    return dependencies

# Helper function to normalize package names for directory lookup
def normalize_package_name_for_find(dep_name):
    """
    Normalizes a package name to a suitable directory name for recipe lookup.

    This involves:
    1. Stripping common prefixes (cmd:, lib:, devel:, etc.) used in dependency lists,
       as these are not part of directory names.
    2. Applying specific rules for known package name patterns that map to
       different directory names (e.g., "python3.9" maps to "python" directory,
       "openssl1.1" maps to "openssl" directory).

    Args:
        dep_name (str): The dependency name, possibly with prefixes or version specifics
                        (e.g., "cmd:python3.9", "openssl1.1", "lib:foo").

    Returns:
        str: A normalized name intended to match a HaikuPorts directory name
             (e.g., "python", "openssl", "foo").
             Returns an empty string if the input is empty.
    """
    if not dep_name:
        return ""

    # Step 1: Strip common recipe prefixes (cmd:, lib:, devel:, etc.)
    # These are used in BUILD_REQUIRES but not for directory naming.
    base_name = re.sub(r"^(cmd:|lib:|devel:|hpkg:|data:|source:)", "", dep_name)

    # Step 2: Apply specific normalization rules for known package families
    # These rules convert common versioned names or specific forms to a base directory name.
    if base_name.startswith("python3") or base_name.startswith("python2"):
        return "python"
    if base_name.startswith("openssl3") or base_name.startswith("openssl1"): # e.g., openssl1.1, openssl3.0
        return "openssl"
    if base_name.startswith("zlib1"): # e.g. zlib1 -> zlib
        return "zlib"
    # For ICU, names like "icu69", "icu72" map to the "icu" directory.
    if base_name.startswith("icu") and base_name[3:].isdigit() and not base_name == "icu":
        return "icu"
    # For Boost, names like "boost1.83" map to "boost" directory
    if base_name.startswith("boost") and base_name[5:].isdigit():
        return "boost"
    # For OpenJDK, names like "openjdk8", "openjdk11" map to "openjdk" directory
    if base_name.startswith("openjdk") and base_name[7:].isdigit():
        return "openjdk"
    # For GLib, names like "glib2.78" (if not already cleaned by parse_recipe) map to "glib"
    if base_name.startswith("glib2"):
        return "glib"
    # Add more specific rules here if other common patterns are observed.

    # Default: return the (prefix-stripped) base_name.
    # This assumes that after prefix stripping, the name is often the directory name.
    # `parse_recipe` is responsible for removing versions like "-1.2.3" from the name part,
    # so `base_name` here should be relatively clean of typical version suffixes.
    return base_name


def resolve_dependencies_recursive(package_name_from_caller, all_found_dependencies, processed_lookup_tracker):
    """
    Recursively finds all dependencies for a given package.

    Args:
        package_name_from_caller (str): The name of the package as found in a
                                        recipe or from initial user arguments.
                                        May include prefixes (e.g., "cmd:make").
        all_found_dependencies (set): A set to accumulate all unique cleaned
                                      dependency names (with prefixes retained,
                                      e.g., "cmd:make", "lib:zlib").
        processed_lookup_tracker (set): A set to track normalized directory names
                                        (lookup_name, e.g., "make", "zlib") that
                                        have already been processed, to prevent
                                        redundant work and cycles.
    """

    # Normalize the package name for directory lookup and for tracking if this *recipe directory* has been processed.
    lookup_name = normalize_package_name_for_find(package_name_from_caller)

    # Base cases for recursion:
    if not lookup_name or lookup_name == "haiku": # Skip invalid names or "haiku" itself (often a meta-package).
        return
    if lookup_name in processed_lookup_tracker: # Already processed this recipe's directory.
        # print(f"resolve_dependencies_recursive: Already processed '{lookup_name}', skipping.") # Verbose
        return

    processed_lookup_tracker.add(lookup_name) # Mark as processed for this lookup_name.
    # print(f"resolve_dependencies_recursive: Processing '{package_name_from_caller}' (lookup as '{lookup_name}')") # Verbose

    recipe_path = find_recipe_file(lookup_name)

    if recipe_path:
        direct_deps = parse_recipe(recipe_path) # Returns cleaned names with prefixes.

        if not direct_deps and package_name_from_caller == lookup_name :
            # Only print if it wasn't some alias that resolved to an empty recipe,
            # and the user explicitly asked for this package.
            print(f"Info: No dependencies parsed or error during parsing for '{lookup_name}' from '{recipe_path}'.", file=sys.stderr)

        for dep_name_with_prefix in direct_deps:
            # `dep_name_with_prefix` is already cleaned and prefixed by `parse_recipe`.

            # Avoid self-dependency cycles if `dep_name_with_prefix` (after normalization for lookup)
            # is the same as the current `lookup_name`. This prevents trivial loops.
            if normalize_package_name_for_find(dep_name_with_prefix) == lookup_name:
                continue

            # Add the dependency (with prefix) to the global set of all found dependencies.
            # This ensures uniqueness across the entire resolution process.
            # Using a set handles uniqueness automatically.
            all_found_dependencies.add(dep_name_with_prefix)
            # if dep_name_with_prefix not in all_found_dependencies: # Verbose check
            #    print(f"resolve_dependencies_recursive: Adding dependency for '{lookup_name}': '{dep_name_with_prefix}'") # Verbose

            # Recursively resolve dependencies for this newly found dependency.
            # The `dep_name_with_prefix` is passed as is; it will be normalized
            # at the beginning of the next recursive call.
            resolve_dependencies_recursive(dep_name_with_prefix, all_found_dependencies, processed_lookup_tracker)
    else:
        # Error message if a recipe file cannot be found for a `lookup_name`.
        # This is important for identifying missing packages or normalization issues.
        print(f"Warning: No recipe file found for lookup name '{lookup_name}' (derived from '{package_name_from_caller}'). Cannot resolve its dependencies.", file=sys.stderr)


def main():
    """
    Main function to parse arguments and drive the dependency resolution process.
    It initializes the sets for tracking dependencies and processed packages,
    then calls the recursive resolver for each user-supplied package name.
    Finally, it filters the results and prints the list of prerequisites.
    """
    parser = argparse.ArgumentParser(
        description="Resolve build dependencies for HaikuPorts packages.",
        formatter_class=argparse.RawDescriptionHelpFormatter # Preserves formatting of help text from module docstring
    )
    parser.add_argument("package_names", nargs='+',
                        help="One or more package names to resolve dependencies for (e.g., 'openssl', 'cmd:make').")

    args = parser.parse_args()

    initial_packages_as_specified = set(args.package_names)
    all_found_dependencies = set() # Stores cleaned dependency names with prefixes, from parse_recipe.
    processed_lookup_tracker = set() # Stores normalized lookup_names to avoid reprocessing recipe files.

    print(f"Attempting to resolve dependencies for initial package(s): {', '.join(sorted(list(initial_packages_as_specified)))}")

    for pkg_spec_name in initial_packages_as_specified:
        # Start the recursive resolution for each initially specified package.
        resolve_dependencies_recursive(pkg_spec_name, all_found_dependencies, processed_lookup_tracker)

    # Filtering logic:
    # `all_found_dependencies` contains all unique dependencies found, with prefixes.
    # `initial_packages_as_specified` contains what the user typed.
    # We need to exclude a dependency if its base name (without prefix) or its full prefixed name
    # was in the initial set provided by the user.
    final_dependencies_to_install = set()
    for dep_with_prefix in all_found_dependencies:
        # Get the base name by stripping any known prefix
        base_name_of_dep = re.sub(r"^(cmd:|lib:|devel:)", "", dep_with_prefix)

        # A dependency should be excluded if:
        # 1. Its base name matches one of the initially specified packages.
        #    (e.g., user typed "gcc", and a resolved dependency is "cmd:gcc")
        # 2. Its full prefixed name matches one of the initially specified packages.
        #    (e.g., user typed "cmd:gcc", and a resolved dependency is "cmd:gcc")
        if not (base_name_of_dep in initial_packages_as_specified or \
                dep_with_prefix in initial_packages_as_specified):
            final_dependencies_to_install.add(dep_with_prefix)

    if final_dependencies_to_install:
        print("\nFinal list of prerequisite packages (excluding initially specified packages; prefixes retained):")
        for dep in sorted(list(final_dependencies_to_install)):
            print(dep)
    else:
        # This block provides more context if the resulting list is empty.
        if not all_found_dependencies and initial_packages_as_specified:
             # This means no dependencies were found *at all* for the given initial packages.
             print(f"\nNo dependencies found for the specified package(s): {', '.join(sorted(list(initial_packages_as_specified)))}. "
                   "They might be meta-packages, have no listed build requirements, their recipes were not found, or there was a parsing error.")
        elif not all_found_dependencies: # No initial packages specified and no dependencies found (e.g. error or empty run)
             print(f"\nNo packages or dependencies processed or found.")
        else: # Dependencies were found, but all of them were part of the initial set.
             print("\nNo additional prerequisite packages found beyond those specified (or the specified packages are themselves the only dependencies, considering prefixes).")

if __name__ == "__main__":
    main()
