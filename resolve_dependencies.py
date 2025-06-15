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
  - Category directories are identifiable by containing a hyphen in their name
    (e.g., "dev-libs", "app-text").

Key Steps:
  1. Index Building: Creates an in-memory index of all `PROVIDES` items from all recipes.
  2. Initial Package Resolution: Maps user-provided package names to recipe files using the index.
  3. Recipe Parsing: Extracts `PROVIDES`, `BUILD_REQUIRES`, and `BUILD_PREREQUIRES`
     sections from recipe files.
  4. Name Cleaning & Prefix Retention: Cleans item names by stripping versions,
     architecture suffixes, and Haiku-specific variables, while *retaining*
     functional prefixes (cmd:, lib:, devel:, package:, etc.).
  5. Recursive Resolution: Traverses the dependency graph using the `provides_index`
     to find all direct and indirect dependencies, avoiding cycles by tracking processed recipe paths.
  6. Output Generation: Lists the final set of unique dependencies, excluding initial inputs.
"""

import argparse
import os
import re
import sys

# Constants for HaikuPorts directory structure (adjust if necessary)
HAIKUPORTS_ROOT = "." # Assuming the script is run from the root of haikuports clone

# Note: find_recipe_file and normalize_package_name_for_find have been removed.
# Recipe lookups are now primarily done via the provides_index.
# build_provides_index uses its own file scanning logic.

def parse_recipe(recipe_path):
    """
    Parses a HaikuPorts .recipe file to extract PROVIDES, BUILD_REQUIRES,
    and BUILD_PREREQUIRES sections.

    It handles multi-line variable definitions (lines ending with '\\' or quoted
    multi-line strings). Item strings are cleaned by:
    - Retaining prefixes like "cmd:", "lib:", "devel:".
    - Removing version specifications (e.g., ">=1.0", "==1.2.3").
    - Removing Haiku-specific variables like "$secondaryArchSuffix".
    - Removing common architecture and build suffixes (e.g., "_x86", "_host").

    Args:
        recipe_path (str): The full path to the .recipe file.

    Returns:
        dict: A dictionary with keys 'provides', 'build_requires',
              'build_prerequires', each mapping to a set of unique,
              cleaned item names (strings) with prefixes retained.
              Returns a dictionary with empty sets on error.
    """
    provides_set = set()
    build_requires_set = set()
    build_prerequires_set = set()

    block_to_set_map = {
        "PROVIDES": provides_set,
        "BUILD_REQUIRES": build_requires_set,
        "BUILD_PREREQUIRES": build_prerequires_set,
    }

    active_block_var_name = None
    current_block_content = ""
    in_block_definition = False
    line_number = 0

    try:
        with open(recipe_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_number, line_text in enumerate(f, 1):
                stripped_line = line_text.strip()

                if not stripped_line or (stripped_line.startswith("#") and not in_block_definition) :
                    continue

                if not in_block_definition:
                    for block_name in block_to_set_map.keys():
                        if stripped_line.startswith(block_name + "="):
                            active_block_var_name = block_name
                            value_part = stripped_line.split("=", 1)[1].lstrip()
                            value_part_no_comment = value_part.split('#', 1)[0].rstrip()

                            if value_part_no_comment.startswith('"'):
                                current_block_content = value_part_no_comment[1:]
                                if current_block_content.endswith('"') and not current_block_content.endswith('\\"'):
                                    current_block_content = current_block_content[:-1]
                                    in_block_definition = False
                                else:
                                    in_block_definition = True
                                    if current_block_content.endswith('\\'):
                                         current_block_content = current_block_content[:-1].strip() + " "
                                    else:
                                         current_block_content += " "
                            elif value_part_no_comment.endswith('\\'):
                                current_block_content = value_part_no_comment[:-1].strip() + " "
                                in_block_definition = True
                            else:
                                current_block_content = value_part_no_comment
                                in_block_definition = False
                            break
                else:
                    line_to_add = stripped_line.split('#', 1)[0].rstrip()
                    if (line_to_add.endswith('"') and not line_to_add.endswith('\\"')) or \
                       (line_to_add == '"' and current_block_content.strip()):
                        current_block_content += line_to_add[:-1].strip() if line_to_add != '"' else ""
                        in_block_definition = False
                    elif line_to_add.endswith('\\'):
                        current_block_content += line_to_add[:-1].strip() + " "
                    else:
                        current_block_content += line_to_add + " "

                if not in_block_definition and current_block_content.strip():
                    target_set = block_to_set_map.get(active_block_var_name)
                    if target_set is not None:
                        final_content = current_block_content.strip()
                        if final_content.startswith('"') and final_content.endswith('"') and len(final_content) > 1:
                            final_content = final_content[1:-1]
                        elif final_content.startswith("'") and final_content.endswith("'") and len(final_content) > 1:
                            final_content = final_content[1:-1]

                        raw_items = final_content.split()
                        for raw_item in raw_items:
                            cleaned_item = _clean_recipe_item(raw_item)
                            if cleaned_item:
                                target_set.add(cleaned_item)

                    active_block_var_name = None
                    current_block_content = ""

            if in_block_definition and current_block_content.strip() and active_block_var_name:
                target_set = block_to_set_map.get(active_block_var_name)
                if target_set is not None:
                    final_content = current_block_content.strip()
                    if final_content.startswith('"') and final_content.endswith('"') and len(final_content) > 1: final_content = final_content[1:-1]
                    elif final_content.startswith("'") and final_content.endswith("'") and len(final_content) > 1: final_content = final_content[1:-1]
                    raw_items = final_content.split()
                    for raw_item in raw_items:
                        cleaned_item = _clean_recipe_item(raw_item)
                        if cleaned_item: target_set.add(cleaned_item)

    except FileNotFoundError:
        print(f"Error: Recipe file '{recipe_path}' not found.", file=sys.stderr)
    except Exception as e:
        print(f"Error parsing recipe {recipe_path} (around line {line_number}): {e}", file=sys.stderr)

    return {
        'provides': provides_set,
        'build_requires': build_requires_set,
        'build_prerequires': build_prerequires_set
    }

def resolve_dependencies_recursive(dependency_name, all_deps_set, processed_recipe_paths_set, provides_index):
    """
    Recursively finds all dependencies for a given dependency name using the provides_index.

    Args:
        dependency_name (str): The cleaned, prefixed name of the dependency to resolve
                               (e.g., "lib:openssl", "cmd:make"). This name should be
                               as found in recipe files (after cleaning by _clean_recipe_item)
                               or an initial package name provided by the user.
        all_deps_set (set): A set to accumulate all unique dependency names found
                            (will contain prefixed, cleaned names).
        processed_recipe_paths_set (set): A set to store the file paths of recipes
                                          that have already been parsed, to prevent
                                          redundant work and cycles.
        provides_index (dict): The pre-built dictionary mapping provided items
                               to their recipe file paths.
    """
    # print(f"resolve_dependencies_recursive: Attempting to resolve '{dependency_name}'") # Verbose

    recipe_path = get_recipe_path_for_dependency(dependency_name, provides_index)

    if recipe_path is None:
        # print(f"resolve_dependencies_recursive: No recipe path found in index for '{dependency_name}'. Leaf node or external.", file=sys.stderr) # Verbose
        return

    if recipe_path in processed_recipe_paths_set:
        # print(f"resolve_dependencies_recursive: Recipe '{recipe_path}' already processed. Skipping for '{dependency_name}'.") # Verbose
        return

    processed_recipe_paths_set.add(recipe_path)
    # print(f"resolve_dependencies_recursive: Processing recipe '{recipe_path}' for '{dependency_name}'.") # Verbose

    parsed_info = parse_recipe(recipe_path)

    direct_dependencies = parsed_info['build_requires'].union(parsed_info['build_prerequires'])

    if not direct_dependencies:
        # print(f"resolve_dependencies_recursive: No further build dependencies found in '{recipe_path}' for '{dependency_name}'.") # Verbose
        pass

    for new_dep_name in direct_dependencies:
        all_deps_set.add(new_dep_name)
        resolve_dependencies_recursive(new_dep_name, all_deps_set, processed_recipe_paths_set, provides_index)

def _clean_recipe_item(raw_item_str):
    """
    Cleans a raw string from a PROVIDES, BUILD_REQUIRES, or BUILD_PREREQUIRES block.
    - Strips surrounding quotes.
    - Retains functional prefixes (cmd:, lib:, devel:, etc.).
    - Removes version specifications and variables ($secondaryArchSuffix, etc.).
    - Removes common architecture suffixes.
    """
    item_str = raw_item_str.strip().strip('"').strip("'")
    if not item_str or item_str.startswith('#'):
        return None

    prefix = ""
    prefix_match = re.match(r"^(cmd:|lib:|devel:|hpkg:|data:|source:|generic:|package:)", item_str)
    if prefix_match:
        prefix = prefix_match.group(1)
        item_str = item_str[len(prefix):].strip()

    item_str = item_str.split(' ')[0]
    item_str = item_str.split('==')[0]
    item_str = item_str.split('>=')[0]
    item_str = item_str.split('<=')[0]
    item_str = item_str.split('=')[0]
    item_str = item_str.split('%')[0]

    vars_to_remove = [
        "$secondaryArchSuffix", "${secondaryArchSuffix}",
        "$arch", "${arch}",
        "$effectiveTargetArchitecture", "${effectiveTargetArchitecture}",
        "$portVersion", "${portVersion}",
        "$majorVersion", "${majorVersion}",
        "$minorVersion", "${minorVersion}",
        "$patchVersion", "${patchVersion}",
    ]
    for var in vars_to_remove:
        item_str = item_str.replace(var, "")

    arch_suffixes_regex = r"_((x86_gcc2)|(x86_64)|x86|gcc2|any|source)$"
    item_str = re.sub(arch_suffixes_regex, "", item_str)
    item_str = re.sub(r"_primaryArch$", "", item_str)
    item_str = item_str.strip('_')

    if not item_str:
        return None

    return prefix + item_str

def build_provides_index(haikuports_root):
    """
    Builds an index mapping cleaned provided item names to their recipe file paths.

    Scans all .recipe files in the specified haikuports_root, parses their
    PROVIDES sections, cleans the item names (retaining prefixes, removing
    versions/variables/arch-suffixes), and stores the mapping.

    Args:
        haikuports_root (str): The root path of the HaikuPorts checkout.

    Returns:
        dict: A dictionary where keys are cleaned provided item names (str)
              and values are the absolute paths to the recipe files (str)
              that provide them.
    """
    provides_index = {}
    print(f"Building PROVIDES index from: {haikuports_root}...")

    category_dirs = []
    try:
        for entry in os.listdir(haikuports_root):
            if os.path.isdir(os.path.join(haikuports_root, entry)) and '-' in entry:
                category_dirs.append(entry)
    except OSError as e:
        print(f"Error: Could not list category directories in '{haikuports_root}': {e}", file=sys.stderr)
        return provides_index

    for category in category_dirs:
        category_path = os.path.join(haikuports_root, category)
        try:
            for package_dir_name in os.listdir(category_path):
                package_dir_path = os.path.join(category_path, package_dir_name)
                if os.path.isdir(package_dir_path):
                    try:
                        recipe_files = [f for f in os.listdir(package_dir_path) if f.endswith(".recipe")]
                        for recipe_filename in recipe_files:
                            current_recipe_path = os.path.join(package_dir_path, recipe_filename)
                            try:
                                with open(current_recipe_path, 'r', encoding='utf-8', errors='ignore') as rf:
                                    # Use parse_recipe to get the 'provides' part
                                    parsed_content = parse_recipe(current_recipe_path) # Call the refactored parse_recipe
                                    recipe_provides = parsed_content.get('provides', set())

                                    for cleaned_item in recipe_provides:
                                        if cleaned_item in provides_index and provides_index[cleaned_item] != current_recipe_path:
                                            print(f"WARNING: Duplicate provide for '{cleaned_item}': new '{current_recipe_path}' (from package '{package_dir_name}') potentially overrides old '{provides_index[cleaned_item]}'", file=sys.stderr)
                                        provides_index[cleaned_item] = current_recipe_path
                            except Exception as e_file:
                                print(f"Error reading or processing recipe '{current_recipe_path}' for index: {e_file}", file=sys.stderr)
                    except OSError as e_pkg:
                        print(f"Error listing contents of package directory '{package_dir_path}': {e_pkg}", file=sys.stderr)
        except OSError as e_cat:
            print(f"Error listing contents of category directory '{category_path}': {e_cat}", file=sys.stderr)

    print(f"Built PROVIDES index with {len(provides_index)} entries.")
    return provides_index

def get_recipe_path_for_dependency(dependency_name, provides_index):
    """
    Retrieves the recipe file path for a given dependency name using the provides_index.

    Args:
        dependency_name (str): The cleaned, prefixed dependency name
                               (e.g., "cmd:make", "lib:zlib", "devel:libfoo").
        provides_index (dict): The pre-built dictionary mapping provided items
                               to their recipe file paths.

    Returns:
        str: The path to the recipe file that provides the dependency,
             or None if the dependency is not found in the index.
    """
    recipe_path = provides_index.get(dependency_name)
    if recipe_path:
        return recipe_path
    else:
        # print(f"Info: Dependency '{dependency_name}' not found in PROVIDES index.", file=sys.stderr) # Can be noisy
        return None

def main():
    """
    Main function to parse arguments and drive the dependency resolution process.
    It initializes the sets for tracking dependencies and processed packages,
    then calls the recursive resolver for each user-supplied package name.
    Finally, it filters the results and prints the list of prerequisites.
    """
    parser = argparse.ArgumentParser(
        description="Resolve build dependencies for HaikuPorts packages.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("package_names", nargs='+',
                        help="One or more package names to resolve dependencies for (e.g., 'openssl', 'cmd:make').")

    args = parser.parse_args()

    print("Building package provides index. This might take a moment...")
    provides_index = build_provides_index(HAIKUPORTS_ROOT)

    if not provides_index:
        print("Error: The provides index is empty. This could mean the script is not run from "
              "the root of a HaikuPorts checkout, or no recipes were found/parsed correctly.", file=sys.stderr)
        sys.exit(1)

    initial_packages_from_args = set(args.package_names)
    all_found_dependencies = set()
    processed_recipe_paths = set()

    print(f"Attempting to resolve dependencies for initial package(s): {', '.join(sorted(list(initial_packages_from_args)))}")

    for user_pkg_name in initial_packages_from_args:
        found_dep_name_in_index = None

        # Order of preference for looking up the user-provided package name
        prefixes_to_try = ["", "package:", "cmd:", "lib:", "devel:", "hpkg:", "generic:", "source:"]

        # If user typed a prefixed name, try that first and primarily.
        is_user_prefixed = ":" in user_pkg_name and user_pkg_name.split(":",1)[0]+":" in prefixes_to_try

        if is_user_prefixed:
            if user_pkg_name in provides_index:
                found_dep_name_in_index = user_pkg_name
        else: # User typed a base name (e.g., "openssl")
            for prefix in prefixes_to_try:
                potential_name = prefix + user_pkg_name
                if potential_name in provides_index:
                    found_dep_name_in_index = potential_name
                    break

        if found_dep_name_in_index:
            # print(f"Found initial package '{user_pkg_name}' as '{found_dep_name_in_index}' in index.") # Verbose
            all_found_dependencies.add(found_dep_name_in_index)
            resolve_dependencies_recursive(found_dep_name_in_index, all_found_dependencies, processed_recipe_paths, provides_index)
        else:
            print(f"ERROR: Could not find a recipe in the index that provides '{user_pkg_name}' or its common prefixed variants. "
                  "It might be a typo or not a directly providable package name.", file=sys.stderr)

    final_dependencies_to_install = set()
    for dep_in_all_deps in all_found_dependencies:
        base_name_of_dep = re.sub(r"^(package:|cmd:|lib:|devel:|hpkg:|generic:|source:)", "", dep_in_all_deps)

        if dep_in_all_deps not in initial_packages_from_args and \
           base_name_of_dep not in initial_packages_from_args:
            final_dependencies_to_install.add(dep_in_all_deps)

    if final_dependencies_to_install:
        print("\nFinal list of prerequisite packages (excluding initially specified packages; prefixes retained):")
        for dep in sorted(list(final_dependencies_to_install)):
            print(dep)
    else:
        if not all_found_dependencies and initial_packages_from_args:
             print(f"\nNo dependencies found for the specified package(s): {', '.join(sorted(list(initial_packages_from_args)))}. "
                   "They might be meta-packages, have no listed build requirements, their recipes were not found in the index, or there was a parsing error.")
        elif not all_found_dependencies:
             print(f"\nNo packages or dependencies processed or found.")
        else:
             print("\nNo additional prerequisite packages found beyond those specified (or the specified packages are themselves the only dependencies, considering prefixes).")

if __name__ == "__main__":
    main()
