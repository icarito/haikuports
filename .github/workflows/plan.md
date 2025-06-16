Como puedes ver a continuacion el cache parece no ser detectado correctamente. Podemos simplificar todo, dejar todo en un solo job y subir la data de depedencias directamente al VM sin tener que hacer dos pasos?


2025-06-14T19:27:46.3061060Z Current runner version: '2.325.0'
2025-06-14T19:27:46.3085797Z ##[group]Operating System
2025-06-14T19:27:46.3086533Z Ubuntu
2025-06-14T19:27:46.3087026Z 24.04.2
2025-06-14T19:27:46.3087531Z LTS
2025-06-14T19:27:46.3088025Z ##[endgroup]
2025-06-14T19:27:46.3088551Z ##[group]Runner Image
2025-06-14T19:27:46.3089685Z Image: ubuntu-24.04
2025-06-14T19:27:46.3090232Z Version: 20250609.1.0
2025-06-14T19:27:46.3091447Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20250609.1/images/ubuntu/Ubuntu2404-Readme.md
2025-06-14T19:27:46.3092982Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20250609.1
2025-06-14T19:27:46.3093835Z ##[endgroup]
2025-06-14T19:27:46.3094346Z ##[group]Runner Image Provisioner
2025-06-14T19:27:46.3095012Z 2.0.437.1
2025-06-14T19:27:46.3095432Z ##[endgroup]
2025-06-14T19:27:46.3097837Z ##[group]GITHUB_TOKEN Permissions
2025-06-14T19:27:46.3100097Z Actions: write
2025-06-14T19:27:46.3100787Z Attestations: write
2025-06-14T19:27:46.3101613Z Checks: write
2025-06-14T19:27:46.3102104Z Contents: write
2025-06-14T19:27:46.3102638Z Deployments: write
2025-06-14T19:27:46.3103167Z Discussions: write
2025-06-14T19:27:46.3103656Z Issues: write
2025-06-14T19:27:46.3104169Z Metadata: read
2025-06-14T19:27:46.3104653Z Models: read
2025-06-14T19:27:46.3105125Z Packages: write
2025-06-14T19:27:46.3105558Z Pages: write
2025-06-14T19:27:46.3106132Z PullRequests: write
2025-06-14T19:27:46.3106614Z RepositoryProjects: write
2025-06-14T19:27:46.3107144Z SecurityEvents: write
2025-06-14T19:27:46.3107675Z Statuses: write
2025-06-14T19:27:46.3108159Z ##[endgroup]
2025-06-14T19:27:46.3110134Z Secret source: Actions
2025-06-14T19:27:46.3111632Z Prepare workflow directory
2025-06-14T19:27:46.3439544Z Prepare all required actions
2025-06-14T19:27:46.3477344Z Getting action download info
2025-06-14T19:27:46.6477585Z ##[group]Download immutable action package 'actions/checkout@v4'
2025-06-14T19:27:46.6478542Z Version: 4.2.2
2025-06-14T19:27:46.6479484Z Digest: sha256:ccb2698953eaebd21c7bf6268a94f9c26518a7e38e27e0b83c1fe1ad049819b1
2025-06-14T19:27:46.6480733Z Source commit SHA: 11bd71901bbe5b1630ceea73d27597364c9af683
2025-06-14T19:27:46.6481677Z ##[endgroup]
2025-06-14T19:27:46.7584308Z ##[group]Download immutable action package 'actions/setup-python@v4'
2025-06-14T19:27:46.7585056Z Version: 4.9.1
2025-06-14T19:27:46.7585775Z Digest: sha256:f03e505388af670b5a108629e0ba26befc08d5c62b41f46146a45fe29ae509a5
2025-06-14T19:27:46.7586822Z Source commit SHA: 7f4fc3e22c37d6ff65e88745f38bd3157c663f7c
2025-06-14T19:27:46.7587461Z ##[endgroup]
2025-06-14T19:27:46.9998192Z ##[group]Download immutable action package 'actions/cache@v4'
2025-06-14T19:27:46.9998909Z Version: 4.2.3
2025-06-14T19:27:46.9999696Z Digest: sha256:c8a3bb963e1f1826d8fcc8d1354f0dd29d8ac1db1d4f6f20247055ae11b81ed9
2025-06-14T19:27:47.0000701Z Source commit SHA: 5a3ec84eff668545956fd18022155c47e93e2684
2025-06-14T19:27:47.0001673Z ##[endgroup]
2025-06-14T19:27:47.1836999Z Complete job name: prepare-build
2025-06-14T19:27:47.2512503Z ##[group]Run actions/checkout@v4
2025-06-14T19:27:47.2513322Z with:
2025-06-14T19:27:47.2513685Z   fetch-depth: 0
2025-06-14T19:27:47.2514091Z   repository: icarito/haikuports
2025-06-14T19:27:47.2514691Z   token: ***
2025-06-14T19:27:47.2515056Z   ssh-strict: true
2025-06-14T19:27:47.2515417Z   ssh-user: git
2025-06-14T19:27:47.2515801Z   persist-credentials: true
2025-06-14T19:27:47.2516226Z   clean: true
2025-06-14T19:27:47.2516606Z   sparse-checkout-cone-mode: true
2025-06-14T19:27:47.2517079Z   fetch-tags: false
2025-06-14T19:27:47.2517445Z   show-progress: true
2025-06-14T19:27:47.2517818Z   lfs: false
2025-06-14T19:27:47.2518157Z   submodules: false
2025-06-14T19:27:47.2518537Z   set-safe-directory: true
2025-06-14T19:27:47.2519149Z ##[endgroup]
2025-06-14T19:27:47.5278773Z Syncing repository: icarito/haikuports
2025-06-14T19:27:47.5280924Z ##[group]Getting Git version info
2025-06-14T19:27:47.5281964Z Working directory is '/home/runner/work/haikuports/haikuports'
2025-06-14T19:27:47.5283267Z [command]/usr/bin/git version
2025-06-14T19:27:47.5408627Z git version 2.49.0
2025-06-14T19:27:47.5445574Z ##[endgroup]
2025-06-14T19:27:47.5460782Z Temporarily overriding HOME='/home/runner/work/_temp/3608443c-0517-473b-9381-6eb9d7bc3279' before making global git config changes
2025-06-14T19:27:47.5463376Z Adding repository directory to the temporary git global config as a safe directory
2025-06-14T19:27:47.5473982Z [command]/usr/bin/git config --global --add safe.directory /runner/work/haikuports/haikuports
2025-06-14T19:27:47.5515831Z Deleting the contents of '/home/runner/work/haikuports/haikuports'
2025-06-14T19:27:47.5519609Z ##[group]Initializing the repository
2025-06-14T19:27:47.5524711Z [command]/usr/bin/git init /runner/work/haikuports/haikuports
2025-06-14T19:27:47.5644826Z hint: Using 'master' as the name for the initial branch. This default branch name
2025-06-14T19:27:47.5646128Z hint: is subject to change. To configure the initial branch name to use in all
2025-06-14T19:27:47.5647035Z hint: of your new repositories, which will suppress this warning, call:
2025-06-14T19:27:47.5647670Z hint:
2025-06-14T19:27:47.5648231Z hint: 	git config --global init.defaultBranch <name>
2025-06-14T19:27:47.5649083Z hint:
2025-06-14T19:27:47.5649812Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2025-06-14T19:27:47.5650672Z hint: 'development'. The just-created branch can be renamed via this command:
2025-06-14T19:27:47.5651543Z hint:
2025-06-14T19:27:47.5651909Z hint: 	git branch -m <name>
2025-06-14T19:27:47.5671707Z Initialized empty Git repository in /runner/work/haikuports/haikuports/.git/
2025-06-14T19:27:47.5683876Z [command]/usr/bin/git remote add origin https://github.com/icarito/haikuports
2025-06-14T19:27:47.5724409Z ##[endgroup]
2025-06-14T19:27:47.5725562Z ##[group]Disabling automatic garbage collection
2025-06-14T19:27:47.5729484Z [command]/usr/bin/git config --local gc.auto 0
2025-06-14T19:27:47.5760695Z ##[endgroup]
2025-06-14T19:27:47.5762158Z ##[group]Setting up auth
2025-06-14T19:27:47.5768530Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2025-06-14T19:27:47.5799845Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2025-06-14T19:27:47.6176676Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2025-06-14T19:27:47.6204369Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2025-06-14T19:27:47.6424690Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2025-06-14T19:27:47.6459785Z ##[endgroup]
2025-06-14T19:27:47.6460975Z ##[group]Fetching the repository
2025-06-14T19:27:47.6468613Z [command]/usr/bin/git -c protocol.version=2 fetch --prune --no-recurse-submodules origin +refs/heads/*:refs/remotes/origin/* +refs/tags/*:refs/tags/*
2025-06-14T19:27:52.1259399Z From https://github.com/icarito/haikuports
2025-06-14T19:27:52.1261276Z  * [new branch]          autobuilder             -> origin/autobuilder
2025-06-14T19:27:52.1262705Z  * [new branch]          develop                 -> origin/develop
2025-06-14T19:27:52.1264222Z  * [new branch]          development             -> origin/development
2025-06-14T19:27:52.1265775Z  * [new branch]          gtk4                    -> origin/gtk4
2025-06-14T19:27:52.1267275Z  * [new branch]          gtk4-libadwaita-and-friends -> origin/gtk4-libadwaita-and-friends
2025-06-14T19:27:52.1268877Z  * [new branch]          gtk4_old                -> origin/gtk4_old
2025-06-14T19:27:52.1270412Z  * [new branch]          master                  -> origin/master
2025-06-14T19:27:52.1271843Z  * [new branch]          optimize-haiku-checkout -> origin/optimize-haiku-checkout
2025-06-14T19:27:52.1316031Z [command]/usr/bin/git branch --list --remote origin/development
2025-06-14T19:27:52.1338616Z   origin/development
2025-06-14T19:27:52.1348120Z [command]/usr/bin/git rev-parse refs/remotes/origin/development
2025-06-14T19:27:52.1368941Z 63b53c782f0409298c5b9fc44661b627ea21230d
2025-06-14T19:27:52.1375859Z ##[endgroup]
2025-06-14T19:27:52.1377840Z ##[group]Determining the checkout info
2025-06-14T19:27:52.1379530Z ##[endgroup]
2025-06-14T19:27:52.1382079Z [command]/usr/bin/git sparse-checkout disable
2025-06-14T19:27:52.1423010Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2025-06-14T19:27:52.1450167Z ##[group]Checking out the ref
2025-06-14T19:27:52.1455039Z [command]/usr/bin/git checkout --progress --force -B development refs/remotes/origin/development
2025-06-14T19:27:52.8218472Z Switched to a new branch 'development'
2025-06-14T19:27:52.8219481Z branch 'development' set up to track 'origin/development'.
2025-06-14T19:27:52.8252098Z ##[endgroup]
2025-06-14T19:27:52.8293505Z [command]/usr/bin/git log -1 --format=%H
2025-06-14T19:27:52.8315459Z 63b53c782f0409298c5b9fc44661b627ea21230d
2025-06-14T19:27:52.8536294Z ##[group]Run actions/setup-python@v4
2025-06-14T19:27:52.8536674Z with:
2025-06-14T19:27:52.8536932Z   python-version: 3.9
2025-06-14T19:27:52.8537214Z   check-latest: false
2025-06-14T19:27:52.8537651Z   token: ***
2025-06-14T19:27:52.8537938Z   update-environment: true
2025-06-14T19:27:52.8538251Z   allow-prereleases: false
2025-06-14T19:27:52.8538538Z ##[endgroup]
2025-06-14T19:27:53.0167334Z ##[group]Installed versions
2025-06-14T19:27:53.0249312Z Successfully set up CPython (3.9.23)
2025-06-14T19:27:53.0250108Z ##[endgroup]
2025-06-14T19:27:53.0352192Z ##[group]Run git clone https://github.com/haikuports/haikuporter.git ~/haikuporter
2025-06-14T19:27:53.0352999Z [36;1mgit clone https://github.com/haikuports/haikuporter.git ~/haikuporter[0m
2025-06-14T19:27:53.0353619Z [36;1msudo ln -s "$HOME/haikuporter/haikuporter" /local/bin/haikuporter[0m
2025-06-14T19:27:53.0354125Z [36;1mecho "HaikuPorter installed. Version:"[0m
2025-06-14T19:27:53.0354490Z [36;1mhaikuporter --version[0m
2025-06-14T19:27:53.0472184Z shell: /bin/bash --noprofile --norc -e -o pipefail {0}
2025-06-14T19:27:53.0472604Z env:
2025-06-14T19:27:53.0472909Z   pythonLocation: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.0473411Z   PKG_CONFIG_PATH: /hostedtoolcache/Python/3.9.23/x64/lib/pkgconfig
2025-06-14T19:27:53.0473894Z   Python_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.0474333Z   Python2_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.0474792Z   Python3_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.0475214Z   LD_LIBRARY_PATH: /hostedtoolcache/Python/3.9.23/x64/lib
2025-06-14T19:27:53.0475576Z ##[endgroup]
2025-06-14T19:27:53.0590644Z Cloning into '/home/runner/haikuporter'...
2025-06-14T19:27:53.5505737Z HaikuPorter installed. Version:
2025-06-14T19:27:53.7103738Z haikuporter 1.3.2
2025-06-14T19:27:53.7222250Z ##[group]Run echo "TREE_PATH=\"/home/runner/work/haikuports/haikuports\"" > "/home/runner/work/haikuports/haikuports/haikuports.conf"
2025-06-14T19:27:53.7223188Z [36;1mecho "TREE_PATH=\"/home/runner/work/haikuports/haikuports\"" > "/home/runner/work/haikuports/haikuports/haikuports.conf"[0m
2025-06-14T19:27:53.7284661Z [36;1mecho "PACKAGER=\"CI Builder <ci@example.com>\"" >> "/home/runner/work/haikuports/haikuports/haikuports.conf"[0m
2025-06-14T19:27:53.7285907Z [36;1mecho "TARGET_ARCHITECTURE=\"x86_64\"" >> "/home/runner/work/haikuports/haikuports/haikuports.conf"[0m
2025-06-14T19:27:53.7287015Z [36;1mecho "HaikuPorter configuration created at /runner/work/haikuports/haikuports/haikuports.conf:"[0m
2025-06-14T19:27:53.7288075Z [36;1mcat "/home/runner/work/haikuports/haikuports/haikuports.conf"[0m
2025-06-14T19:27:53.7353661Z shell: /bin/bash --noprofile --norc -e -o pipefail {0}
2025-06-14T19:27:53.7353985Z env:
2025-06-14T19:27:53.7354265Z   pythonLocation: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.7354878Z   PKG_CONFIG_PATH: /hostedtoolcache/Python/3.9.23/x64/lib/pkgconfig
2025-06-14T19:27:53.7355261Z   Python_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.7355596Z   Python2_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.7355928Z   Python3_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.7356273Z   LD_LIBRARY_PATH: /hostedtoolcache/Python/3.9.23/x64/lib
2025-06-14T19:27:53.7356552Z ##[endgroup]
2025-06-14T19:27:53.7439232Z HaikuPorter configuration created at /runner/work/haikuports/haikuports/haikuports.conf:
2025-06-14T19:27:53.7448476Z TREE_PATH="/home/runner/work/haikuports/haikuports"
2025-06-14T19:27:53.7449021Z PACKAGER="CI Builder <ci@example.com>"
2025-06-14T19:27:53.7449449Z TARGET_ARCHITECTURE="x86_64"
2025-06-14T19:27:53.7476186Z ##[group]Run wget https://github.com/waddlesplash/haiku-licenses/archive/master.zip -O haiku-licenses.zip
2025-06-14T19:27:53.7476942Z [36;1mwget https://github.com/waddlesplash/haiku-licenses/archive/master.zip -O haiku-licenses.zip[0m
2025-06-14T19:27:53.7477436Z [36;1munzip -q haiku-licenses.zip[0m
2025-06-14T19:27:53.7477784Z [36;1mecho "Haiku Licenses downloaded and unzipped. Found directories:"[0m
2025-06-14T19:27:53.7478391Z [36;1mls -d /runner/work/haikuports/haikuports/haiku-licenses-*/ # Verify directory name relative to workspace[0m
2025-06-14T19:27:53.7533272Z shell: /bin/bash --noprofile --norc -e -o pipefail {0}
2025-06-14T19:27:53.7533577Z env:
2025-06-14T19:27:53.7533814Z   pythonLocation: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.7534211Z   PKG_CONFIG_PATH: /hostedtoolcache/Python/3.9.23/x64/lib/pkgconfig
2025-06-14T19:27:53.7534589Z   Python_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.7534952Z   Python2_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.7535318Z   Python3_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:53.7535655Z   LD_LIBRARY_PATH: /hostedtoolcache/Python/3.9.23/x64/lib
2025-06-14T19:27:53.7535946Z ##[endgroup]
2025-06-14T19:27:53.7652093Z --2025-06-14 19:27:53--  https://github.com/waddlesplash/haiku-licenses/archive/master.zip
2025-06-14T19:27:53.7904990Z Resolving github.com (github.com)... 140.82.113.3
2025-06-14T19:27:53.8061946Z Connecting to github.com (github.com)|140.82.113.3|:443... connected.
2025-06-14T19:27:53.9184805Z HTTP request sent, awaiting response... 302 Found
2025-06-14T19:27:53.9185685Z Location: https://codeload.github.com/waddlesplash/haiku-licenses/zip/refs/heads/master [following]
2025-06-14T19:27:53.9718539Z --2025-06-14 19:27:53--  https://codeload.github.com/waddlesplash/haiku-licenses/zip/refs/heads/master
2025-06-14T19:27:53.9719540Z Resolving codeload.github.com (codeload.github.com)... 140.82.112.9
2025-06-14T19:27:53.9875080Z Connecting to codeload.github.com (codeload.github.com)|140.82.112.9|:443... connected.
2025-06-14T19:27:54.0829218Z HTTP request sent, awaiting response... 200 OK
2025-06-14T19:27:54.0830445Z Length: unspecified [application/zip]
2025-06-14T19:27:54.0831775Z Saving to: ‘haiku-licenses.zip’
2025-06-14T19:27:54.0832127Z 
2025-06-14T19:27:54.1142063Z      0K .......... .......... .......... .......... .......... 1.57M
2025-06-14T19:27:54.1299785Z     50K .......... .......... .......... .......... .......... 3.09M
2025-06-14T19:27:54.1301474Z    100K ..........                                             72.4M=0.05s
2025-06-14T19:27:54.1301908Z 
2025-06-14T19:27:54.1303321Z 2025-06-14 19:27:54 (2.29 MB/s) - ‘haiku-licenses.zip’ saved [113160]
2025-06-14T19:27:54.1303790Z 
2025-06-14T19:27:54.1386681Z Haiku Licenses downloaded and unzipped. Found directories:
2025-06-14T19:27:54.1399514Z /runner/work/haikuports/haikuports/haiku-licenses-master/
2025-06-14T19:27:54.1431397Z ##[group]Run git config --global --add safe.directory "$GITHUB_WORKSPACE"
2025-06-14T19:27:54.1431982Z [36;1mgit config --global --add safe.directory "$GITHUB_WORKSPACE"[0m
2025-06-14T19:27:54.1432502Z [36;1mGIT_PRIMARY_BRANCH_REF=""[0m
2025-06-14T19:27:54.1432744Z [36;1mPRIMARY_BRANCH_SHA_VALUE=""[0m
2025-06-14T19:27:54.1432969Z [36;1m[0m
2025-06-14T19:27:54.1433216Z [36;1mif git rev-parse --verify origin/main >/dev/null 2>&1; then[0m
2025-06-14T19:27:54.1433568Z [36;1m  GIT_PRIMARY_BRANCH_REF="origin/main"[0m
2025-06-14T19:27:54.1433909Z [36;1melif git rev-parse --verify origin/master >/dev/null 2>&1; then[0m
2025-06-14T19:27:54.1434256Z [36;1m  GIT_PRIMARY_BRANCH_REF="origin/master"[0m
2025-06-14T19:27:54.1434496Z [36;1mfi[0m
2025-06-14T19:27:54.1434654Z [36;1m[0m
2025-06-14T19:27:54.1434849Z [36;1mif [ -z "$GIT_PRIMARY_BRANCH_REF" ]; then[0m
2025-06-14T19:27:54.1435350Z [36;1m  echo "::warning::No main or master branch found at origin to compare against. Assuming all recipes need checking."[0m
2025-06-14T19:27:54.1435925Z [36;1m  CHANGED_RECIPES=$(find . -name '*.recipe' -printf '%h\n' | sed 's|^\./||' | sort -u)[0m
2025-06-14T19:27:54.1436362Z [36;1m  echo "build_all_flag=true" >> $GITHUB_OUTPUT [0m
2025-06-14T19:27:54.1436628Z [36;1melse[0m
2025-06-14T19:27:54.1436877Z [36;1m  echo "Primary branch for comparison: $GIT_PRIMARY_BRANCH_REF"[0m
2025-06-14T19:27:54.1437235Z [36;1m  if [ "$GITHUB_EVENT_NAME" == "pull_request" ]; then[0m
2025-06-14T19:27:54.1437738Z [36;1m    # For PRs, diff against the merge base with the target branch (already fetched by checkout@v4 with ref: )[0m
2025-06-14T19:27:54.1438188Z [36;1m    TARGET_REF="origin/$GITHUB_BASE_REF"[0m
2025-06-14T19:27:54.1438475Z [36;1m    git fetch origin "$GITHUB_BASE_REF" --depth=1[0m
2025-06-14T19:27:54.1438790Z [36;1m    MERGE_BASE=$(git merge-base HEAD "$TARGET_REF")[0m
2025-06-14T19:27:54.1439217Z [36;1m    echo "Pull Request: Diffing from merge base $MERGE_BASE to HEAD ($GITHUB_SHA)"[0m
2025-06-14T19:27:54.1439772Z [36;1m    CHANGED_RECIPES=$(git diff --name-only "$MERGE_BASE" HEAD -- '*/*.recipe' | sed 's|/[^/]*\.recipe$||g' | sort -u)[0m
2025-06-14T19:27:54.1440214Z [36;1m  else[0m
2025-06-14T19:27:54.1440560Z [36;1m    echo "Push/Manual Trigger: Diffing from $GIT_PRIMARY_BRANCH_REF to HEAD ($GITHUB_SHA)"[0m
2025-06-14T19:27:54.1441343Z [36;1m    # Ensure the primary branch is fetched for an accurate diff base and for rev-parse later[0m
2025-06-14T19:27:54.1441841Z [36;1m    # fetch-depth:0 should get it, but this is an explicit safeguard.[0m
2025-06-14T19:27:54.1442526Z [36;1m    git fetch origin "$(echo $GIT_PRIMARY_BRANCH_REF | sed 's|origin/||')" --depth=1 --no-tags || echo "::warning::Failed to fetch $GIT_PRIMARY_BRANCH_REF, diff might be inaccurate."[0m
2025-06-14T19:27:54.1443357Z [36;1m    CHANGED_RECIPES=$(git diff --name-only "$GIT_PRIMARY_BRANCH_REF...HEAD" -- '*/*.recipe' | sed 's|/[^/]*\.recipe$||g' | sort -u)[0m
2025-06-14T19:27:54.1443828Z [36;1m  fi[0m
2025-06-14T19:27:54.1444034Z [36;1m  echo "build_all_flag=false" >> $GITHUB_OUTPUT[0m
2025-06-14T19:27:54.1444289Z [36;1mfi[0m
2025-06-14T19:27:54.1444438Z [36;1m[0m
2025-06-14T19:27:54.1444628Z [36;1mif [ -n "$GIT_PRIMARY_BRANCH_REF" ]; then[0m
2025-06-14T19:27:54.1445012Z [36;1m  PRIMARY_BRANCH_SHA_VALUE=$(git rev-parse "$GIT_PRIMARY_BRANCH_REF" 2>/dev/null)[0m
2025-06-14T19:27:54.1445403Z [36;1m  if [ -z "$PRIMARY_BRANCH_SHA_VALUE" ]; then[0m
2025-06-14T19:27:54.1445831Z [36;1m      echo "::warning::Failed to parse SHA for $GIT_PRIMARY_BRANCH_REF. Cache key will use GITHUB_SHA."[0m
2025-06-14T19:27:54.1446328Z [36;1m      PRIMARY_BRANCH_SHA_VALUE="63b53c782f0409298c5b9fc44661b627ea21230d"[0m
2025-06-14T19:27:54.1446656Z [36;1m  fi[0m
2025-06-14T19:27:54.1446814Z [36;1melse[0m
2025-06-14T19:27:54.1447080Z [36;1m  echo "::debug::No primary branch ref, using GITHUB_SHA for cache key."[0m
2025-06-14T19:27:54.1447662Z [36;1m  PRIMARY_BRANCH_SHA_VALUE="63b53c782f0409298c5b9fc44661b627ea21230d"[0m
2025-06-14T19:27:54.1447984Z [36;1mfi[0m
2025-06-14T19:27:54.1448258Z [36;1mecho "primary_branch_sha=${PRIMARY_BRANCH_SHA_VALUE}" >> $GITHUB_OUTPUT[0m
2025-06-14T19:27:54.1448584Z [36;1m[0m
2025-06-14T19:27:54.1448933Z [36;1mCHANGED_RECIPES=$(echo "$CHANGED_RECIPES" | sed '/^$/d')[0m
2025-06-14T19:27:54.1449220Z [36;1m[0m
2025-06-14T19:27:54.1449401Z [36;1mif [ -z "$CHANGED_RECIPES" ]; then[0m
2025-06-14T19:27:54.1449649Z [36;1m  echo "No recipes changed."[0m
2025-06-14T19:27:54.1449933Z [36;1m  echo "changed_recipes_json=[]" >> $GITHUB_OUTPUT[0m
2025-06-14T19:27:54.1450261Z [36;1m  echo "has_changed_recipes=false" >> $GITHUB_OUTPUT[0m
2025-06-14T19:27:54.1450522Z [36;1melse[0m
2025-06-14T19:27:54.1450703Z [36;1m  echo "Changed recipes found:"[0m
2025-06-14T19:27:54.1450940Z [36;1m  echo "$CHANGED_RECIPES"[0m
2025-06-14T19:27:54.1451502Z [36;1m  CHANGED_RECIPES_JSON=$(echo "$CHANGED_RECIPES" | jq -R -s -c 'split("\n") | map(select(length > 0))')[0m
2025-06-14T19:27:54.1452027Z [36;1m  echo "changed_recipes_json=$CHANGED_RECIPES_JSON" >> $GITHUB_OUTPUT[0m
2025-06-14T19:27:54.1452424Z [36;1m  echo "has_changed_recipes=true" >> $GITHUB_OUTPUT[0m
2025-06-14T19:27:54.1452687Z [36;1mfi[0m
2025-06-14T19:27:54.1516118Z shell: /bin/bash --noprofile --norc -e -o pipefail {0}
2025-06-14T19:27:54.1516421Z env:
2025-06-14T19:27:54.1516655Z   pythonLocation: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:54.1517049Z   PKG_CONFIG_PATH: /hostedtoolcache/Python/3.9.23/x64/lib/pkgconfig
2025-06-14T19:27:54.1517429Z   Python_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:54.1517762Z   Python2_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:54.1518089Z   Python3_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:54.1518421Z   LD_LIBRARY_PATH: /hostedtoolcache/Python/3.9.23/x64/lib
2025-06-14T19:27:54.1518695Z ##[endgroup]
2025-06-14T19:27:54.1644511Z Primary branch for comparison: origin/master
2025-06-14T19:27:54.1645188Z Push/Manual Trigger: Diffing from origin/master to HEAD (63b53c782f0409298c5b9fc44661b627ea21230d)
2025-06-14T19:27:54.5007228Z From https://github.com/icarito/haikuports
2025-06-14T19:27:54.5007627Z  * branch                master     -> FETCH_HEAD
2025-06-14T19:27:54.5108076Z Changed recipes found:
2025-06-14T19:27:54.5108446Z gui-libs/gtk4
2025-06-14T19:27:54.5213770Z ##[group]Run echo "Starting Hybrid .DependencyInfo Generation Process..."
2025-06-14T19:27:54.5214278Z [36;1mecho "Starting Hybrid .DependencyInfo Generation Process..."[0m
2025-06-14T19:27:54.5214867Z [36;1mLICENSES_DIR_NAME=$(ls -d /runner/work/haikuports/haikuports/haiku-licenses-*/ | head -n 1 | xargs basename)[0m
2025-06-14T19:27:54.5215612Z [36;1mecho "Using licenses directory: $LICENSES_DIR_NAME at /runner/work/haikuports/haikuports/$LICENSES_DIR_NAME"[0m
2025-06-14T19:27:54.5216075Z [36;1m[0m
2025-06-14T19:27:54.5216337Z [36;1m# Create directories needed by HaikuPorter and for dummy flags[0m
2025-06-14T19:27:54.5216751Z [36;1mmkdir -p "/home/runner/work/haikuports/haikuports/packages"[0m
2025-06-14T19:27:54.5217215Z [36;1mmkdir -p "/home/runner/work/haikuports/haikuports/repository" # REPOSITORY_PATH[0m
2025-06-14T19:27:54.5217701Z [36;1mmkdir -p "/home/runner/work/haikuports/haikuports/dummy_mimedb"[0m
2025-06-14T19:27:54.5218153Z [36;1mmkdir -p "/home/runner/work/haikuports/haikuports/dummy_cross_tools"[0m
2025-06-14T19:27:54.5218481Z [36;1m[0m
2025-06-14T19:27:54.5218727Z [36;1mecho "Running global 'haikuporter --repository-update'..."[0m
2025-06-14T19:27:54.5219578Z [36;1mhaikuporter --config="/home/runner/work/haikuports/haikuports/haikuports.conf"                --licenses="/home/runner/work/haikuports/haikuports/$LICENSES_DIR_NAME"                --repository-update[0m
2025-06-14T19:27:54.5220312Z [36;1m[0m
2025-06-14T19:27:54.5220483Z [36;1mHP_GLOBAL_UPDATE_EXIT_CODE=$?[0m
2025-06-14T19:27:54.5220757Z [36;1mif [ $HP_GLOBAL_UPDATE_EXIT_CODE -ne 0 ]; then[0m
2025-06-14T19:27:54.5221649Z [36;1m  echo "::warning::Global 'haikuporter --repository-update' failed with exit code $HP_GLOBAL_UPDATE_EXIT_CODE. Will rely solely on individual generation for changed recipes."[0m
2025-06-14T19:27:54.5222270Z [36;1melse[0m
2025-06-14T19:27:54.5222681Z [36;1m  echo "Global 'haikuporter --repository-update' completed."[0m
2025-06-14T19:27:54.5222982Z [36;1mfi[0m
2025-06-14T19:27:54.5223130Z [36;1m[0m
2025-06-14T19:27:54.5223562Z [36;1mecho "Listing contents of REPOSITORY_PATH (/home/runner/work/haikuports/haikuports/repository/) after global update:"[0m
2025-06-14T19:27:54.5224143Z [36;1mls -R "/home/runner/work/haikuports/haikuports/repository/"[0m
2025-06-14T19:27:54.5224440Z [36;1m[0m
2025-06-14T19:27:54.5224705Z [36;1mecho "Processing changed recipes to stage .DependencyInfo files..."[0m
2025-06-14T19:27:54.5225114Z [36;1m# THIS IS WHERE THE NEW SCRIPT'S LOGIC FOR CONSOLIDATION STARTS[0m
2025-06-14T19:27:54.5225600Z [36;1m# The old script had 'mkdir -p dependency-infos', the new one also has it but it's used differently.[0m
2025-06-14T19:27:54.5226168Z [36;1m# The provided script in the subtask is for "Ensure All Dependency Infos in Output Repository"[0m
2025-06-14T19:27:54.5226633Z [36;1m# I will use the script from the subtask description literally.[0m
2025-06-14T19:27:54.5226925Z [36;1m[0m
2025-06-14T19:27:54.5227369Z [36;1mecho "Final listing of consolidated REPOSITORY_PATH (/home/runner/work/haikuports/haikuports/repository/) before caching:"[0m
2025-06-14T19:27:54.5227967Z [36;1mls -R "/home/runner/work/haikuports/haikuports/repository/"[0m
2025-06-14T19:27:54.5228424Z [36;1m# Remove the now-unused 'dependency-infos' staging directory if it exists from old runs[0m
2025-06-14T19:27:54.5289404Z shell: /bin/bash --noprofile --norc -e -o pipefail {0}
2025-06-14T19:27:54.5289705Z env:
2025-06-14T19:27:54.5289933Z   pythonLocation: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:54.5290316Z   PKG_CONFIG_PATH: /hostedtoolcache/Python/3.9.23/x64/lib/pkgconfig
2025-06-14T19:27:54.5290686Z   Python_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:54.5291005Z   Python2_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:54.5291469Z   Python3_ROOT_DIR: /hostedtoolcache/Python/3.9.23/x64
2025-06-14T19:27:54.5291983Z   LD_LIBRARY_PATH: /hostedtoolcache/Python/3.9.23/x64/lib
2025-06-14T19:27:54.5292269Z ##[endgroup]
2025-06-14T19:27:54.5368685Z Starting Hybrid .DependencyInfo Generation Process...
2025-06-14T19:27:54.5412149Z Using licenses directory: haiku-licenses-master at /runner/work/haikuports/haikuports/haiku-licenses-master
2025-06-14T19:27:54.5460785Z Running global 'haikuporter --repository-update'...
2025-06-14T19:27:54.8998373Z Warning: Found old repository format - repopulating the repository ...
2025-06-14T19:27:57.0627147Z Populating repository ...
2025-06-14T19:27:57.0627682Z 	updating dependency infos of 0ad-0.0.23b~alpha
2025-06-14T19:27:57.0628229Z 	updating dependency infos of 0ad_data-0.0.23b~alpha
2025-06-14T19:27:57.0628926Z 	updating dependency infos of 1oom-1.0
2025-06-14T19:27:57.0629388Z 	updating dependency infos of 2048-1.1.1
2025-06-14T19:27:57.0629912Z 	updating dependency infos of 2048_libretro-1.0_20241227
2025-06-14T19:27:57.0630501Z 	recipe for 2cdt-2016.10.16 is still broken:
2025-06-14T19:27:57.0631313Z 	Error: package 2cdt-2016.10.16 cannot be built for architecture x86_64
2025-06-14T19:27:57.0631974Z 	recipe for 2dphysicsdemo-22.5.98 is still broken:
2025-06-14T19:27:57.0632497Z 	Error: No match found for license unknown
2025-06-14T19:27:57.0633029Z 	Error: Valid license filenames included with Haiku are:
2025-06-14T19:27:57.0635945Z 	Error: Anti-Grain Geometry, Apache v2, Artistic, Artistic v2.0, BSD (2-clause), BSD (3-clause), BSD (4-clause), Be Sample Code License, Bullet, CDDL v1, CQuantizer, DEC, GLUT (Mark Kilgard), GNU GPL font exception, GNU GPL v1, GNU GPL v2, GNU GPL v3, GNU LGPL v2, GNU LGPL v2.1, GNU LGPL v3, GPC, Intel (2xxx firmware), Intel (ACPICA), Intel (firmware), LibHTTPd, LibJPEG, LibPNG, MAPM, MIT, MIT (no promotion), MPL v1.1, MPL v2.0, Marvell (firmware), OpenGroup, PDFlib Lite, Public Domain, Ralink (firmware), SGI Free B, SIL Open Font License v1.1, Zlib
2025-06-14T19:27:57.0639454Z 	Error: (in /runner/work/haikuports/haikuports/sci-physics/2dphysicsdemo/2dphysicsdemo-22.5.98.recipe)
2025-06-14T19:27:57.0640314Z 	updating dependency infos of 2pow-1.2.2
2025-06-14T19:27:57.0640866Z 	updating dependency infos of 3dengine_libretro-1.0_20250304
2025-06-14T19:27:57.0641795Z 	updating dependency infos of 3dmov-0.2
2025-06-14T19:27:57.0642284Z 	updating dependency infos of 54321-1.0.2001.11.16
2025-06-14T19:27:57.0642929Z 	updating dependency infos of 64tass-1.60.3243
2025-06-14T19:27:57.0643406Z 	updating dependency infos of 7kaa-2.15.6
2025-06-14T19:27:57.0643854Z 	updating dependency infos of 7kaa_music-2.15
2025-06-14T19:27:57.0644352Z 	updating dependency infos of 81_libretro-1.0a_20241021
2025-06-14T19:27:57.0644913Z 	updating dependency infos of 8dock-0.9.5~git
2025-06-14T19:27:57.0645354Z 	updating dependency infos of a2ps-4.15.6
2025-06-14T19:27:57.0645787Z 	updating dependency infos of a52dec-0.8.0
2025-06-14T19:27:57.0646220Z 	updating dependency infos of a_book-1.1
2025-06-14T19:27:57.0646652Z 	updating dependency infos of aaaa-1.1
2025-06-14T19:27:57.0647078Z 	updating dependency infos of aalib-1.4~rc5
2025-06-14T19:27:57.0647566Z 	updating dependency infos of aalibtranslator-0.0.1
2025-06-14T19:27:57.0648077Z 	updating dependency infos of abaddon-0.2.2~git
2025-06-14T19:27:57.0648522Z 	updating dependency infos of abcl-1.9.2
2025-06-14T19:27:57.0648946Z 	updating dependency infos of abe-1.1
2025-06-14T19:27:57.0649531Z 	abi_compliance_checker-2.3 is still marked as untested on target architecture
2025-06-14T19:27:57.0650327Z 	abi_compliance_checker-1.98.3 is still marked as untested on target architecture
2025-06-14T19:27:57.0650960Z 	updating dependency infos of abiword-3.0.5
2025-06-14T19:27:57.0651663Z 	abrick-1.12 is still marked as untested on target architecture
2025-06-14T19:27:57.0652227Z 	updating dependency infos of abseil_cpp-20230125.3
2025-06-14T19:27:57.0652756Z 	updating dependency infos of abseil_cpp.2022-20220623.1
2025-06-14T19:27:57.0653322Z 	updating dependency infos of abseil_cpp.2025-20250127.0
2025-06-14T19:27:57.0653872Z 	updating dependency infos of abstrakt-0.0.1~20180515
2025-06-14T19:27:57.0654658Z 	abuse-0.8 is still marked as untested on target architecture
2025-06-14T19:27:57.0655225Z 	updating dependency infos of accounts_qml-0.7
2025-06-14T19:27:57.0655704Z 	updating dependency infos of ack-3.7.0
2025-06-14T19:27:57.0656109Z 	updating dependency infos of acme-0.96.5
2025-06-14T19:27:57.0656372Z 	updating dependency infos of acr-2.1.4
2025-06-14T19:27:57.0656703Z 	updating dependency infos of ada-2.9.2
2025-06-14T19:27:57.0656997Z 	updating dependency infos of admesh-0.98.5
2025-06-14T19:27:57.0657279Z 	updating dependency infos of advancemame-3.10
2025-06-14T19:27:57.0657575Z 	updating dependency infos of adwaita_icon_theme-42.0
2025-06-14T19:27:57.0657856Z 	recipe for aesaddon-0.3.1 is still broken:
2025-06-14T19:27:57.0658193Z 	Error: package aesaddon-0.3.1 cannot be built for architecture x86_64
2025-06-14T19:27:57.0658604Z 	aflplusplus-3.12c is still marked as untested on target architecture
2025-06-14T19:27:57.0658945Z 	updating dependency infos of agar-1.7.0
2025-06-14T19:27:57.0659204Z 	updating dependency infos of agg-2.7.0~r139
2025-06-14T19:27:57.0659470Z 	updating dependency infos of ahem-1.0
2025-06-14T19:27:57.0659731Z 	updating dependency infos of aiksaurus-1.2.2~git
2025-06-14T19:27:57.0660013Z 	updating dependency infos of aiodns-2.0.0
2025-06-14T19:27:57.0660272Z 	updating dependency infos of aiohttp-3.8.1
2025-06-14T19:27:57.0660532Z 	updating dependency infos of aiosignal-1.2.0
2025-06-14T19:27:57.0660808Z 	updating dependency infos of airstrike-0.99.6
2025-06-14T19:27:57.0661235Z 	updating dependency infos of akonadi-23.08.5
2025-06-14T19:27:57.0661671Z 	updating dependency infos of akonadi_calendar-23.08.5
2025-06-14T19:27:57.0661992Z 	updating dependency infos of akonadi_contacts-23.08.5
2025-06-14T19:27:57.0662306Z 	updating dependency infos of akonadi_mime-23.08.5
2025-06-14T19:27:57.0662608Z 	updating dependency infos of akonadi_notes-23.08.5
2025-06-14T19:27:57.0663068Z 	updating dependency infos of akonadi_search-23.08.5
2025-06-14T19:27:57.0663370Z 	updating dependency infos of akregator-23.08.5
2025-06-14T19:27:57.0663639Z 	updating dependency infos of al_anvar-0.5.0
2025-06-14T19:27:57.0663904Z 	updating dependency infos of alabaster-0.7.13
2025-06-14T19:27:57.0664163Z 	updating dependency infos of album-0.9.4
2025-06-14T19:27:57.0664413Z 	updating dependency infos of ale-0.9.1
2025-06-14T19:27:57.0664657Z 	updating dependency infos of alembic-1.8.3
2025-06-14T19:27:57.0664926Z 	updating dependency infos of alembic_py-1.13.2
2025-06-14T19:27:57.0665186Z 	updating dependency infos of alex4-1.0
2025-06-14T19:27:57.0665426Z 	updating dependency infos of alglib-4.00.0
2025-06-14T19:27:57.0665684Z 	updating dependency infos of algol68g-2.8.5
2025-06-14T19:27:57.0665952Z 	updating dependency infos of algorithm_diff-1.201
2025-06-14T19:27:57.0666236Z 	updating dependency infos of alien_build-2.84
2025-06-14T19:27:57.0666573Z 	updating dependency infos of alien_build_plugin_download_gitlab-0.01
2025-06-14T19:27:57.0666941Z 	updating dependency infos of alien_libxml2-0.19
2025-06-14T19:27:57.0667213Z 	updating dependency infos of alien_sdl-1.446
2025-06-14T19:27:57.0667488Z 	updating dependency infos of alienblaster-1.1.0
2025-06-14T19:27:57.0667772Z 	updating dependency infos of alivejournal-1.61
2025-06-14T19:27:57.0668038Z 	updating dependency infos of allegro-4.4.3.1
2025-06-14T19:27:57.0668308Z 	updating dependency infos of alligator-25.04.0
2025-06-14T19:27:57.0668619Z 	almp3-2.0.4 is still marked as untested on target architecture
2025-06-14T19:27:57.0668933Z 	updating dependency infos of amarok-3.2.2
2025-06-14T19:27:57.0669189Z 	updating dependency infos of amath-1.8.5
2025-06-14T19:27:57.0669438Z 	recipe for amc-1.14.0 is still broken:
2025-06-14T19:27:57.0669740Z 	Error: package amc-1.14.0 cannot be built for architecture x86_64
2025-06-14T19:27:57.0670078Z 	updating dependency infos of amd_microcode-20240116
2025-06-14T19:27:57.0670374Z 	updating dependency infos of amoebax-0.2.1
2025-06-14T19:27:57.0670620Z 	updating dependency infos of amule-2.3.3
2025-06-14T19:27:57.0671009Z 	updating dependency infos of an-1.2~git
2025-06-14T19:27:57.0671546Z 	updating dependency infos of anagramarama-0.7
2025-06-14T19:27:57.0671821Z 	updating dependency infos of analitza-23.08.5
2025-06-14T19:27:57.0672094Z 	updating dependency infos of analitza_kf6-25.04.0
2025-06-14T19:27:57.0672371Z 	updating dependency infos of ancestris-12
2025-06-14T19:27:57.0672630Z 	updating dependency infos of ancient-2.1.1
2025-06-14T19:27:57.0672924Z 	updating dependency infos of android_file_transfer-4.3~git
2025-06-14T19:27:57.0673232Z 	updating dependency infos of angband-4.2.4
2025-06-14T19:27:57.0673495Z 	updating dependency infos of angelscript-2.35.1
2025-06-14T19:27:57.0673937Z 	recipe for animator-1.0 is still broken:
2025-06-14T19:27:57.0674336Z 	Error: No match found for license Unknown
2025-06-14T19:27:57.0674629Z 	Error: Valid license filenames included with Haiku are:
2025-06-14T19:27:57.0676244Z 	Error: Anti-Grain Geometry, Apache v2, Artistic, Artistic v2.0, BSD (2-clause), BSD (3-clause), BSD (4-clause), Be Sample Code License, Bullet, CDDL v1, CQuantizer, DEC, GLUT (Mark Kilgard), GNU GPL font exception, GNU GPL v1, GNU GPL v2, GNU GPL v3, GNU LGPL v2, GNU LGPL v2.1, GNU LGPL v3, GPC, Intel (2xxx firmware), Intel (ACPICA), Intel (firmware), LibHTTPd, LibJPEG, LibPNG, MAPM, MIT, MIT (no promotion), MPL v1.1, MPL v2.0, Marvell (firmware), OpenGroup, PDFlib Lite, Public Domain, Ralink (firmware), SGI Free B, SIL Open Font License v1.1, Zlib
2025-06-14T19:27:57.0677929Z 	Error: (in /runner/work/haikuports/haikuports/haiku-apps/animator/animator-1.0.recipe)
2025-06-14T19:27:57.0678388Z 	updating dependency infos of anonymous_pro-1.002.001
2025-06-14T19:27:57.0678691Z 	updating dependency infos of another_world-0.0.1
2025-06-14T19:27:57.0678975Z 	updating dependency infos of ansiweather-1.18.0
2025-06-14T19:27:57.0679254Z 	updating dependency infos of ant_core-1.10.13
2025-06-14T19:27:57.0679720Z 	anthy-9100h is still marked as untested on target architecture
2025-06-14T19:27:57.0680070Z 	updating dependency infos of antigravitaattori-0.3.0
2025-06-14T19:27:57.0680355Z 	updating dependency infos of antiword-0.37
2025-06-14T19:27:57.0680623Z 	updating dependency infos of antlr_cpp-4.13.2
2025-06-14T19:27:57.0680913Z 	updating dependency infos of antlr_runtime-4.13.2
2025-06-14T19:27:57.0681422Z 	updating dependency infos of antlr_tool-4.13.2
2025-06-14T19:27:57.0681688Z 	updating dependency infos of anura-4.0.2
2025-06-14T19:27:57.0681941Z 	updating dependency infos of aobook-1.0.3_4
2025-06-14T19:27:57.0682200Z 	updating dependency infos of apache-2.4.63
2025-06-14T19:27:57.0682451Z 	updating dependency infos of apitrace-7.1
2025-06-14T19:27:57.0682766Z 	aplayer-4.0_svn is still marked as untested on target architecture
2025-06-14T19:27:57.0683079Z 	updating dependency infos of apng2gif-1.8
2025-06-14T19:27:57.0683328Z 	updating dependency infos of apngopt-1.4
2025-06-14T19:27:57.0683587Z 	updating dependency infos of app2png-1.0.0
2025-06-14T19:27:57.0683861Z 	updating dependency infos of appstream_glib-0.8.1
2025-06-14T19:27:57.0684133Z 	updating dependency infos of apr-1.7.5
2025-06-14T19:27:57.0684381Z 	updating dependency infos of apr_util-1.6.3
2025-06-14T19:27:57.0684639Z 	updating dependency infos of apsw-3.36.0~r1
2025-06-14T19:27:57.0684894Z 	updating dependency infos of aqbanking-6.5.4
2025-06-14T19:27:57.0685269Z 	updating dependency infos of aqemu-0.9.2
2025-06-14T19:27:57.0685569Z 	updating dependency infos of aquaria-1.1.3~git06072020
2025-06-14T19:27:57.0685866Z 	updating dependency infos of aquaskk-4.7.0.2
2025-06-14T19:27:57.0686130Z 	updating dependency infos of arabeyes_fonts-1.1
2025-06-14T19:27:57.0686428Z 	updating dependency infos of aranym-1.1.0
2025-06-14T19:27:57.0686667Z 	updating dependency infos of arc-5.21q
2025-06-14T19:27:57.0686935Z 	updating dependency infos of archive_extract-0.88
2025-06-14T19:27:57.0687213Z 	updating dependency infos of archive_zip-1.68
2025-06-14T19:27:57.0687537Z 	archiver-1.0.0 is still marked as broken on target architecture
2025-06-14T19:27:57.0687977Z 	updating dependency infos of arduino-1.6.1
2025-06-14T19:27:57.0688244Z 	updating dependency infos of argon2-20200709
2025-06-14T19:27:57.0688546Z 	updating dependency infos of argon2_cffi_bindings-21.2.0
2025-06-14T19:27:57.0688888Z 	updating dependency infos of argp_standalone-1.5.0
2025-06-14T19:27:57.0689202Z 	updating dependency infos of argparse_manpage-4.6
2025-06-14T19:27:57.0689489Z 	updating dependency infos of argtable2-13
2025-06-14T19:27:57.0689747Z 	updating dependency infos of aria2-1.36.0
2025-06-14T19:27:58.8228232Z 	updating dependency infos of arianna-23.08.5
2025-06-14T19:27:58.8228835Z 	updating dependency infos of arj-3.10.22
2025-06-14T19:27:58.8229280Z 	updating dependency infos of ark-23.08.5
2025-06-14T19:27:58.8229810Z 	updating dependency infos of arm_none_eabi_binutils-2.40
2025-06-14T19:27:58.8230385Z 	updating dependency infos of arm_none_eabi_gcc-13.1.0
2025-06-14T19:27:58.8230791Z 	updating dependency infos of arm_none_eabi_gcc_nolibc-13.1.0
2025-06-14T19:27:58.8231534Z 	recipe for arm_none_eabi_gdb-7.7 is still broken:
2025-06-14T19:27:58.8231934Z 	Error: package arm_none_eabi_gdb-7.7 cannot be built for architecture x86_64
2025-06-14T19:27:58.8232347Z 	updating dependency infos of arm_none_eabi_newlib-4.3.0
2025-06-14T19:27:58.8232661Z 	updating dependency infos of armadillo-12.6.3
2025-06-14T19:27:58.8232956Z 	updating dependency infos of armadillo10-10.8.2
2025-06-14T19:27:58.8233238Z 	updating dependency infos of armadillo9-9.900.6
2025-06-14T19:27:58.8233535Z 	updating dependency infos of armagetronad-0.2.9.1.0
2025-06-14T19:27:58.8233832Z 	updating dependency infos of armyknife-5.1.2
2025-06-14T19:27:58.8234103Z 	updating dependency infos of arpack-3.9.0
2025-06-14T19:27:58.8234371Z 	updating dependency infos of artpaint-2.7.1
2025-06-14T19:27:58.8234641Z 	updating dependency infos of arx_libertatis-1.2
2025-06-14T19:27:58.8235156Z 	updating dependency infos of asciidoc-10.2.0
2025-06-14T19:27:58.8235423Z 	updating dependency infos of asciinema-2.2.0
2025-06-14T19:27:58.8235694Z 	updating dependency infos of asio-1.31.0
2025-06-14T19:27:58.8235961Z 	updating dependency infos of asn1crypto-1.5.1
2025-06-14T19:27:58.8236242Z 	updating dependency infos of aspell-0.60.8.1
2025-06-14T19:27:58.8236522Z 	updating dependency infos of aspell6_cs-20040614_1
2025-06-14T19:27:58.8236815Z 	updating dependency infos of aspell_be-0.01
2025-06-14T19:27:58.8237085Z 	updating dependency infos of aspell_bg-4.1~0
2025-06-14T19:27:58.8237344Z 	updating dependency infos of aspell_ca-2.5.0
2025-06-14T19:27:58.8237630Z 	updating dependency infos of aspell_de-20161207_7_0
2025-06-14T19:27:58.8237927Z 	updating dependency infos of aspell_en-2020.12.07~0
2025-06-14T19:27:58.8238251Z 	updating dependency infos of aspell_eo-2.1.20000225a~2
2025-06-14T19:27:58.8238554Z 	updating dependency infos of aspell_es-1.11~2
2025-06-14T19:27:58.8238841Z 	updating dependency infos of aspell_fi-0.7~0
2025-06-14T19:27:58.8239123Z 	updating dependency infos of aspell_fr-0.50~3
2025-06-14T19:27:58.8239398Z 	updating dependency infos of aspell_hr-0.51~0
2025-06-14T19:27:58.8239689Z 	updating dependency infos of aspell_hu-0.99.4.2~0
2025-06-14T19:27:58.8239991Z 	updating dependency infos of aspell_it-2.4_20070901_0
2025-06-14T19:27:58.8240293Z 	updating dependency infos of aspell_lt-1.2.1~0
2025-06-14T19:27:58.8240568Z 	updating dependency infos of aspell_nl-0.50~2
2025-06-14T19:27:58.8240862Z 	updating dependency infos of aspell_pl-6.0_20061121~0
2025-06-14T19:27:58.8241396Z 	updating dependency infos of aspell_pt_br-20131030_12_0
2025-06-14T19:27:58.8241786Z 	updating dependency infos of aspell_pt_pt-20070510~0
2025-06-14T19:27:58.8242083Z 	updating dependency infos of aspell_ro-3.3~2
2025-06-14T19:27:58.8242359Z 	updating dependency infos of aspell_ru-0.99f7~1
2025-06-14T19:27:58.8242643Z 	updating dependency infos of aspell_sk-2.02~0
2025-06-14T19:27:58.8242909Z 	updating dependency infos of aspell_sl-0.50~0
2025-06-14T19:27:58.8243188Z 	updating dependency infos of aspell_sr-0.02
2025-06-14T19:27:58.8243588Z 	updating dependency infos of aspell_sv-0.51~0
2025-06-14T19:27:58.8243865Z 	updating dependency infos of aspell_uk-1.4.0~0
2025-06-14T19:27:58.8244151Z 	updating dependency infos of assaultcube-1.3.0.2
2025-06-14T19:27:58.8244425Z 	updating dependency infos of assimp-6.0.1
2025-06-14T19:27:58.8244713Z 	updating dependency infos of assimp_docs-5.3.0
2025-06-14T19:27:58.8244996Z 	updating dependency infos of astroid-2.15.5
2025-06-14T19:27:58.8245271Z 	updating dependency infos of astromenace-1.4.3
2025-06-14T19:27:58.8245538Z 	updating dependency infos of asttokens-2.2.1
2025-06-14T19:27:58.8245804Z 	updating dependency infos of astyle-3.4.8
2025-06-14T19:27:58.8246057Z 	updating dependency infos of asylum-0.3.2
2025-06-14T19:27:58.8246318Z 	updating dependency infos of asymptote-3.04
2025-06-14T19:27:58.8246593Z 	updating dependency infos of async_timeout-4.0.2
2025-06-14T19:27:58.8246864Z 	updating dependency infos of at-3.2.5
2025-06-14T19:27:58.8247117Z 	updating dependency infos of atari++-1.81
2025-06-14T19:27:58.8247478Z 	updating dependency infos of atari800_libretro-3.1.0_20241031
2025-06-14T19:27:58.8247783Z 	updating dependency infos of atf-0.21
2025-06-14T19:27:58.8248037Z 	updating dependency infos of atftp-0.8.0
2025-06-14T19:27:58.8248291Z 	updating dependency infos of atk-2.38.0
2025-06-14T19:27:58.8248543Z 	updating dependency infos of atkmm-2.28.2
2025-06-14T19:27:58.8248841Z 	atlas-3.10.3 is still marked as untested on target architecture
2025-06-14T19:27:58.8249156Z 	updating dependency infos of atool-0.39.0
2025-06-14T19:27:58.8249409Z 	updating dependency infos of attica-5.115.0
2025-06-14T19:27:58.8249669Z 	updating dependency infos of attica6-6.13.0
2025-06-14T19:27:58.8249920Z 	updating dependency infos of attr-2.5.1
2025-06-14T19:27:58.8250161Z 	updating dependency infos of attrs-22.1.0
2025-06-14T19:27:58.8250422Z 	updating dependency infos of audacious-4.4.2
2025-06-14T19:27:58.8250819Z 	updating dependency infos of audacious_plugins-4.4.2
2025-06-14T19:27:58.8251373Z 	updating dependency infos of audacity-3.7.1
2025-06-14T19:27:58.8251783Z 	updating dependency infos of audiofile-0.3.6
2025-06-14T19:27:58.8252060Z 	recipe for auralillusion-4.0 is still broken:
2025-06-14T19:27:58.8252428Z 	Error: package auralillusion-4.0 cannot be built for architecture x86_64
2025-06-14T19:27:58.8253078Z 	updating dependency infos of autoconf-2.72
2025-06-14T19:27:58.8253581Z 	updating dependency infos of autoconf2.71-2.71
2025-06-14T19:27:58.8254094Z 	updating dependency infos of autoconf213-2.13
2025-06-14T19:27:58.8254594Z 	updating dependency infos of autoconf264-2.64
2025-06-14T19:27:58.8255064Z 	updating dependency infos of autoconf269-2.69
2025-06-14T19:27:58.8255610Z 	updating dependency infos of autoconf_archive-2024.10.16
2025-06-14T19:27:58.8256146Z 	updating dependency infos of automake-1.16.5
2025-06-14T19:27:58.8256640Z 	updating dependency infos of automake113-1.13.1
2025-06-14T19:27:58.8257151Z 	updating dependency infos of autosp-2023_10_07
2025-06-14T19:27:58.8257674Z 	updating dependency infos of autotrace-0.40.0_20230301
2025-06-14T19:27:58.8258229Z 	updating dependency infos of autovivification-0.18
2025-06-14T19:27:58.8258799Z 	avahi-0.8 is still marked as untested on target architecture
2025-06-14T19:27:58.8259340Z 	updating dependency infos of avidemux-2.8.1
2025-06-14T19:27:58.8259820Z 	updating dependency infos of avisynthplus-3.7.5
2025-06-14T19:27:58.8260327Z 	updating dependency infos of avr_binutils-2.40
2025-06-14T19:27:58.8260798Z 	updating dependency infos of avr_gcc-13.1.0
2025-06-14T19:27:58.8261452Z 	updating dependency infos of avr_libc-2.1.0
2025-06-14T19:27:58.8261903Z 	updating dependency infos of avra-1.4.2
2025-06-14T19:27:58.8262340Z 	updating dependency infos of avrdude-7.0
2025-06-14T19:27:58.8262790Z 	updating dependency infos of axel-2.17.11
2025-06-14T19:27:58.8263283Z 	updating dependency infos of ayat_recit_ghamadi-0.0.1
2025-06-14T19:27:58.8263844Z 	updating dependency infos of ayat_tafasir_data-0.0.1
2025-06-14T19:27:58.8264644Z 	updating dependency infos of ayat_tarajem_data-0.0.1
2025-06-14T19:27:58.8265193Z 	updating dependency infos of azpainter-3.0.4
2025-06-14T19:27:58.8265680Z 	updating dependency infos of b43_fwcutter-019
2025-06-14T19:27:58.8266136Z 	updating dependency infos of b612-1.008
2025-06-14T19:27:58.8266575Z 	updating dependency infos of b_cow-0.007
2025-06-14T19:27:58.8267065Z 	updating dependency infos of b_hooks_endofscope-0.28
2025-06-14T19:27:58.8267569Z 	updating dependency infos of babel-2.12.1
2025-06-14T19:27:58.8268010Z 	updating dependency infos of babl-0.1.112
2025-06-14T19:27:58.8268461Z 	updating dependency infos of babybe-2.2~git
2025-06-14T19:27:58.8269069Z 	backup-0.0.1 is still marked as broken on target architecture
2025-06-14T19:27:58.8269610Z 	updating dependency infos of bacon-5.0.1
2025-06-14T19:27:58.8270048Z 	updating dependency infos of bafx-0.2.3
2025-06-14T19:27:58.8270600Z 	ballsmacker-1.0.0 is still marked as untested on target architecture
2025-06-14T19:27:58.8271345Z 	updating dependency infos of baloo-5.115.0
2025-06-14T19:27:58.8271789Z 	updating dependency infos of baloo6-6.13.0
2025-06-14T19:27:58.8272288Z 	updating dependency infos of baloo_widgets_kf6-25.04.0
2025-06-14T19:27:58.8272809Z 	updating dependency infos of balsa-2.6.4
2025-06-14T19:27:58.8273269Z 	updating dependency infos of bam-0.5.1
2025-06-14T19:27:58.8273911Z 	bamkeys-1.0.0 is still marked as broken on target architecture
2025-06-14T19:27:58.8274564Z 	barrage-1.0.5 is still marked as untested on target architecture
2025-06-14T19:27:58.8275180Z 	updating dependency infos of barrier_haiku-1.0~git
2025-06-14T19:27:58.8275675Z 	updating dependency infos of bash-5.2.037
2025-06-14T19:27:58.8276182Z 	updating dependency infos of bash_completion-2.14.0
2025-06-14T19:27:58.8276691Z 	recipe for basiliskii-1.0.0 is still broken:
2025-06-14T19:27:58.8277292Z 	Error: package basiliskii-1.0.0 cannot be built for architecture x86_64
2025-06-14T19:27:58.8278371Z 	recipe for basiliskii-0.9.1 is still broken:
2025-06-14T19:27:58.8279007Z 	Error: package basiliskii-0.9.1 cannot be built for architecture x86_64
2025-06-14T19:27:58.8279634Z 	updating dependency infos of bat-0.12.1
2025-06-14T19:27:58.8280109Z 	updating dependency infos of batchrename-0.2.0
2025-06-14T19:27:58.8280646Z 	updating dependency infos of bc-1.07.1
2025-06-14T19:27:58.8281267Z 	updating dependency infos of bchunk-1.2.2
2025-06-14T19:27:58.8281746Z 	updating dependency infos of bcrypt-3.2.0
2025-06-14T19:27:58.8282193Z 	updating dependency infos of bcunit-3.0.2
2025-06-14T19:27:58.8282642Z 	updating dependency infos of bdhcalc-1.1
2025-06-14T19:27:58.8283150Z 	updating dependency infos of bdirectconnect-0.5.0~git
2025-06-14T19:27:58.8283673Z 	updating dependency infos of be_book-2008_10_26
2025-06-14T19:27:58.8284277Z 	beaccessible-1.0.0 is still marked as broken on target architecture
2025-06-14T19:27:58.8284933Z 	beacon-27 is still marked as untested on target architecture
2025-06-14T19:27:58.8285470Z 	updating dependency infos of beae-1.2
2025-06-14T19:27:58.8285911Z 	updating dependency infos of beam-1.2.2
2025-06-14T19:27:58.8286347Z 	updating dependency infos of bear-3.1.5
2025-06-14T19:27:58.8286828Z 	updating dependency infos of beautifulsoup4-4.12.3
2025-06-14T19:27:58.8287338Z 	updating dependency infos of bebattle-1.0.0
2025-06-14T19:27:58.8287821Z 	updating dependency infos of bebuilder-0.5.2~git
2025-06-14T19:27:58.8288303Z 	updating dependency infos of becasso-2.0
2025-06-14T19:27:58.8288786Z 	updating dependency infos of becheckers-1.0.1
2025-06-14T19:27:58.8289257Z 	updating dependency infos of becjk-1.0.1
2025-06-14T19:27:58.8289724Z 	updating dependency infos of beecrypt-4.2.1
2025-06-14T19:27:58.8290180Z 	updating dependency infos of beezer-0.99
2025-06-14T19:27:58.8290643Z 	updating dependency infos of befar-4.2_beta
2025-06-14T19:27:58.8291505Z 	beget-1.2.3 is still marked as broken on target architecture
2025-06-14T19:27:58.8292203Z 	behappy-1.06e~git is still marked as untested on target architecture
2025-06-14T19:27:58.8293035Z 	updating dependency infos of beindexed-0.2.0_alpha
2025-06-14T19:27:58.8293551Z 	recipe for belife-1.0.0 is still broken:
2025-06-14T19:27:58.8294136Z 	Error: package belife-1.0.0 cannot be built for architecture x86_64
2025-06-14T19:27:58.8294727Z 	updating dependency infos of bemines-1.2
2025-06-14T19:27:58.8295276Z 	bemobile-0.9 is still marked as broken on target architecture
2025-06-14T19:27:58.8295844Z 	updating dependency infos of benchmark-1.6.1
2025-06-14T19:27:58.8296365Z 	updating dependency infos of bencode_tools-20110315
2025-06-14T19:27:58.8296882Z 	updating dependency infos of benettris-0.2
2025-06-14T19:27:58.8297438Z 	benormal-1.0 is still marked as untested on target architecture
2025-06-14T19:27:58.8297935Z 	updating dependency infos of beohms-0.1~git
2025-06-14T19:27:58.8298215Z 	recipe for beostilink-0~git is still broken:
2025-06-14T19:27:58.8298566Z 	Error: package beostilink-0~git cannot be built for architecture x86_64
2025-06-14T19:27:58.8298930Z 	updating dependency infos of bepdf-2.1.4
2025-06-14T19:27:58.8299196Z 	recipe for bephonebook-1.2 is still broken:
2025-06-14T19:28:00.9272023Z 	Error: No match found for license Unknown
2025-06-14T19:28:00.9272610Z 	Error: Valid license filenames included with Haiku are:
2025-06-14T19:28:00.9275232Z 	Error: Anti-Grain Geometry, Apache v2, Artistic, Artistic v2.0, BSD (2-clause), BSD (3-clause), BSD (4-clause), Be Sample Code License, Bullet, CDDL v1, CQuantizer, DEC, GLUT (Mark Kilgard), GNU GPL font exception, GNU GPL v1, GNU GPL v2, GNU GPL v3, GNU LGPL v2, GNU LGPL v2.1, GNU LGPL v3, GPC, Intel (2xxx firmware), Intel (ACPICA), Intel (firmware), LibHTTPd, LibJPEG, LibPNG, MAPM, MIT, MIT (no promotion), MPL v1.1, MPL v2.0, Marvell (firmware), OpenGroup, PDFlib Lite, Public Domain, Ralink (firmware), SGI Free B, SIL Open Font License v1.1, Zlib
2025-06-14T19:28:00.9277476Z 	Error: (in /runner/work/haikuports/haikuports/haiku-apps/bephonebook/bephonebook-1.2.recipe)
2025-06-14T19:28:00.9278289Z 	bephotomagic-0.62_git is still marked as untested on target architecture
2025-06-14T19:28:00.9278672Z 	updating dependency infos of bepodder-1.5.0
2025-06-14T19:28:00.9278992Z 	berdp-1 is still marked as untested on target architecture
2025-06-14T19:28:00.9279321Z 	updating dependency infos of bescreencapture-2.9.9
2025-06-14T19:28:00.9279611Z 	updating dependency infos of beshare-3.04
2025-06-14T19:28:00.9296822Z 	besol-2.0.5 is still marked as untested on target architecture
2025-06-14T19:28:00.9297398Z 	updating dependency infos of bespider-0.1.1
2025-06-14T19:28:00.9297845Z 	updating dependency infos of betex-20220223
2025-06-14T19:28:00.9298166Z 	updating dependency infos of betterspades-0.1.6~git
2025-06-14T19:28:00.9298580Z 	updating dependency infos of bevexed-20141224
2025-06-14T19:28:00.9298939Z 	bezilla-2.0.0.22 is still marked as untested on target architecture
2025-06-14T19:28:00.9299286Z 	updating dependency infos of bghostview-1.0.0
2025-06-14T19:28:00.9299581Z 	updating dependency infos of bgswitch-0.1.0
2025-06-14T19:28:00.9299835Z 	updating dependency infos of biber-2.20
2025-06-14T19:28:00.9300144Z 	bic-1.0~git is still marked as broken on target architecture
2025-06-14T19:28:00.9300461Z 	updating dependency infos of billardgl-1.75
2025-06-14T19:28:00.9300726Z 	updating dependency infos of bin86-0.16.21
2025-06-14T19:28:00.9301059Z 	binaryclock-20141223 is still marked as broken on target architecture
2025-06-14T19:28:00.9301723Z 	updating dependency infos of bind_utils-9.16.50
2025-06-14T19:28:00.9302005Z 	updating dependency infos of biniax2-1.30
2025-06-14T19:28:00.9302265Z 	updating dependency infos of binutils-2.42
2025-06-14T19:28:00.9302524Z 	updating dependency infos of binwalk-2.4.0
2025-06-14T19:28:00.9302775Z 	updating dependency infos of bison-3.8.2
2025-06-14T19:28:00.9303030Z 	updating dependency infos of bitchx-1.2.1
2025-06-14T19:28:00.9303278Z 	updating dependency infos of bitlbee-3.5.1
2025-06-14T19:28:00.9303560Z 	updating dependency infos of bk_libretro-1.0_20241021
2025-06-14T19:28:00.9303848Z 	updating dependency infos of blake3-1.4.1
2025-06-14T19:28:00.9304346Z 	updating dependency infos of blastem_libretro-0.6.3_20220726
2025-06-14T19:28:00.9304711Z 	updating dependency infos of blaze-3.8.2
2025-06-14T19:28:00.9305017Z 	blender-2.79b is still marked as untested on target architecture
2025-06-14T19:28:00.9305344Z 	updating dependency infos of blender3-3.3.21
2025-06-14T19:28:00.9305610Z 	updating dependency infos of blinken-25.04.0
2025-06-14T19:28:00.9305861Z 	updating dependency infos of blis-0.9.0
2025-06-14T19:28:00.9306112Z 	updating dependency infos of blis8-0.8.0
2025-06-14T19:28:00.9306382Z 	updating dependency infos of blobbyvolley2-1.1~git
2025-06-14T19:28:00.9306718Z 	blobwars-2.00 is still marked as untested on target architecture
2025-06-14T19:28:00.9307026Z 	updating dependency infos of blobwars-1.19
2025-06-14T19:28:00.9307284Z 	updating dependency infos of blockout2-2.5
2025-06-14T19:28:00.9307556Z 	updating dependency infos of blogpositive-0.4.0
2025-06-14T19:28:00.9307836Z 	updating dependency infos of bluefish-2.2.16
2025-06-14T19:28:00.9308147Z 	updating dependency infos of bluemsx_libretro-2.9.0_20250416
2025-06-14T19:28:00.9308507Z 	bluez_qt6-6.13.0 is still marked as untested on target architecture
2025-06-14T19:28:00.9308826Z 	updating dependency infos of bmake-20230723
2025-06-14T19:28:00.9309076Z 	updating dependency infos of boca-1.0.7
2025-06-14T19:28:00.9309327Z 	updating dependency infos of bochs-2.6.11
2025-06-14T19:28:00.9309579Z 	updating dependency infos of boehm_gc-8.2.8
2025-06-14T19:28:00.9309836Z 	updating dependency infos of bomber-25.04.0
2025-06-14T19:28:00.9310087Z 	updating dependency infos of bong-1.4~git
2025-06-14T19:28:00.9310344Z 	updating dependency infos of bonnie++-2.00a
2025-06-14T19:28:00.9310639Z 	updating dependency infos of bookmarkconverter-0.4.3
2025-06-14T19:28:00.9310927Z 	updating dependency infos of booksorg-0.3
2025-06-14T19:28:00.9311485Z 	updating dependency infos of boost1.83-1.83.0
2025-06-14T19:28:00.9311907Z 	updating dependency infos of boost1.85-1.85.0
2025-06-14T19:28:00.9312179Z 	updating dependency infos of boost1.87-1.87.0
2025-06-14T19:28:00.9312438Z 	updating dependency infos of boost1.88-1.88.0
2025-06-14T19:28:00.9312705Z 	updating dependency infos of boost169-1.69.0
2025-06-14T19:28:00.9312972Z 	updating dependency infos of boost170-1.70.0
2025-06-14T19:28:00.9313241Z 	updating dependency infos of boost_build-1.70.0
2025-06-14T19:28:00.9313521Z 	updating dependency infos of borgbackup-1.4.0
2025-06-14T19:28:00.9313779Z 	updating dependency infos of boswars-2.8
2025-06-14T19:28:00.9314032Z 	updating dependency infos of botan-2.19.4
2025-06-14T19:28:00.9314281Z 	updating dependency infos of botan3-3.8.1
2025-06-14T19:28:00.9314538Z 	updating dependency infos of bottle-0.12.25
2025-06-14T19:28:00.9314790Z 	updating dependency infos of bovo-25.04.0
2025-06-14T19:28:00.9315038Z 	updating dependency infos of box2d-2.4.1
2025-06-14T19:28:00.9315305Z 	updating dependency infos of boxedwine-21.0.1
2025-06-14T19:28:00.9315628Z 	brainwash-1.0.0 is still marked as broken on target architecture
2025-06-14T19:28:00.9315956Z 	updating dependency infos of breathe-4.35.0
2025-06-14T19:28:00.9316231Z 	updating dependency infos of breeze_icons-6.13.0
2025-06-14T19:28:00.9316505Z 	updating dependency infos of brexx-1.3.2
2025-06-14T19:28:00.9316752Z 	updating dependency infos of brie-0.4
2025-06-14T19:28:00.9317003Z 	updating dependency infos of brotli-1.1.0
2025-06-14T19:28:00.9317250Z 	recipe for bs2b-2.1.0 is still broken:
2025-06-14T19:28:00.9317563Z 	Error: package bs2b-2.1.0 cannot be built for architecture x86_64
2025-06-14T19:28:00.9317903Z 	updating dependency infos of bsap-0.8
2025-06-14T19:28:00.9318200Z 	bshisen-1.2 is still marked as broken on target architecture
2025-06-14T19:28:00.9318559Z 	updating dependency infos of bsnes_libretro-115.1_20241029
2025-06-14T19:28:00.9318863Z 	updating dependency infos of bsnow-1.0.0
2025-06-14T19:28:00.9319131Z 	updating dependency infos of btanks-0.9.8083
2025-06-14T19:28:00.9319404Z 	updating dependency infos of bugdom-1.3.4
2025-06-14T19:28:00.9319765Z 	updating dependency infos of build-1.2.2
2025-06-14T19:28:00.9320082Z 	buildcpr-2014 is still marked as untested on target architecture
2025-06-14T19:28:00.9320397Z 	updating dependency infos of bullet-3.17
2025-06-14T19:28:00.9320720Z 	bumprace-1.5.6 is still marked as untested on target architecture
2025-06-14T19:28:00.9321055Z 	updating dependency infos of burgerspace-1.9.4
2025-06-14T19:28:00.9321567Z 	updating dependency infos of burnitnow-1.2.1
2025-06-14T19:28:00.9321833Z 	updating dependency infos of burp-3.1.4
2025-06-14T19:28:00.9322106Z 	updating dependency infos of business_isbn-3.011
2025-06-14T19:28:00.9322435Z 	updating dependency infos of business_isbn_data-20241224.001
2025-06-14T19:28:00.9322758Z 	updating dependency infos of business_ismn-1.204
2025-06-14T19:28:00.9323041Z 	updating dependency infos of business_issn-1.007
2025-06-14T19:28:00.9323312Z 	updating dependency infos of butterfly-1.6.2
2025-06-14T19:28:00.9323585Z 	updating dependency infos of byacc-20230219
2025-06-14T19:28:00.9323844Z 	updating dependency infos of bzflag-2.4.26
2025-06-14T19:28:00.9324103Z 	updating dependency infos of bzip2-1.0.8
2025-06-14T19:28:00.9324354Z 	updating dependency infos of bzip3-1.5.1
2025-06-14T19:28:00.9324603Z 	updating dependency infos of c_ares-1.19.1
2025-06-14T19:28:00.9324862Z 	updating dependency infos of c_blosc-1.18.1
2025-06-14T19:28:00.9325171Z 	updating dependency infos of ca_root_certificates-2024_11_26
2025-06-14T19:28:00.9325555Z 	updating dependency infos of ca_root_certificates_java-2024_11_26
2025-06-14T19:28:00.9325934Z 	cabal-3.2.1.0 is still marked as broken on target architecture
2025-06-14T19:28:00.9326261Z 	updating dependency infos of cabextract-1.11
2025-06-14T19:28:00.9326521Z 	updating dependency infos of cadaver-0.26
2025-06-14T19:28:00.9326775Z 	updating dependency infos of caffe-1.0
2025-06-14T19:28:00.9327026Z 	updating dependency infos of cairo-1.16.0
2025-06-14T19:28:00.9327409Z 	updating dependency infos of cairo1.18-1.18.0
2025-06-14T19:28:00.9327680Z 	updating dependency infos of cairomm-1.13.1
2025-06-14T19:28:00.9327929Z 	updating dependency infos of cal-4.1
2025-06-14T19:28:00.9328171Z 	updating dependency infos of cal3d-0.120
2025-06-14T19:28:00.9328426Z 	updating dependency infos of caladea-20130214
2025-06-14T19:28:00.9328690Z 	updating dependency infos of calc-2.12.7.2
2025-06-14T19:28:00.9328944Z 	updating dependency infos of calcurse-4.8.0
2025-06-14T19:28:00.9329203Z 	updating dependency infos of calendar-0.1
2025-06-14T19:28:00.9329594Z 	updating dependency infos of calendarsupport-23.08.5
2025-06-14T19:28:00.9329945Z 	updating dependency infos of calibre-5.32.0
2025-06-14T19:28:00.9330208Z 	updating dependency infos of caligula-1.0
2025-06-14T19:28:00.9330459Z 	updating dependency infos of calligra-3.2.1
2025-06-14T19:28:00.9330732Z 	updating dependency infos of calligraplan-3.3.0
2025-06-14T19:28:00.9331050Z 	camlp5-7.05 is still marked as untested on target architecture
2025-06-14T19:28:00.9331600Z 	camlp5-6.12 is still marked as untested on target architecture
2025-06-14T19:28:00.9331914Z 	updating dependency infos of canna-1.0.3~git
2025-06-14T19:28:00.9332230Z 	updating dependency infos of cannonball_libretro-0.34_20241021
2025-06-14T19:28:00.9332568Z 	updating dependency infos of cantarell-0.303.1
2025-06-14T19:28:00.9332839Z 	updating dependency infos of cantata-2.5.0
2025-06-14T19:28:00.9333099Z 	updating dependency infos of cantor-25.04.0
2025-06-14T19:28:00.9333396Z 	updating dependency infos of cap32_libretro-4.2.0_20250208
2025-06-14T19:28:00.9333708Z 	updating dependency infos of capitalbe-2.3.1
2025-06-14T19:28:00.9333974Z 	updating dependency infos of capnproto-1.1.0
2025-06-14T19:28:00.9334239Z 	updating dependency infos of capstone-4.0.2
2025-06-14T19:28:00.9334499Z 	updating dependency infos of capstone5-5.0.1
2025-06-14T19:28:00.9334764Z 	updating dependency infos of capture_tiny-0.48
2025-06-14T19:28:00.9335033Z 	updating dependency infos of cardo-1.04
2025-06-14T19:28:00.9335284Z 	updating dependency infos of cargo_c-0.10.7
2025-06-14T19:28:00.9335683Z 	updating dependency infos of carlito-20130920
2025-06-14T19:28:00.9335968Z 	updating dependency infos of cascadia_code-2106.17
2025-06-14T19:28:00.9336247Z 	updating dependency infos of catch2-3.4.0
2025-06-14T19:28:00.9336534Z 	updating dependency infos of catchchallenger-3.0.0.0
2025-06-14T19:28:00.9336815Z 	updating dependency infos of catdoc-0.95
2025-06-14T19:28:00.9337085Z 	updating dependency infos of catkeyseditor-0.1.2
2025-06-14T19:28:00.9337367Z 	updating dependency infos of caveexpress-2.5.2
2025-06-14T19:28:00.9337643Z 	updating dependency infos of cavepacker-2.5.2
2025-06-14T19:28:00.9337945Z 	caya-0.0.3 is still marked as broken on target architecture
2025-06-14T19:28:00.9338248Z 	updating dependency infos of cbindgen-0.28.0
2025-06-14T19:28:00.9338636Z 	updating dependency infos of cblas_reference-20110120
2025-06-14T19:28:00.9338975Z 	updating dependency infos of ccache-4.11.2
2025-06-14T19:28:00.9339242Z 	updating dependency infos of ccatch-5.0.0
2025-06-14T19:28:00.9339500Z 	updating dependency infos of ccd2iso-0.3
2025-06-14T19:28:00.9339766Z 	updating dependency infos of ccextractor-0.88
2025-06-14T19:28:00.9340024Z 	updating dependency infos of ccfits-2.5
2025-06-14T19:28:00.9340331Z 	ccleste-1.4.0 is still marked as untested on target architecture
2025-06-14T19:28:00.9340648Z 	updating dependency infos of ccls-0.20241108
2025-06-14T19:28:00.9340918Z 	updating dependency infos of cctv_viewer-0.1.9
2025-06-14T19:28:03.0846071Z 	updating dependency infos of cd-5.12
2025-06-14T19:28:03.0846627Z 	updating dependency infos of cdogs_sdl-1.4.1
2025-06-14T19:28:03.0846988Z 	updating dependency infos of cdplayer-1.0
2025-06-14T19:28:03.0847299Z 	updating dependency infos of cdrtools-3.02~a09
2025-06-14T19:28:03.0847576Z 	updating dependency infos of cegui-0.8.7
2025-06-14T19:28:03.0847847Z 	updating dependency infos of celestia-1.6.3
2025-06-14T19:28:03.0848373Z 	updating dependency infos of cereal-1.3.0
2025-06-14T19:28:03.0848669Z 	updating dependency infos of ceres_solver-2.0.1~git
2025-06-14T19:28:03.0848976Z 	updating dependency infos of certifi-2023.7.22
2025-06-14T19:28:03.0849235Z 	updating dependency infos of cffi-1.15.1
2025-06-14T19:28:03.0849493Z 	updating dependency infos of cfitsio-4.4.0
2025-06-14T19:28:03.0849745Z 	updating dependency infos of cfitsio3-3.49
2025-06-14T19:28:03.0849990Z 	updating dependency infos of cgal-4.13
2025-06-14T19:28:03.0850229Z 	updating dependency infos of cglm-0.8.5
2025-06-14T19:28:03.0850476Z 	updating dependency infos of chafa-1.14.4
2025-06-14T19:28:03.0850725Z 	updating dependency infos of chardet-4.0.0
2025-06-14T19:28:03.0851001Z 	updating dependency infos of charset_normalizer-2.1.1
2025-06-14T19:28:03.0851693Z 	updating dependency infos of chat_o_matic-0.0.3~git
2025-06-14T19:28:03.0851978Z 	updating dependency infos of check-0.15.2
2025-06-14T19:28:03.0852319Z 	cherry_blossom-1.0 is still marked as untested on target architecture
2025-06-14T19:28:03.0852660Z 	updating dependency infos of chessx-1.5.0
2025-06-14T19:28:03.0852922Z 	updating dependency infos of chexquest-1.0
2025-06-14T19:28:03.0853191Z 	updating dependency infos of chexquest3-1.4
2025-06-14T19:28:03.0853446Z 	updating dependency infos of chicken-5.4.0
2025-06-14T19:28:03.0853699Z 	updating dependency infos of chktex-1.7.9
2025-06-14T19:28:03.0853943Z 	updating dependency infos of chmlib-0.40
2025-06-14T19:28:03.0854217Z 	updating dependency infos of chocolate_doom-3.1.0
2025-06-14T19:28:03.0854506Z 	updating dependency infos of chromaprint-1.5.1
2025-06-14T19:28:03.0854773Z 	updating dependency infos of chrpath-0.16
2025-06-14T19:28:03.0855031Z 	updating dependency infos of cine_encoder-3.5.1
2025-06-14T19:28:03.0855314Z 	updating dependency infos of circuslinux-1.0.3
2025-06-14T19:28:03.0855597Z 	updating dependency infos of cjk_utils-4.8.5
2025-06-14T19:28:03.0855855Z 	updating dependency infos of cjson-1.7.18
2025-06-14T19:28:03.0856105Z 	updating dependency infos of clamav-1.4.2
2025-06-14T19:28:03.0856377Z 	updating dependency infos of clamav_gui-1.0.9
2025-06-14T19:28:03.0856804Z 	updating dependency infos of class_accessor-0.51
2025-06-14T19:28:03.0857130Z 	updating dependency infos of class_data_inheritable-0.09
2025-06-14T19:28:03.0857446Z 	updating dependency infos of class_inspector-1.36
2025-06-14T19:28:03.0857853Z 	updating dependency infos of class_singleton-1.6
2025-06-14T19:28:03.0858231Z 	updating dependency infos of class_tiny-1.008
2025-06-14T19:28:03.0858518Z 	updating dependency infos of class_xsaccessor-1.19
2025-06-14T19:28:03.0858797Z 	updating dependency infos of classicube-1.3.7
2025-06-14T19:28:03.0859066Z 	updating dependency infos of claws_mail-4.3.1
2025-06-14T19:28:03.0859321Z 	updating dependency infos of clazy-1.14
2025-06-14T19:28:03.0859577Z 	updating dependency infos of clear_sans-1.00
2025-06-14T19:28:03.0859854Z 	updating dependency infos of clementine-1.4.1~git
2025-06-14T19:28:03.0860124Z 	updating dependency infos of click-8.1.3
2025-06-14T19:28:03.0860395Z 	updating dependency infos of clipboard-0.10.0
2025-06-14T19:28:03.0860660Z 	updating dependency infos of clipdinger-1.2.4
2025-06-14T19:28:03.0860927Z 	updating dependency infos of clipper2-1.5.2
2025-06-14T19:28:03.0861419Z 	updating dependency infos of clips-6.30
2025-06-14T19:28:03.0861687Z 	recipe for clipup-2.0.3 is still broken:
2025-06-14T19:28:03.0862016Z 	Error: package clipup-2.0.3 cannot be built for architecture x86_64
2025-06-14T19:28:03.0862359Z 	updating dependency infos of clisp-2.49.95~git
2025-06-14T19:28:03.0862632Z 	updating dependency infos of cln-1.3.6
2025-06-14T19:28:03.0862894Z 	updating dependency infos of clockwerk-1.0~git
2025-06-14T19:28:03.0863165Z 	updating dependency infos of clone-0.47
2025-06-14T19:28:03.0863416Z 	updating dependency infos of cloud_init-1.1
2025-06-14T19:28:03.0863679Z 	updating dependency infos of clucene-2.3.3.4
2025-06-14T19:28:03.0863941Z 	updating dependency infos of cmake-3.31.5
2025-06-14T19:28:03.0864341Z 	updating dependency infos of cmake_gui-3.31.5
2025-06-14T19:28:03.0864675Z 	cmake_haiku-git is still marked as untested on target architecture
2025-06-14T19:28:03.0865000Z 	updating dependency infos of cmark-0.29.0
2025-06-14T19:28:03.0865254Z 	updating dependency infos of cmocka-1.1.5
2025-06-14T19:28:03.0865496Z 	updating dependency infos of cmus-2.10.0
2025-06-14T19:28:03.0865819Z 	codeblocks-20.03 is still marked as untested on target architecture
2025-06-14T19:28:03.0866146Z 	updating dependency infos of codecrypt-1.8
2025-06-14T19:28:03.0866398Z 	updating dependency infos of coeurl-0.3.1
2025-06-14T19:28:03.0866646Z 	updating dependency infos of coin-4.0.0
2025-06-14T19:28:03.0866891Z 	updating dependency infos of colm-0.13.0.5
2025-06-14T19:28:03.0867144Z 	updating dependency infos of colobot-0.2.2
2025-06-14T19:28:03.0867454Z 	updating dependency infos of colobot_data-0.2.2
2025-06-14T19:28:03.0867977Z 	updating dependency infos of color_lines-0.6
2025-06-14T19:28:03.0868492Z 	updating dependency infos of colorcode-0.8.5
2025-06-14T19:28:03.0868907Z 	updating dependency infos of colordiff-1.0.19
2025-06-14T19:28:03.0869205Z 	updating dependency infos of colormake-0.9.20140503
2025-06-14T19:28:03.0869482Z 	updating dependency infos of colors-2.3
2025-06-14T19:28:03.0869739Z 	updating dependency infos of comic_neue-2.4
2025-06-14T19:28:03.0870035Z 	updating dependency infos of command_not_found-0.0.1~git
2025-06-14T19:28:03.0870360Z 	updating dependency infos of commandergenius-3.5.2
2025-06-14T19:28:03.0870652Z 	updating dependency infos of commandtimer-0.3.1
2025-06-14T19:28:03.0870941Z 	updating dependency infos of compress_bzip2-2.28
2025-06-14T19:28:03.0871615Z 	updating dependency infos of confclerk-0.7.2
2025-06-14T19:28:03.0871913Z 	updating dependency infos of config_autoconf-0.320
2025-06-14T19:28:03.0872195Z 	updating dependency infos of confuse-3.3
2025-06-14T19:28:03.0872446Z 	updating dependency infos of conky-1.19.6
2025-06-14T19:28:03.0872708Z 	updating dependency infos of connect4-1.0.0
2025-06-14T19:28:03.0873031Z 	updating dependency infos of connectagram-1.3.5
2025-06-14T19:28:03.0873469Z 	updating dependency infos of contourpy-1.1.0
2025-06-14T19:28:03.0873813Z 	converttolf-0.0.0 is still marked as untested on target architecture
2025-06-14T19:28:03.0874141Z 	updating dependency infos of convmv-2.05
2025-06-14T19:28:03.0874437Z 	conway-0.9 is still marked as broken on target architecture
2025-06-14T19:28:03.0874756Z 	updating dependency infos of coolreader3-3.2.2.5m
2025-06-14T19:28:03.0875084Z 	updating dependency infos of copynametoclipboard-1.0.1
2025-06-14T19:28:03.0875390Z 	updating dependency infos of coreutils-9.6
2025-06-14T19:28:03.0875649Z 	updating dependency infos of corrosion-0.4.4
2025-06-14T19:28:03.0875920Z 	updating dependency infos of corsix_th-0.68.0
2025-06-14T19:28:03.0876196Z 	updating dependency infos of courier_prime-1.203
2025-06-14T19:28:03.0876480Z 	updating dependency infos of coverage-7.6.10
2025-06-14T19:28:03.0876753Z 	recipe for coveredcalc-1.10.0 is still broken:
2025-06-14T19:28:03.0877116Z 	Error: package coveredcalc-1.10.0 cannot be built for architecture x86_64
2025-06-14T19:28:03.0877479Z 	updating dependency infos of cowsay-3.04
2025-06-14T19:28:03.0877757Z 	updating dependency infos of cpan_meta_check-0.018
2025-06-14T19:28:03.0878045Z 	updating dependency infos of cpctools-0.3.3
2025-06-14T19:28:03.0878299Z 	updating dependency infos of cpio-2.14
2025-06-14T19:28:03.0878571Z 	updating dependency infos of cppcheck-2.17.1
2025-06-14T19:28:03.0878839Z 	updating dependency infos of cppdap-1.58.0
2025-06-14T19:28:03.0879105Z 	updating dependency infos of cppfront-0.8.1
2025-06-14T19:28:03.0879362Z 	updating dependency infos of cppunit-1.14.0
2025-06-14T19:28:03.0879617Z 	updating dependency infos of cppy-1.2.1
2025-06-14T19:28:03.0879869Z 	updating dependency infos of cpuminer-2.5.1
2025-06-14T19:28:03.0880172Z 	updating dependency infos of craft_libretro-1.0_20241006
2025-06-14T19:28:03.0880473Z 	updating dependency infos of cram-0.7
2025-06-14T19:28:03.0880835Z 	updating dependency infos of crawl-0.29.0
2025-06-14T19:28:03.0881361Z 	cream-0.43 is still marked as broken on target architecture
2025-06-14T19:28:03.0881759Z 	crimson-0.5.3 is still marked as untested on target architecture
2025-06-14T19:28:03.0882095Z 	updating dependency infos of criticalmass-2.2
2025-06-14T19:28:03.0882380Z 	updating dependency infos of cro_mag_rally-3.0.1
2025-06-14T19:28:03.0882663Z 	updating dependency infos of cronie-1.7.2
2025-06-14T19:28:03.0882942Z 	updating dependency infos of croscorefonts-1.31.0
2025-06-14T19:28:03.0883225Z 	updating dependency infos of crunch-3.6
2025-06-14T19:28:03.0883483Z 	updating dependency infos of crypto++-8.9.0
2025-06-14T19:28:03.0883750Z 	updating dependency infos of cryptography-3.4.8
2025-06-14T19:28:03.0884132Z 	updating dependency infos of cscope-15.9
2025-06-14T19:28:03.0884466Z 	updating dependency infos of cson-0.8
2025-06-14T19:28:03.0884723Z 	updating dependency infos of csound-6.18.1
2025-06-14T19:28:03.0884990Z 	updating dependency infos of css_parser-1.0.9
2025-06-14T19:28:03.0885271Z 	updating dependency infos of cssselect-1.1.0
2025-06-14T19:28:03.0885540Z 	updating dependency infos of ctags-6.1.0
2025-06-14T19:28:03.0885786Z 	updating dependency infos of ctpl-0.3.4
2025-06-14T19:28:03.0886062Z 	updating dependency infos of cube2tesseract-r2553
2025-06-14T19:28:03.0886356Z 	updating dependency infos of cubeb-0.2~git20201209
2025-06-14T19:28:03.0886648Z 	updating dependency infos of cudatext-1.221.0.0
2025-06-14T19:28:03.0886924Z 	updating dependency infos of curaengine-4.8.0
2025-06-14T19:28:03.0887192Z 	updating dependency infos of curl-8.13.0
2025-06-14T19:28:03.0887447Z 	updating dependency infos of curlftpfs-0.9.2
2025-06-14T19:28:03.0887722Z 	updating dependency infos of cutemarked-0.11.3
2025-06-14T19:28:03.0887994Z 	updating dependency infos of cutemaze-1.3.3
2025-06-14T19:28:03.0888244Z 	updating dependency infos of cutter-2.3.4
2025-06-14T19:28:03.0888513Z 	updating dependency infos of cutycapt-1.0_20130715
2025-06-14T19:28:03.0888790Z 	updating dependency infos of cvs-1.12.13.1
2025-06-14T19:28:03.0889172Z 	updating dependency infos of cvsps-2.2b1
2025-06-14T19:28:03.0889429Z 	updating dependency infos of cxxopts-3.2.0
2025-06-14T19:28:03.0889680Z 	updating dependency infos of cycler-0.11.0
2025-06-14T19:28:03.0889988Z 	cylindrix-1.0 is still marked as broken on target architecture
2025-06-14T19:28:03.0890309Z 	updating dependency infos of cyrus_sasl-2.1.28
2025-06-14T19:28:03.0890578Z 	updating dependency infos of cython-3.0.10
2025-06-14T19:28:03.0890818Z 	recipe for d52-3.4.1 is still broken:
2025-06-14T19:28:03.0891302Z 	Error: package d52-3.4.1 cannot be built for architecture x86_64
2025-06-14T19:28:03.0891740Z 	updating dependency infos of daa2iso-0.1.7e
2025-06-14T19:28:03.0892003Z 	updating dependency infos of dash-0.5.12
2025-06-14T19:28:03.0892325Z 	dasmxx-0.1.202108 is still marked as untested on target architecture
2025-06-14T19:28:03.0892671Z 	updating dependency infos of data_compare-1.29
2025-06-14T19:28:03.0892952Z 	updating dependency infos of data_dump-1.25
2025-06-14T19:28:03.0893224Z 	updating dependency infos of data_uniqid-0.12
2025-06-14T19:28:03.0893497Z 	updating dependency infos of datetime-1.65
2025-06-14T19:28:03.0893804Z 	updating dependency infos of datetime_calendar_julian-0.107
2025-06-14T19:28:03.0894157Z 	updating dependency infos of datetime_format_builder-0.83
2025-06-14T19:28:03.0894500Z 	updating dependency infos of datetime_format_strptime-1.79
2025-06-14T19:28:03.0894829Z 	updating dependency infos of datetime_locale-1.43
2025-06-14T19:28:03.0895133Z 	updating dependency infos of datetime_timezone-2.63
2025-06-14T19:28:03.0895416Z 	updating dependency infos of dateutil-2.8.2
2025-06-14T19:28:03.0895674Z 	updating dependency infos of dav1d-1.5.0
2025-06-14T19:28:03.0895930Z 	updating dependency infos of dave_gnukem-1.0
2025-06-14T19:28:03.0896189Z 	updating dependency infos of db18-18.1.40
2025-06-14T19:28:03.0896439Z 	updating dependency infos of dblatex-0.3.12
2025-06-14T19:28:03.0896939Z 	updating dependency infos of dbus-1.12.20
2025-06-14T19:28:03.0897193Z 	updating dependency infos of dbus_glib-0.112
2025-06-14T19:28:03.0897472Z 	updating dependency infos of dbuspython-1.3.2
2025-06-14T19:28:03.0897757Z 	updating dependency infos of dbztool-2025.02.22
2025-06-14T19:28:03.0898025Z 	updating dependency infos of dcadec-0.2.0
2025-06-14T19:28:03.0898282Z 	updating dependency infos of dconf-0.40.0
2025-06-14T19:28:04.1324147Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:04.1337619Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:04.1352135Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:04.1366040Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:04.1380245Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:04.1395132Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.0253077Z 	updating dependency infos of dconf_editor-43.0
2025-06-14T19:28:05.0253670Z 	updating dependency infos of dcraw-9.28.0
2025-06-14T19:28:05.0254104Z 	recipe for dcron-4.5 is still broken:
2025-06-14T19:28:05.0254632Z 	Error: package dcron-4.5 cannot be built for architecture x86_64
2025-06-14T19:28:05.0255176Z 	updating dependency infos of ddgr-1.6
2025-06-14T19:28:05.0255629Z 	updating dependency infos of ddnet-2023.03.12~git
2025-06-14T19:28:05.0256095Z 	updating dependency infos of ddrescue-1.19
2025-06-14T19:28:05.0256441Z 	dead_ascend-1.1.0 is still marked as untested on target architecture
2025-06-14T19:28:05.0256781Z 	updating dependency infos of deark-1.7.0
2025-06-14T19:28:05.0257053Z 	updating dependency infos of deathchase3d-0.9
2025-06-14T19:28:05.0257367Z 	updating dependency infos of debugmonitor-0.1.1~20181227
2025-06-14T19:28:05.0257668Z 	updating dependency infos of decorator-5.1.1
2025-06-14T19:28:05.0257948Z 	updating dependency infos of deeperpeople-1.0.0
2025-06-14T19:28:05.0258250Z 	updating dependency infos of defendguin-0.0.13
2025-06-14T19:28:05.0258725Z 	updating dependency infos of dejagnu-1.6
2025-06-14T19:28:05.0258984Z 	updating dependency infos of dejavu-2.37
2025-06-14T19:28:05.0259237Z 	updating dependency infos of deskbareyes-0.1.1
2025-06-14T19:28:05.0259505Z 	updating dependency infos of desknotes-1.2.1
2025-06-14T19:28:05.0259813Z 	updating dependency infos of desmume_libretro-0.9.11_20241021
2025-06-14T19:28:05.0260147Z 	updating dependency infos of devel_stacktrace-2.05
2025-06-14T19:28:05.0260422Z 	updating dependency infos of devil-1.8.0
2025-06-14T19:28:05.0260684Z 	updating dependency infos of devilutionx-1.5.4
2025-06-14T19:28:05.0260982Z 	updating dependency infos of devilutionx_extras-v4
2025-06-14T19:28:05.0261566Z 	updating dependency infos of dfu_programmer-1.1.0
2025-06-14T19:28:05.0261857Z 	updating dependency infos of dfu_util-0.9
2025-06-14T19:28:05.0262149Z 	dgen-1.33 is still marked as untested on target architecture
2025-06-14T19:28:05.0262460Z 	updating dependency infos of dhewm3-1.5.1
2025-06-14T19:28:05.0262712Z 	updating dependency infos of dht-0.26
2025-06-14T19:28:05.0262954Z 	updating dependency infos of di-4.54
2025-06-14T19:28:05.0263223Z 	updating dependency infos of diablo_shareware-1.09
2025-06-14T19:28:05.0263516Z 	updating dependency infos of dialog-1.3_20240619
2025-06-14T19:28:05.0263804Z 	updating dependency infos of diff_so_fancy-1.4.3
2025-06-14T19:28:05.0264073Z 	updating dependency infos of diffstat-1.64
2025-06-14T19:28:05.0264340Z 	updating dependency infos of diffutils-3.10
2025-06-14T19:28:05.0264597Z 	updating dependency infos of digger-20020314
2025-06-14T19:28:05.0264857Z 	updating dependency infos of digiclock-1.0
2025-06-14T19:28:05.0265106Z 	updating dependency infos of digikam-8.2.0
2025-06-14T19:28:05.0265370Z 	updating dependency infos of dillo_plus-3.2.1
2025-06-14T19:28:05.0265696Z 	direnv-2.14.0 is still marked as untested on target architecture
2025-06-14T19:28:05.0266167Z 	updating dependency infos of discid-1.2.0
2025-06-14T19:28:05.0266435Z 	updating dependency infos of discount-3.0.0d
2025-06-14T19:28:05.0266701Z 	updating dependency infos of diskus-0.6.0
2025-06-14T19:28:05.0267030Z 	updating dependency infos of dist_checkconflicts-0.11
2025-06-14T19:28:05.0267322Z 	updating dependency infos of distcc-3.3.5
2025-06-14T19:28:05.0267566Z 	updating dependency infos of djview-4.12
2025-06-14T19:28:05.0267824Z 	updating dependency infos of djvu-3.5.28
2025-06-14T19:28:05.0268090Z 	updating dependency infos of djvutranslator-1.2.2
2025-06-14T19:28:05.0268387Z 	updating dependency infos of djvuviewer-1.2.2
2025-06-14T19:28:05.0268643Z 	updating dependency infos of dlib-19.21
2025-06-14T19:28:05.0268892Z 	updating dependency infos of dma-0.14~git
2025-06-14T19:28:05.0269138Z 	updating dependency infos of dmd-2.067.1
2025-06-14T19:28:05.0269382Z 	updating dependency infos of dmg2img-1.6.7
2025-06-14T19:28:05.0269638Z 	updating dependency infos of dmidecode-3.3
2025-06-14T19:28:05.0269897Z 	updating dependency infos of dmtx_utils-0.7.6
2025-06-14T19:28:05.0270178Z 	updating dependency infos of dnspython-1.16.0
2025-06-14T19:28:05.0270448Z 	updating dependency infos of docbook_xml_dtd-4.5
2025-06-14T19:28:05.0270771Z 	updating dependency infos of docbook_xsl_stylesheets-1.79.2
2025-06-14T19:28:05.0271436Z 	updating dependency infos of dockbert-1.0.2b1
2025-06-14T19:28:05.0271806Z 	recipe for doctranslator-0.1.0 is still broken:
2025-06-14T19:28:05.0272285Z 	Error: package doctranslator-0.1.0 cannot be built for architecture x86_64
2025-06-14T19:28:05.0272989Z 	updating dependency infos of documentviewer-0.3~git
2025-06-14T19:28:05.0273464Z 	updating dependency infos of docutils-0.20.1
2025-06-14T19:28:05.0273735Z 	updating dependency infos of dolphin-23.08.5
2025-06-14T19:28:05.0274142Z 	dolphin_emu-2412 is still marked as untested on target architecture
2025-06-14T19:28:05.0274501Z 	updating dependency infos of dolphin_kf6-25.04.0
2025-06-14T19:28:05.0274802Z 	updating dependency infos of dolphin_plugins-23.08.5
2025-06-14T19:28:05.0275135Z 	updating dependency infos of dolphin_plugins_kf6-25.04.0
2025-06-14T19:28:05.0275584Z 	updating dependency infos of dooble-2025.04.27
2025-06-14T19:28:05.0275877Z 	updating dependency infos of doom_shareware-1.9
2025-06-14T19:28:05.0276147Z 	updating dependency infos of dopewars-1.6.1
2025-06-14T19:28:05.0276406Z 	updating dependency infos of dos2unix-7.5.1
2025-06-14T19:28:05.0276657Z 	updating dependency infos of dosbox-0.74.3
2025-06-14T19:28:05.0276956Z 	updating dependency infos of dosbox_libretro-0.74_20220718
2025-06-14T19:28:05.0277314Z 	updating dependency infos of dosbox_pure_libretro-0.13_20250410
2025-06-14T19:28:05.0277641Z 	updating dependency infos of dosbox_x-2025.05.03
2025-06-14T19:28:05.0277914Z 	updating dependency infos of dosfstools-4.1
2025-06-14T19:28:05.0278186Z 	updating dependency infos of dotsies-1.0~20181222
2025-06-14T19:28:05.0278488Z 	updating dependency infos of double_conversion-3.2.0
2025-06-14T19:28:05.0278774Z 	updating dependency infos of dovecot-2.3.21
2025-06-14T19:28:05.0279028Z 	updating dependency infos of doxygen-1.12.0
2025-06-14T19:28:05.0279308Z 	updating dependency infos of doxygen2docset-0.1.2~git
2025-06-14T19:28:05.0279610Z 	updating dependency infos of doxygen_gui-1.12.0
2025-06-14T19:28:05.0279880Z 	updating dependency infos of draco-1.5.6
2025-06-14T19:28:05.0280138Z 	updating dependency infos of dragengine-1.25
2025-06-14T19:28:05.0280403Z 	updating dependency infos of dragonbox-1.1.3
2025-06-14T19:28:05.0280717Z 	dragonmemory-1 is still marked as broken on target architecture
2025-06-14T19:28:05.0281047Z 	updating dependency infos of drawpile-2.2.2
2025-06-14T19:28:05.0281513Z 	updating dependency infos of drawterm-2024.4.5
2025-06-14T19:28:05.0281799Z 	updating dependency infos of dreamchess-0.3.0
2025-06-14T19:28:05.0282145Z 	drive_encryption-1.0 is still marked as untested on target architecture
2025-06-14T19:28:05.0282478Z 	updating dependency infos of droid-113
2025-06-14T19:28:05.0282738Z 	updating dependency infos of drumcircle-1.0.5
2025-06-14T19:28:05.0283120Z 	updating dependency infos of dsfmt-2.2.5
2025-06-14T19:28:05.0283373Z 	updating dependency infos of dtc-1.6.1
2025-06-14T19:28:05.0283625Z 	updating dependency infos of ducksaver-1.1.0
2025-06-14T19:28:05.0283892Z 	updating dependency infos of duktape-2.6.0
2025-06-14T19:28:05.0284140Z 	updating dependency infos of dukto-6.0.0
2025-06-14T19:28:05.0284391Z 	updating dependency infos of dumb-0.9.3
2025-06-14T19:28:05.0284660Z 	updating dependency infos of dumb2-2.0.3~20181219
2025-06-14T19:28:05.0284945Z 	updating dependency infos of dunelegacy-0.98.2
2025-06-14T19:28:05.0285217Z 	updating dependency infos of dustrac-2.1.1
2025-06-14T19:28:05.0285478Z 	updating dependency infos of dvda_author-05.07
2025-06-14T19:28:05.0285750Z 	updating dependency infos of dvdauthor-0.7.2
2025-06-14T19:28:05.0286005Z 	updating dependency infos of dvdbackup-0.4.2
2025-06-14T19:28:05.0286268Z 	updating dependency infos of dvi2tty-6.0.2
2025-06-14T19:28:05.0286516Z 	updating dependency infos of dvipng-1.18
2025-06-14T19:28:05.0286766Z 	updating dependency infos of dvisvgm-3.4.4
2025-06-14T19:28:05.0287081Z 	dynamate-1.0.0 is still marked as untested on target architecture
2025-06-14T19:28:05.0287407Z 	updating dependency infos of e2fsprogs-1.45.6
2025-06-14T19:28:05.0287727Z 	updating dependency infos of easyrpg_libretro-0.5.1.0_20200414
2025-06-14T19:28:05.0288045Z 	updating dependency infos of ebook_tools-0.2.2
2025-06-14T19:28:05.0288393Z 	ec2drv-20180812 is still marked as untested on target architecture
2025-06-14T19:28:05.0288715Z 	updating dependency infos of ecl-24.5.10
2025-06-14T19:28:05.0288963Z 	updating dependency infos of ecode-0.7.1
2025-06-14T19:28:05.0289211Z 	updating dependency infos of ecwolf-1.4.1
2025-06-14T19:28:05.0289456Z 	updating dependency infos of ed-1.19
2025-06-14T19:28:05.0289711Z 	updating dependency infos of edfbrowser-1.84
2025-06-14T19:28:05.0289961Z 	updating dependency infos of edgar-1.36
2025-06-14T19:28:05.0290212Z 	updating dependency infos of editables-0.3
2025-06-14T19:28:05.0290674Z 	updating dependency infos of editorconfig_core_c-0.12.6
2025-06-14T19:28:05.0291546Z 	updating dependency infos of editorconfig_core_py-0.12.3
2025-06-14T19:28:05.0292057Z 	updating dependency infos of edk2-2018
2025-06-14T19:28:05.0292323Z 	updating dependency infos of eduke32-20200907
2025-06-14T19:28:05.0292631Z 	eepp-0.9.5 is still marked as untested on target architecture
2025-06-14T19:28:05.0292923Z 	updating dependency infos of efte-1.1
2025-06-14T19:28:05.0293166Z 	recipe for eggchess-1.0 is still broken:
2025-06-14T19:28:05.0293480Z 	Error: package eggchess-1.0 cannot be built for architecture x86_64
2025-06-14T19:28:05.0293809Z 	updating dependency infos of eigen-3.4.0
2025-06-14T19:28:05.0294071Z 	updating dependency infos of einsteinium-1.4.1a
2025-06-14T19:28:05.0294361Z 	updating dependency infos of eiskaltdcpp-2.4.2
2025-06-14T19:28:05.0294632Z 	updating dependency infos of elforkane-1.2
2025-06-14T19:28:05.0294878Z 	updating dependency infos of elixir-1.9.4
2025-06-14T19:28:05.0295135Z 	updating dependency infos of emacs-30.1
2025-06-14T19:28:05.0295383Z 	updating dependency infos of embree-3.12.2
2025-06-14T19:28:05.0295633Z 	updating dependency infos of enca-1.19
2025-06-14T19:28:05.0295873Z 	updating dependency infos of enchant-2.5.0
2025-06-14T19:28:05.0296140Z 	updating dependency infos of encode_locale-1.05
2025-06-14T19:28:05.0296416Z 	updating dependency infos of endless_sky-0.10.4
2025-06-14T19:28:05.0296681Z 	updating dependency infos of enet-1.3.18
2025-06-14T19:28:05.0296931Z 	updating dependency infos of epiphany-43.1
2025-06-14T19:28:05.0297255Z 	epoll_shim-0.0.20230411 is still marked as untested on target architecture
2025-06-14T19:28:05.0297595Z 	updating dependency infos of erlang-20.1
2025-06-14T19:28:05.0297833Z 	updating dependency infos of es-0.9.1
2025-06-14T19:28:05.0298072Z 	updating dependency infos of es_de-3.2.0
2025-06-14T19:28:05.0298302Z 	recipe for esdl-1.3.1 is still broken:
2025-06-14T19:28:05.0298724Z 	Error: package esdl-1.3.1 cannot be built for architecture x86_64
2025-06-14T19:28:05.0299050Z 	updating dependency infos of espeak-1.48.04
2025-06-14T19:28:05.0299309Z 	updating dependency infos of esputil-1.0.1
2025-06-14T19:28:05.0299575Z 	updating dependency infos of essays1743-2.001
2025-06-14T19:28:05.0299861Z 	updating dependency infos of eternal_lands-1.9.7.0
2025-06-14T19:28:05.0300151Z 	updating dependency infos of euae-0.8.29~wip4
2025-06-14T19:28:05.0300419Z 	updating dependency infos of eval_closure-0.14
2025-06-14T19:28:05.0300739Z 	eventual-1.0 is still marked as broken on target architecture
2025-06-14T19:28:05.0301055Z 	updating dependency infos of eventviews-23.08.5
2025-06-14T19:28:05.0301604Z 	updating dependency infos of exception_class-1.45
2025-06-14T19:28:05.0301903Z 	updating dependency infos of exceptiongroup-1.1.1
2025-06-14T19:28:05.0302183Z 	updating dependency infos of executing-1.2.0
2025-06-14T19:28:05.0302448Z 	updating dependency infos of exempi-2.6.5
2025-06-14T19:28:05.0302705Z 	updating dependency infos of exiftool-12.92
2025-06-14T19:28:05.0302959Z 	updating dependency infos of exiv2-0.27.7
2025-06-14T19:28:05.0303210Z 	updating dependency infos of exomizer-3.1.2
2025-06-14T19:28:05.0303478Z 	updating dependency infos of expandvars-0.12.0
2025-06-14T19:28:05.0303737Z 	updating dependency infos of expat-2.7.1
2025-06-14T19:28:05.0303995Z 	updating dependency infos of expect-5.45.4
2025-06-14T19:28:05.0304268Z 	updating dependency infos of exporter_tiny-1.006002
2025-06-14T19:28:05.0304563Z 	updating dependency infos of exrtranslator-0.1.0
2025-06-14T19:28:05.0304878Z 	updating dependency infos of extra_cmake_modules-6.13.0
2025-06-14T19:28:05.0305183Z 	updating dependency infos of extractpdfmark-1.1.0
2025-06-14T19:28:05.0305474Z 	updating dependency infos of extreme_tuxracer-0.6
2025-06-14T19:28:05.4890283Z packageEntries: warning: "avdevice" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.4904290Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.4918303Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.4932638Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.5269600Z packageEntries: warning: "avdevice" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.5283451Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.5297673Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.5311695Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.5655598Z packageEntries: warning: "avdevice" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.5669628Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.5684408Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.5698430Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.6034510Z packageEntries: warning: "avdevice" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.6048444Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.6062499Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:05.6076443Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:06.3402924Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:06.3717945Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:06.3881031Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:06.4046151Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.1404277Z 	updating dependency infos of extutils_config-0.010
2025-06-14T19:28:07.1404832Z 	updating dependency infos of extutils_helpers-0.028
2025-06-14T19:28:07.1405698Z 	updating dependency infos of extutils_installpaths-0.014
2025-06-14T19:28:07.1406292Z 	updating dependency infos of extutils_libbuilder-0.09
2025-06-14T19:28:07.1406793Z 	updating dependency infos of exult-1.8
2025-06-14T19:28:07.1407411Z 	f1spirit-0.rc9.1615 is still marked as untested on target architecture
2025-06-14T19:28:07.1407989Z 	updating dependency infos of faac-1.30
2025-06-14T19:28:07.1408412Z 	updating dependency infos of faad2-2.11.2
2025-06-14T19:28:07.1408869Z 	updating dependency infos of fairtrade-1.0.0~git
2025-06-14T19:28:07.1409327Z 	updating dependency infos of faiss-1.10.0
2025-06-14T19:28:07.1409856Z 	fakbetur-1.0.0 is still marked as broken on target architecture
2025-06-14T19:28:07.1410384Z 	updating dependency infos of falkon-23.08.5
2025-06-14T19:28:07.1410843Z 	updating dependency infos of fantasque_sans-1.8.0
2025-06-14T19:28:07.1411637Z 	far-2~git is still marked as untested on target architecture
2025-06-14T19:28:07.1412196Z 	updating dependency infos of farmhash-1.2~git
2025-06-14T19:28:07.1412504Z 	updating dependency infos of farsi_fonts-0.4
2025-06-14T19:28:07.1412823Z 	fasm-1.73.27 is still marked as untested on target architecture
2025-06-14T19:28:07.1413141Z 	updating dependency infos of fastdep-0.16
2025-06-14T19:28:07.1413405Z 	updating dependency infos of fasteners-0.18
2025-06-14T19:28:07.1413683Z 	updating dependency infos of fastfetch-2.42.0
2025-06-14T19:28:07.1413943Z 	updating dependency infos of fastjar-0.98
2025-06-14T19:28:07.1414203Z 	updating dependency infos of fatsort-1.6.5
2025-06-14T19:28:07.1414497Z 	fblend-0.4 is still marked as broken on target architecture
2025-06-14T19:28:07.1414804Z 	updating dependency infos of fbneo-1.0.0.2
2025-06-14T19:28:07.1415115Z 	updating dependency infos of fbneo_libretro-1.0.0.0_20250420
2025-06-14T19:28:07.1415434Z 	updating dependency infos of fbreader-0.99.4
2025-06-14T19:28:07.1415751Z 	updating dependency infos of fceumm_libretro-0.0.1_20250411
2025-06-14T19:28:07.1416060Z 	updating dependency infos of fceux-2.6.5
2025-06-14T19:28:07.1416506Z 	updating dependency infos of fcrm-0.2.0~beta
2025-06-14T19:28:07.1416770Z 	updating dependency infos of fdk_aac-2.0.2
2025-06-14T19:28:07.1417030Z 	updating dependency infos of fdupes-2.2.1
2025-06-14T19:28:07.1417341Z 	updating dependency infos of featherpad-1.5.1
2025-06-14T19:28:07.1417607Z 	updating dependency infos of feedgator-2.1.b
2025-06-14T19:28:07.1417881Z 	updating dependency infos of feedparser-6.0.10
2025-06-14T19:28:07.1418147Z 	updating dependency infos of fennel-1.4.2
2025-06-14T19:28:07.1418450Z 	fenris-0.07 is still marked as untested on target architecture
2025-06-14T19:28:07.1418753Z 	updating dependency infos of festival-2.4
2025-06-14T19:28:07.1419002Z 	updating dependency infos of ffcall-2.5
2025-06-14T19:28:07.1419243Z 	updating dependency infos of fff-2.1
2025-06-14T19:28:07.1419500Z 	updating dependency infos of ffi_checklib-0.31
2025-06-14T19:28:07.1419764Z 	updating dependency infos of ffmpeg-4.2.9
2025-06-14T19:28:07.1420019Z 	updating dependency infos of ffmpeg5-5.1.4
2025-06-14T19:28:07.1420280Z 	updating dependency infos of ffmpeg6-6.1.2
2025-06-14T19:28:07.1420550Z 	updating dependency infos of ffmpeg7-7.1.1
2025-06-14T19:28:07.1420795Z 	updating dependency infos of ffmpeggui-1.2
2025-06-14T19:28:07.1421343Z 	updating dependency infos of ffmpegthumbnailer-2.2.3~git
2025-06-14T19:28:07.1421692Z 	updating dependency infos of ffsb-6.0_rc2
2025-06-14T19:28:07.1421942Z 	updating dependency infos of fftw-3.3.10
2025-06-14T19:28:07.1422202Z 	updating dependency infos of fheroes2-0.9.18
2025-06-14T19:28:07.1422473Z 	updating dependency infos of fife-0.4.2~20220725
2025-06-14T19:28:07.1422774Z 	updating dependency infos of fifechan-0.1.5~20220725
2025-06-14T19:28:07.1423057Z 	updating dependency infos of fig2dev-3.2.8b
2025-06-14T19:28:07.1423321Z 	updating dependency infos of figlet-222
2025-06-14T19:28:07.1423570Z 	updating dependency infos of file-5.43
2025-06-14T19:28:07.1423822Z 	updating dependency infos of file_chdir-0.1011
2025-06-14T19:28:07.1424255Z 	updating dependency infos of file_copy_recursive-0.45
2025-06-14T19:28:07.1424553Z 	updating dependency infos of file_find_rule-0.34
2025-06-14T19:28:07.1424833Z 	updating dependency infos of file_listing-6.16
2025-06-14T19:28:07.1425093Z 	updating dependency infos of file_next-1.18
2025-06-14T19:28:07.1425362Z 	updating dependency infos of file_sharedir-1.118
2025-06-14T19:28:07.1425662Z 	updating dependency infos of file_sharedir_install-0.14
2025-06-14T19:28:07.1425969Z 	updating dependency infos of file_slurp-9999.32
2025-06-14T19:28:07.1426247Z 	updating dependency infos of file_slurper-0.014
2025-06-14T19:28:07.1426512Z 	updating dependency infos of file_which-1.27
2025-06-14T19:28:07.1426778Z 	updating dependency infos of filecropper-1
2025-06-14T19:28:07.1427041Z 	updating dependency infos of filelight-25.04.0
2025-06-14T19:28:07.1427313Z 	updating dependency infos of filer-1.4.0
2025-06-14T19:28:07.1427759Z 	updating dependency infos of filezilla-3.68.1
2025-06-14T19:28:07.1428257Z 	updating dependency infos of filwip-2.0.0
2025-06-14T19:28:07.1428719Z 	updating dependency infos of finance-1.0.0
2025-06-14T19:28:07.1428990Z 	updating dependency infos of findutils-4.9.0
2025-06-14T19:28:07.1429275Z 	updating dependency infos of fira_fonts-4.202
2025-06-14T19:28:07.1429636Z 	updating dependency infos of firacode-4
2025-06-14T19:28:07.1429888Z 	updating dependency infos of fish-3.7.1
2025-06-14T19:28:07.1430210Z 	fish_fillets-1.0.1 is still marked as untested on target architecture
2025-06-14T19:28:07.1430561Z 	updating dependency infos of fitspng-2.0
2025-06-14T19:28:07.1430812Z 	updating dependency infos of fizmo-0.8.5
2025-06-14T19:28:07.1431063Z 	updating dependency infos of flac-1.5.0
2025-06-14T19:28:07.1432030Z 	updating dependency infos of flac1.4-1.4.3
2025-06-14T19:28:07.1432284Z 	updating dependency infos of flac123-0.0.12
2025-06-14T19:28:07.1432542Z 	updating dependency infos of flac13-1.3.4
2025-06-14T19:28:07.1432789Z 	updating dependency infos of flacon-11.2.0
2025-06-14T19:28:07.1433048Z 	updating dependency infos of flam3-3.1.1
2025-06-14T19:28:07.1433450Z 	updating dependency infos of flameshot-12.1.0
2025-06-14T19:28:07.1433719Z 	updating dependency infos of flare-1.11
2025-06-14T19:28:07.1434010Z 	updating dependency infos of flare_data-1.11
2025-06-14T19:28:07.1434270Z 	updating dependency infos of flashback-0.5.2
2025-06-14T19:28:07.1434549Z 	updating dependency infos of flatbuffers-24.3.25
2025-06-14T19:28:07.1434886Z 	flatstyle-0.4 is still marked as untested on target architecture
2025-06-14T19:28:07.1435214Z 	updating dependency infos of flatzebra-0.1.7
2025-06-14T19:28:07.1435471Z 	updating dependency infos of flex-2.6.4
2025-06-14T19:28:07.1435714Z 	updating dependency infos of flexcat-2.18
2025-06-14T19:28:07.1435973Z 	updating dependency infos of flickcurl-1.26
2025-06-14T19:28:07.1436224Z 	updating dependency infos of flif-0.4
2025-06-14T19:28:07.1436473Z 	updating dependency infos of flit_core-3.9.0
2025-06-14T19:28:07.1436729Z 	updating dependency infos of flit_scm-1.7.0
2025-06-14T19:28:07.1436979Z 	updating dependency infos of flite-2.2
2025-06-14T19:28:07.1437229Z 	recipe for flobopuyo-0.20 is still broken:
2025-06-14T19:28:07.1437563Z 	Error: package flobopuyo-0.20 cannot be built for architecture x86_64
2025-06-14T19:28:07.1437954Z 	floorp-11.26.0 is still marked as broken on target architecture
2025-06-14T19:28:07.1438278Z 	updating dependency infos of floorp_bin-11.26.0
2025-06-14T19:28:07.1438549Z 	updating dependency infos of fltk-1.3.9
2025-06-14T19:28:07.1438799Z 	updating dependency infos of fluidlite-1.0.9
2025-06-14T19:28:07.1439127Z 	fluidsynth2-2.4.3 is still marked as untested on target architecture
2025-06-14T19:28:07.1439508Z 	fluidsynth2-2.3.6 is still marked as untested on target architecture
2025-06-14T19:28:07.1439852Z 	updating dependency infos of fluidsynth2-2.1.8
2025-06-14T19:28:07.1440167Z 	updating dependency infos of flycast_libretro-0.1_20220406
2025-06-14T19:28:07.1440488Z 	updating dependency infos of flyingtroll-0.0.1~git
2025-06-14T19:28:07.1440919Z 	updating dependency infos of fmsx_libretro-4.9_20241021
2025-06-14T19:28:07.1441558Z 	updating dependency infos of fnc-0.18
2025-06-14T19:28:07.1441825Z 	updating dependency infos of focuswriter-1.7.6
2025-06-14T19:28:07.1442103Z 	updating dependency infos of foldershaper-1.0
2025-06-14T19:28:07.1442381Z 	updating dependency infos of fontawesome-6.4.2
2025-06-14T19:28:07.1442651Z 	updating dependency infos of fontboy-0.9.8
2025-06-14T19:28:07.1442918Z 	updating dependency infos of fontconfig-2.13.96
2025-06-14T19:28:07.1443198Z 	updating dependency infos of fontforge-20230101
2025-06-14T19:28:07.1443469Z 	updating dependency infos of fonttools-4.40.0
2025-06-14T19:28:07.1443735Z 	updating dependency infos of fontutil-1.3.2
2025-06-14T19:28:07.1444008Z 	updating dependency infos of foobillardplus-3.42.0
2025-06-14T19:28:07.1444290Z 	updating dependency infos of fortuna-1.0.0
2025-06-14T19:28:07.1444539Z 	updating dependency infos of fossil-2.26
2025-06-14T19:28:07.1444797Z 	updating dependency infos of fotowall-1.0
2025-06-14T19:28:07.1445049Z 	updating dependency infos of fpc-3.2.2
2025-06-14T19:28:07.1445294Z 	updating dependency infos of fpc_bin-3.2.0
2025-06-14T19:28:07.1445559Z 	updating dependency infos of fpc_source-3.2.2
2025-06-14T19:28:07.1445839Z 	updating dependency infos of fpcupdeluxe-2.4.0~f
2025-06-14T19:28:07.1446135Z 	updating dependency infos of frame3dd-0.20140514p
2025-06-14T19:28:07.1446454Z 	updating dependency infos of frameworkintegration-5.115.0
2025-06-14T19:28:07.1446808Z 	updating dependency infos of frameworkintegration6-6.13.0
2025-06-14T19:28:07.1447103Z 	updating dependency infos of freac-1.1.7
2025-06-14T19:28:07.1447362Z 	updating dependency infos of freealut-1.1.0
2025-06-14T19:28:07.1447617Z 	updating dependency infos of freeciv-3.1.4
2025-06-14T19:28:07.1447871Z 	updating dependency infos of freedoom-0.13.0
2025-06-14T19:28:07.1448150Z 	updating dependency infos of freedroidrpg-1.0~rc2
2025-06-14T19:28:07.1448434Z 	updating dependency infos of freegemas-22.02
2025-06-14T19:28:07.1448888Z 	freegish-1.0~20170110 is still marked as untested on target architecture
2025-06-14T19:28:07.1449250Z 	updating dependency infos of freeimage-3.18.0
2025-06-14T19:28:07.1449566Z 	updating dependency infos of freeintv_libretro-0.0_20250305
2025-06-14T19:28:07.1449880Z 	updating dependency infos of freerct-0.2~git
2025-06-14T19:28:07.1450136Z 	updating dependency infos of freerdp-2.11.7
2025-06-14T19:28:07.1450393Z 	updating dependency infos of freesynd-0.8
2025-06-14T19:28:07.1450646Z 	updating dependency infos of freetype-2.13.3
2025-06-14T19:28:07.1450942Z 	updating dependency infos of freetype_bootstrap-2.13.3
2025-06-14T19:28:07.1451415Z 	updating dependency infos of freexl-2.0.0
2025-06-14T19:28:07.1451670Z 	updating dependency infos of frei0r-2.3.3
2025-06-14T19:28:07.1451929Z 	updating dependency infos of frescobaldi-3.3.0
2025-06-14T19:28:07.1452202Z 	updating dependency infos of fribidi-1.0.16
2025-06-14T19:28:07.1452461Z 	updating dependency infos of friss-0.9.0
2025-06-14T19:28:07.1452712Z 	updating dependency infos of fritzing-0.9.3b
2025-06-14T19:28:07.1452978Z 	updating dependency infos of frogatto4-4.0.2
2025-06-14T19:28:07.1453235Z 	updating dependency infos of frotz-2.54
2025-06-14T19:28:07.1453511Z 	updating dependency infos of frozen_bubble-2.212
2025-06-14T19:28:07.1453796Z 	updating dependency infos of frozendict-2.3.8
2025-06-14T19:28:07.1454079Z 	updating dependency infos of frozenlist-1.3.1
2025-06-14T19:28:07.1454348Z 	updating dependency infos of fs_uae-3.1.66
2025-06-14T19:28:07.1454624Z 	updating dependency infos of fs_uae_launcher-3.1.68
2025-06-14T19:28:07.1454915Z 	updating dependency infos of fstools-1.0~git
2025-06-14T19:28:07.1455174Z 	updating dependency infos of fswatch-1.14.0
2025-06-14T19:28:07.1455444Z 	updating dependency infos of fteqcc-20230920~git
2025-06-14T19:28:07.1455722Z 	updating dependency infos of fteqw-20240406~git
2025-06-14T19:28:07.1455985Z 	updating dependency infos of ftgl-2.1.5
2025-06-14T19:28:07.1456369Z 	updating dependency infos of ftppositive-1.2.2
2025-06-14T19:28:07.1456640Z 	updating dependency infos of fuel-1.0.1
2025-06-14T19:28:07.1456974Z 	functionplotter-0.9.2 is still marked as untested on target architecture
2025-06-14T19:28:07.1457321Z 	updating dependency infos of furnace-0.6.3
2025-06-14T19:28:07.1457570Z 	updating dependency infos of fuse-1.5.6
2025-06-14T19:28:07.1457858Z 	updating dependency infos of fuse_libretro-1.1.1_20241124
2025-06-14T19:28:07.1458221Z 	fuse_nfs-1.0.0~git is still marked as untested on target architecture
2025-06-14T19:28:07.1458548Z 	updating dependency infos of fuse_utils-1.4.3
2025-06-14T19:28:07.3327831Z packageEntries: warning: "fortran" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.3342821Z packageEntries: warning: "fortran" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.3356742Z packageEntries: warning: "jit" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.3370568Z packageEntries: warning: "syslibs" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.3385485Z packageEntries: warning: "syslibs" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.3399195Z packageEntries: warning: "syslibs" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.3413079Z packageEntries: warning: "syslibs" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.3426901Z packageEntries: warning: "syslibs" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.3440565Z packageEntries: warning: "syslibs" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.3454598Z packageEntries: warning: "syslibs" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.3468131Z packageEntries: warning: "syslibs" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.3481638Z packageEntries: warning: "syslibs" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.5040965Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.5054280Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:07.5067985Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:09.1111074Z 	updating dependency infos of fusesmb_haiku-0.9
2025-06-14T19:28:09.1111908Z 	updating dependency infos of future-0.18.3
2025-06-14T19:28:09.1112426Z 	updating dependency infos of futuresql_qt5-0.1.1
2025-06-14T19:28:09.1112983Z 	updating dependency infos of futuresql_qt6-0.1.1
2025-06-14T19:28:09.1113519Z 	updating dependency infos of fuzzylite-6.0
2025-06-14T19:28:09.1114015Z 	updating dependency infos of fx2lafw-0.1.6
2025-06-14T19:28:09.1114497Z 	recipe for fxload-20120810 is still broken:
2025-06-14T19:28:09.1115109Z 	Error: package fxload-20120810 cannot be built for architecture x86_64
2025-06-14T19:28:09.1115763Z 	updating dependency infos of fzy-1.0~git
2025-06-14T19:28:09.1116355Z 	gadgeteer-0.8.1 is still marked as broken on target architecture
2025-06-14T19:28:09.1116972Z 	updating dependency infos of galasm-2.1
2025-06-14T19:28:09.1117542Z 	updating dependency infos of gambatte_libretro-0.5.0_20250418
2025-06-14T19:28:09.1118132Z 	updating dependency infos of gambit-1.0.4
2025-06-14T19:28:09.1118643Z 	updating dependency infos of game_music_emu-0.6.4
2025-06-14T19:28:09.1119170Z 	updating dependency infos of gast-0.6.0
2025-06-14T19:28:09.1119641Z 	updating dependency infos of gawk-5.3.0
2025-06-14T19:28:09.1120093Z 	updating dependency infos of gcab-1.6
2025-06-14T19:28:09.1120552Z 	updating dependency infos of gcal-4.1
2025-06-14T19:28:09.1121042Z 	updating dependency infos of gcc-13.3.0_2023_08_10
2025-06-14T19:28:09.1121910Z 	updating dependency infos of gcc6809-4.6.4
2025-06-14T19:28:09.1122393Z 	updating dependency infos of gcompris-25.1
2025-06-14T19:28:09.1122879Z 	updating dependency infos of gcr-3.41.1
2025-06-14T19:28:09.1123331Z 	updating dependency infos of gd-2.3.3
2025-06-14T19:28:09.1123793Z 	updating dependency infos of gdal-3.4.2
2025-06-14T19:28:09.1124538Z 	updating dependency infos of gdal302-3.0.2
2025-06-14T19:28:09.1124998Z 	updating dependency infos of gdb-15.1
2025-06-14T19:28:09.1125461Z 	updating dependency infos of gdbm-1.23
2025-06-14T19:28:09.1125945Z 	updating dependency infos of gdk_pixbuf-2.42.9
2025-06-14T19:28:09.1126441Z 	updating dependency infos of geany-2.0.0
2025-06-14T19:28:09.1126931Z 	updating dependency infos of geany_plugins-2.0.0
2025-06-14T19:28:09.1127523Z 	updating dependency infos of gearboy_libretro-3.4_20250417
2025-06-14T19:28:09.1128184Z 	updating dependency infos of gearcoleco_libretro-1.0.0_20250417
2025-06-14T19:28:09.1128867Z 	updating dependency infos of gearsystem_libretro-3.4.1_20250417
2025-06-14T19:28:09.1129445Z 	updating dependency infos of gegl-0.4.56
2025-06-14T19:28:09.1129996Z 	gemdropx-0.9 is still marked as untested on target architecture
2025-06-14T19:28:09.1130580Z 	updating dependency infos of gemrb-0.9.4
2025-06-14T19:28:09.1131339Z 	gemz-0.97.0 is still marked as untested on target architecture
2025-06-14T19:28:09.1131966Z 	updating dependency infos of generaluser_gs-1.471
2025-06-14T19:28:09.1132534Z 	updating dependency infos of genesis_commander-0.49
2025-06-14T19:28:09.1133180Z 	updating dependency infos of genesis_plus_gx_libretro-1.7.4_20250418
2025-06-14T19:28:09.1133916Z 	updating dependency infos of genesis_plus_gx_wide_libretro-1.7.4_202110904
2025-06-14T19:28:09.1134534Z 	updating dependency infos of gengetopt-2.23
2025-06-14T19:28:09.1135111Z 	genie-20190612~git is still marked as untested on target architecture
2025-06-14T19:28:09.1135675Z 	updating dependency infos of genio-4.0
2025-06-14T19:28:09.1136138Z 	updating dependency infos of geogebra-5.0.766.0
2025-06-14T19:28:09.1136606Z 	updating dependency infos of geoip-1.6.12
2025-06-14T19:28:09.1137083Z 	updating dependency infos of geoipupdate-2.4.0
2025-06-14T19:28:09.1137653Z 	updating dependency infos of geolith_libretro-0.2.1_20240217
2025-06-14T19:28:09.1138455Z 	updating dependency infos of geos-3.11.0
2025-06-14T19:28:09.1138969Z 	updating dependency infos of gerbera-2.4.1
2025-06-14T19:28:09.1139515Z 	updating dependency infos of gertty-1.6.0
2025-06-14T19:28:09.1140304Z 	updating dependency infos of getconf-0.6
2025-06-14T19:28:09.1140915Z 	updating dependency infos of getopt-1.1.6
2025-06-14T19:28:09.1141737Z 	updating dependency infos of gettext-0.22.5
2025-06-14T19:28:09.1142361Z 	updating dependency infos of gexiv2-0.14.0
2025-06-14T19:28:09.1142916Z 	updating dependency infos of gflags-2.2.2
2025-06-14T19:28:09.1143430Z 	updating dependency infos of gfx2crtc-0.3.1
2025-06-14T19:28:09.1144041Z 	recipe for ghc-7.8.3 is still broken:
2025-06-14T19:28:09.1144665Z 	Error: package ghc-7.8.3 cannot be built for architecture x86_64
2025-06-14T19:28:09.1145386Z 	recipe for ghc7.10-7.10.3 is still broken:
2025-06-14T19:28:09.1146141Z 	Error: package ghc7.10-7.10.3 cannot be built for architecture x86_64
2025-06-14T19:28:09.1146680Z 	recipe for ghc8.10-8.10.5 is still broken:
2025-06-14T19:28:09.1196338Z 	Error: package ghc8.10-8.10.5 cannot be built for architecture x86_64
2025-06-14T19:28:09.1196901Z 	recipe for ghc8.10-8.10.2 is still broken:
2025-06-14T19:28:09.1197270Z 	Error: package ghc8.10-8.10.2 cannot be built for architecture x86_64
2025-06-14T19:28:09.1197613Z 	recipe for ghc8.2-8.2.2 is still broken:
2025-06-14T19:28:09.1197944Z 	Error: package ghc8.2-8.2.2 cannot be built for architecture x86_64
2025-06-14T19:28:09.1198279Z 	recipe for ghc8.6-8.6.5 is still broken:
2025-06-14T19:28:09.1198584Z 	Error: package ghc8.6-8.6.5 cannot be built for architecture x86_64
2025-06-14T19:28:09.1198937Z 	updating dependency infos of ghostscript_gpl-10.03.1
2025-06-14T19:28:09.1199258Z 	updating dependency infos of ghostwriter-24.02.2
2025-06-14T19:28:09.1199527Z 	updating dependency infos of giddy3-1.5
2025-06-14T19:28:09.1199776Z 	updating dependency infos of gif2apng-1.9
2025-06-14T19:28:09.1200028Z 	updating dependency infos of giflib-5.2.2
2025-06-14T19:28:09.1200340Z 	giflib6-5.0.5 is still marked as untested on target architecture
2025-06-14T19:28:09.1200884Z 	updating dependency infos of gifsicle-1.96
2025-06-14T19:28:09.1201373Z 	updating dependency infos of gimp-3.0.0
2025-06-14T19:28:09.1201739Z 	gimps-29.4b7 is still marked as broken on target architecture
2025-06-14T19:28:09.1202046Z 	updating dependency infos of ginac-1.7.2
2025-06-14T19:28:09.1202298Z 	updating dependency infos of girara-0.3.7
2025-06-14T19:28:09.1202543Z 	updating dependency infos of gish-1.2~git
2025-06-14T19:28:09.1202801Z 	updating dependency infos of git-2.48.1
2025-06-14T19:28:09.1203053Z 	updating dependency infos of git_cola-3.12.0
2025-06-14T19:28:09.1203365Z 	updating dependency infos of git_flow-1.8.0
2025-06-14T19:28:09.1203814Z 	updating dependency infos of gitdb-4.0.11
2025-06-14T19:28:09.1204271Z 	updating dependency infos of gitpython-3.1.40
2025-06-14T19:28:09.1204751Z 	updating dependency infos of gitqlient-1.6.2
2025-06-14T19:28:09.1205217Z 	updating dependency infos of gittyup-1.4.0
2025-06-14T19:28:09.1205775Z 	glances-3.1.3 is still marked as untested on target architecture
2025-06-14T19:28:09.1206358Z 	updating dependency infos of glaxnimate-0.5.4
2025-06-14T19:28:09.1206837Z 	updating dependency infos of glew-2.2.0
2025-06-14T19:28:09.1207281Z 	updating dependency infos of glew1-1.13.0
2025-06-14T19:28:09.1207721Z 	updating dependency infos of glew21-2.1.0
2025-06-14T19:28:09.1208164Z 	updating dependency infos of glfw-3.3.7
2025-06-14T19:28:09.1208662Z 	updating dependency infos of glib2-2.78.0
2025-06-14T19:28:09.1209202Z 	updating dependency infos of glib_networking-2.72.2
2025-06-14T19:28:09.1209713Z 	updating dependency infos of glibmm-2.66.2
2025-06-14T19:28:09.1210194Z 	updating dependency infos of glibmm2.68-2.78.0
2025-06-14T19:28:09.1210665Z 	updating dependency infos of glm-0.9.9.8
2025-06-14T19:28:09.1211286Z 	updating dependency infos of global-6.6.3
2025-06-14T19:28:09.1211729Z 	updating dependency infos of globe-0.4
2025-06-14T19:28:09.1212196Z 	updating dependency infos of globulation2-0.9.4.4
2025-06-14T19:28:09.1212674Z 	updating dependency infos of glog-0.7.1
2025-06-14T19:28:09.1213116Z 	updating dependency infos of glogg-1.1.4
2025-06-14T19:28:09.1213857Z 	gloom3d-1.0.0 is still marked as broken on target architecture
2025-06-14T19:28:09.1214401Z 	updating dependency infos of gloox-1.0.28
2025-06-14T19:28:09.1214847Z 	updating dependency infos of glpng-1.46
2025-06-14T19:28:09.1215289Z 	updating dependency infos of glslang-14.0.0
2025-06-14T19:28:09.1215733Z 	updating dependency infos of gltron-0.70
2025-06-14T19:28:09.1216166Z 	updating dependency infos of glu-9.0.0
2025-06-14T19:28:09.1216593Z 	updating dependency infos of glucas-2.9.0
2025-06-14T19:28:09.1217058Z 	updating dependency infos of glukalka-3.0.0
2025-06-14T19:28:09.1217588Z 	updating dependency infos of gme_libretro-0.5.2_20241021
2025-06-14T19:28:09.1218107Z 	updating dependency infos of gmic-3.1.2
2025-06-14T19:28:09.1218540Z 	updating dependency infos of gmime-3.2.13
2025-06-14T19:28:09.1218977Z 	updating dependency infos of gmp-6.3.0
2025-06-14T19:28:09.1219415Z 	updating dependency infos of gmp_ecm-7.0.4
2025-06-14T19:28:09.1219854Z 	updating dependency infos of gmsh-4.8.4
2025-06-14T19:28:09.1220326Z 	updating dependency infos of gn-0.1891.dfcbc6fe
2025-06-14T19:28:09.1220821Z 	updating dependency infos of gn1731-0.1731.5ed3c9cc
2025-06-14T19:28:09.1221572Z 	updating dependency infos of gnash-0.8.11~git
2025-06-14T19:28:09.1222069Z 	updating dependency infos of gnome_common-3.18.0
2025-06-14T19:28:09.1222678Z 	gnu_classpath-0.98 is still marked as untested on target architecture
2025-06-14T19:28:09.1223297Z 	updating dependency infos of gnu_efi_kernel-3.0.10
2025-06-14T19:28:09.1223795Z 	updating dependency infos of gnubg-1.07.001
2025-06-14T19:28:09.1224256Z 	updating dependency infos of gnucash-5.11
2025-06-14T19:28:09.1224702Z 	updating dependency infos of gnuchess-6.2.9
2025-06-14T19:28:09.1225248Z 	gnucobol-3.2 is still marked as untested on target architecture
2025-06-14T19:28:09.1225786Z 	updating dependency infos of gnugo-3.8
2025-06-14T19:28:09.1226246Z 	updating dependency infos of gnulib-2013_12_17
2025-06-14T19:28:09.1226920Z 	updating dependency infos of gnupg-2.4.7
2025-06-14T19:28:09.1227479Z 	gnuplot-6.0.0 is still marked as broken on target architecture
2025-06-14T19:28:09.1228033Z 	updating dependency infos of gnuplot-5.4.10
2025-06-14T19:28:09.1228500Z 	updating dependency infos of gnurobbo-0.66
2025-06-14T19:28:09.1228956Z 	updating dependency infos of gnutls-3.7.8
2025-06-14T19:28:09.1229496Z 	go_md2man-1.0.7 is still marked as untested on target architecture
2025-06-14T19:28:09.1230135Z 	updating dependency infos of gobject_introspection-1.78.1
2025-06-14T19:28:09.1230734Z 	gocr-0.50 is still marked as untested on target architecture
2025-06-14T19:28:09.1231563Z 	godot-3.0.6 is still marked as broken on target architecture
2025-06-14T19:28:09.1232091Z 	updating dependency infos of godot-2.1.6
2025-06-14T19:28:09.1232555Z 	recipe for gogo_no_coda-3.13 is still broken:
2025-06-14T19:28:09.1233149Z 	Error: package gogo_no_coda-3.13 cannot be built for architecture x86_64
2025-06-14T19:28:09.1233750Z 	updating dependency infos of golang-1.4.3
2025-06-14T19:28:09.1234223Z 	updating dependency infos of goldendict-1.5.0
2025-06-14T19:28:09.1234585Z 	updating dependency infos of googlemaps_mini-0.1
2025-06-14T19:28:09.1234874Z 	updating dependency infos of goonies-1.4.1528
2025-06-14T19:28:09.1235210Z 	gophernicus-2.0~git is still marked as untested on target architecture
2025-06-14T19:28:09.1235552Z 	recipe for gosu-0.8.7.2 is still broken:
2025-06-14T19:28:09.1235918Z 	Error: package gosu-0.8.7.2 cannot be built for architecture x86_64
2025-06-14T19:28:09.1236498Z 	updating dependency infos of gottet-1.2.3
2025-06-14T19:28:09.1237052Z 	gpart-0.3~git is still marked as untested on target architecture
2025-06-14T19:28:09.1237615Z 	updating dependency infos of gperf-3.1
2025-06-14T19:28:09.1238082Z 	updating dependency infos of gpgme-1.24.1
2025-06-14T19:28:09.1238551Z 	updating dependency infos of gphoto2-2.5.27
2025-06-14T19:28:09.1239140Z 	gphotofs-1.0git is still marked as untested on target architecture
2025-06-14T19:28:09.1239730Z 	updating dependency infos of gpp-2.25
2025-06-14T19:28:09.1240455Z 	updating dependency infos of gpsp_libretro-0.91_20250120
2025-06-14T19:28:09.1241045Z 	updating dependency infos of gptfdisk-1.0.9
2025-06-14T19:28:09.1241709Z 	updating dependency infos of gputils-1.5.0
2025-06-14T19:28:09.1242166Z 	updating dependency infos of gpxlab-0.7.0
2025-06-14T19:28:09.1242623Z 	updating dependency infos of gpxsee-13.9
2025-06-14T19:28:09.1242882Z 	updating dependency infos of grafx2-2.9
2025-06-14T19:28:09.1243146Z 	updating dependency infos of granatier-25.04.0
2025-06-14T19:28:09.1243417Z 	updating dependency infos of granite-6.2.0
2025-06-14T19:28:09.1243673Z 	updating dependency infos of grantlee-5.3.1
2025-06-14T19:28:09.1243945Z 	updating dependency infos of grantleetheme-23.08.5
2025-06-14T19:28:09.1244239Z 	updating dependency infos of graphene-1.10.8
2025-06-14T19:28:09.2905757Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:09.5930979Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:09.6102900Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:09.6375683Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8224506Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8238065Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8251800Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8265575Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8279142Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8292897Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8306443Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8320282Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8334029Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8347501Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8361269Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8739136Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8752922Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8766550Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8779949Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8793497Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8806927Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8820478Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8833839Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8847515Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:10.8860982Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.0611774Z 	updating dependency infos of graphicsmagick-1.3.40
2025-06-14T19:28:11.0612356Z 	updating dependency infos of graphite2-1.3.14
2025-06-14T19:28:11.0612703Z 	updating dependency infos of graphviz-12.2.1
2025-06-14T19:28:11.0613071Z 	grcompiler-5.2.1 is still marked as untested on target architecture
2025-06-14T19:28:11.0613423Z 	updating dependency infos of gregorio-6.1.0
2025-06-14T19:28:11.0613700Z 	updating dependency infos of grep-3.11
2025-06-14T19:28:11.0614003Z 	gri-2.12.23 is still marked as untested on target architecture
2025-06-14T19:28:11.0614336Z 	updating dependency infos of groff-1.23.0
2025-06-14T19:28:11.0614832Z 	updating dependency infos of grpc-1.53.0
2025-06-14T19:28:11.0615098Z 	updating dependency infos of gsasl-2.2.0
2025-06-14T19:28:11.0615412Z 	updating dependency infos of gsettings_desktop_schemas-43.0
2025-06-14T19:28:11.0615733Z 	updating dependency infos of gsftopk-1.19.2
2025-06-14T19:28:11.0615994Z 	updating dependency infos of gsl-2.6
2025-06-14T19:28:11.0616238Z 	updating dependency infos of gsl25-2.5
2025-06-14T19:28:11.0616499Z 	updating dependency infos of gsoap-2.8.135
2025-06-14T19:28:11.0616755Z 	updating dependency infos of gsplus-0.14
2025-06-14T19:28:11.0617042Z 	updating dependency infos of gst_plugins_bad-1.24.7
2025-06-14T19:28:11.0617361Z 	updating dependency infos of gst_plugins_base-1.24.7
2025-06-14T19:28:11.0617673Z 	updating dependency infos of gst_plugins_good-1.24.7
2025-06-14T19:28:11.0617979Z 	updating dependency infos of gst_plugins_ugly-1.24.7
2025-06-14T19:28:11.0618277Z 	updating dependency infos of gstreamer-1.24.7
2025-06-14T19:28:11.0618569Z 	updating dependency infos of gstreamermm-1.10.0
2025-06-14T19:28:11.0618843Z 	updating dependency infos of gtest-1.14.0
2025-06-14T19:28:11.0619099Z 	updating dependency infos of gtk3-3.24.36
2025-06-14T19:28:11.0619346Z 	updating dependency infos of gtk4-4.15.6
2025-06-14T19:28:11.0619608Z 	updating dependency infos of gtk_doc-1.33.2
2025-06-14T19:28:11.0619872Z 	updating dependency infos of gtkmm3-3.24.5
2025-06-14T19:28:11.0620147Z 	updating dependency infos of gtksourceview-4.8.4
2025-06-14T19:28:11.0620450Z 	updating dependency infos of gtksourceview3-3.24.0
2025-06-14T19:28:11.0620741Z 	updating dependency infos of gtkspell3-3.0.10
2025-06-14T19:28:11.0621023Z 	updating dependency infos of gucharmap-15.0.1
2025-06-14T19:28:11.0621725Z 	updating dependency infos of guideml-3.17
2025-06-14T19:28:11.0621999Z 	updating dependency infos of guile-3.0.10
2025-06-14T19:28:11.0622255Z 	updating dependency infos of guile1-1.8.8
2025-06-14T19:28:11.0622652Z 	updating dependency infos of guile2.2-2.2.7
2025-06-14T19:28:11.0622917Z 	updating dependency infos of guilib-1.2.1
2025-06-14T19:28:11.0623205Z 	updating dependency infos of guitar-1.2.999~git
2025-06-14T19:28:11.0623508Z 	updating dependency infos of guitarmaster-1.0.0~git
2025-06-14T19:28:11.0623829Z 	updating dependency infos of gulrak_filesystem-1.5.12
2025-06-14T19:28:11.0624117Z 	updating dependency infos of gumbo-0.10.1
2025-06-14T19:28:11.0624392Z 	updating dependency infos of gutenprint8-5.3.1
2025-06-14T19:28:11.0624672Z 	updating dependency infos of gutenprint9-5.3.4
2025-06-14T19:28:11.0624973Z 	updating dependency infos of gw_libretro-1.6.2_20241021
2025-06-14T19:28:11.0625272Z 	updating dependency infos of gwenhywfar-5.10.2
2025-06-14T19:28:11.0625548Z 	updating dependency infos of gwenview-23.08.5
2025-06-14T19:28:11.0625809Z 	updating dependency infos of gws-0.1.8
2025-06-14T19:28:11.0626062Z 	updating dependency infos of gyp-20230301~git
2025-06-14T19:28:11.0626331Z 	updating dependency infos of gzdoom-3.8.2
2025-06-14T19:28:11.0626580Z 	updating dependency infos of gzip-1.14
2025-06-14T19:28:11.0626885Z 	ha-0999 is still marked as untested on target architecture
2025-06-14T19:28:11.0627176Z 	updating dependency infos of hack-3.003
2025-06-14T19:28:11.0627461Z 	updating dependency infos of hacx-1.2
2025-06-14T19:28:11.0627719Z 	updating dependency infos of haiku_format-18.1.8
2025-06-14T19:28:11.0628051Z 	haiku_on_x86-1.0 is still marked as untested on target architecture
2025-06-14T19:28:11.0628381Z 	updating dependency infos of haiku_pyapi-0.3
2025-06-14T19:28:11.0628686Z 	updating dependency infos of haiku_svg_icon_theme-5.15.2.38
2025-06-14T19:28:11.0629029Z 	updating dependency infos of haiku_userguide-2024_09_09
2025-06-14T19:28:11.0629342Z 	updating dependency infos of haiku_welcome-2024_09_09
2025-06-14T19:28:11.0629632Z 	recipe for haikuplot-1.0.1 is still broken:
2025-06-14T19:28:11.0629967Z 	Error: package haikuplot-1.0.1 cannot be built for architecture x86_64
2025-06-14T19:28:11.0630321Z 	recipe for haikuplot-1.0.0 is still broken:
2025-06-14T19:28:11.0630764Z 	Error: package haikuplot-1.0.0 cannot be built for architecture x86_64
2025-06-14T19:28:11.0631314Z 	updating dependency infos of haikuporter-1.3.1
2025-06-14T19:28:11.0631600Z 	recipe for haikutodo-0.0 is still broken:
2025-06-14T19:28:11.0631929Z 	Error: package haikutodo-0.0 cannot be built for architecture x86_64
2025-06-14T19:28:11.0632574Z 	haikutwitter-1.0_git is still marked as untested on target architecture
2025-06-14T19:28:11.0633182Z 	updating dependency infos of haikuutils-r131~git
2025-06-14T19:28:11.0633602Z 	updating dependency infos of haikuwebkit-1.9.22
2025-06-14T19:28:11.0633899Z 	updating dependency infos of haikuwebsearch-0~git
2025-06-14T19:28:11.0634168Z 	updating dependency infos of haiqr-2.0
2025-06-14T19:28:11.0634432Z 	updating dependency infos of hakidecors-0.1~git
2025-06-14T19:28:11.0634894Z 	recipe for ham-0.1 is still broken:
2025-06-14T19:28:11.0635378Z 	Error: package ham-0.1 cannot be built for architecture x86_64
2025-06-14T19:28:11.0635806Z 	updating dependency infos of hamlib-4.4
2025-06-14T19:28:11.0636071Z 	updating dependency infos of handbrake-1.5.1
2025-06-14T19:28:11.0636420Z 	updating dependency infos of handy_libretro-0.95_20241021
2025-06-14T19:28:11.0636774Z 	updating dependency infos of haproxy-2.8.3
2025-06-14T19:28:11.0637031Z 	updating dependency infos of hare-1.1.1
2025-06-14T19:28:11.0637289Z 	updating dependency infos of harfbuzz-8.3.0
2025-06-14T19:28:11.0637583Z 	updating dependency infos of hatari_libretro-1.8_20241021
2025-06-14T19:28:11.0637897Z 	updating dependency infos of hatchling-1.25.0
2025-06-14T19:28:11.0638153Z 	updating dependency infos of havoc-0.3.0
2025-06-14T19:28:11.0638407Z 	updating dependency infos of hblock-3.4.4
2025-06-14T19:28:11.0638650Z 	updating dependency infos of hdf5-1.12.0
2025-06-14T19:28:11.0638904Z 	updating dependency infos of hdf5_103-1.10.6
2025-06-14T19:28:11.0639152Z 	updating dependency infos of hdialog-0.2
2025-06-14T19:28:11.0639590Z 	updating dependency infos of heart_of_darkness-0.2.9f
2025-06-14T19:28:11.0639969Z 	heartofthealien-1.2.2 is still marked as untested on target architecture
2025-06-14T19:28:11.0640317Z 	updating dependency infos of hefur-1.1~git
2025-06-14T19:28:11.0640598Z 	updating dependency infos of heictranslator-0.2.0
2025-06-14T19:28:11.0640921Z 	heidi-0.1 is still marked as untested on target architecture
2025-06-14T19:28:11.0641410Z 	updating dependency infos of heimer-1.20.0
2025-06-14T19:28:11.0641713Z 	helios-1.7.2 is still marked as untested on target architecture
2025-06-14T19:28:11.0642021Z 	updating dependency infos of hello-2.10
2025-06-14T19:28:11.0642288Z 	updating dependency infos of help2man-1.48.3
2025-06-14T19:28:11.0642565Z 	updating dependency infos of helpviewer-1.6.2.1
2025-06-14T19:28:11.0642855Z 	updating dependency infos of hermes_game-1.02
2025-06-14T19:28:11.0643114Z 	updating dependency infos of heroes-0.21
2025-06-14T19:28:11.0643380Z 	updating dependency infos of hex_a_hop-1.1.0
2025-06-14T19:28:11.0643652Z 	updating dependency infos of hexalate-1.2.3
2025-06-14T19:28:11.0643930Z 	updating dependency infos of hexcompare-1.0.4
2025-06-14T19:28:11.0644190Z 	updating dependency infos of hexedit-1.2.13
2025-06-14T19:28:11.0644449Z 	updating dependency infos of hexvexed-1.0.0
2025-06-14T19:28:11.0644705Z 	updating dependency infos of hidapi-0.10.1
2025-06-14T19:28:11.0644970Z 	updating dependency infos of hideur_maikeur-2.0
2025-06-14T19:28:11.0645246Z 	updating dependency infos of highway-1.2.0
2025-06-14T19:28:11.0645502Z 	updating dependency infos of hikounomizu-1.1
2025-06-14T19:28:11.0645763Z 	updating dependency infos of hippo-0.1~git
2025-06-14T19:28:11.0646010Z 	updating dependency infos of hiredis-1.0.2
2025-06-14T19:28:11.0646282Z 	updating dependency infos of hivelytracker-1.9
2025-06-14T19:28:11.0646548Z 	recipe for hoedown-3.0.7 is still broken:
2025-06-14T19:28:11.0646798Z 	Error: No match found for license ISC
2025-06-14T19:28:11.0647085Z 	Error: Valid license filenames included with Haiku are:
2025-06-14T19:28:11.0648794Z 	Error: Anti-Grain Geometry, Apache v2, Artistic, Artistic v2.0, BSD (2-clause), BSD (3-clause), BSD (4-clause), Be Sample Code License, Bullet, CDDL v1, CQuantizer, DEC, GLUT (Mark Kilgard), GNU GPL font exception, GNU GPL v1, GNU GPL v2, GNU GPL v3, GNU LGPL v2, GNU LGPL v2.1, GNU LGPL v3, GPC, Intel (2xxx firmware), Intel (ACPICA), Intel (firmware), LibHTTPd, LibJPEG, LibPNG, MAPM, MIT, MIT (no promotion), MPL v1.1, MPL v2.0, Marvell (firmware), OpenGroup, PDFlib Lite, Public Domain, Ralink (firmware), SGI Free B, SIL Open Font License v1.1, Zlib
2025-06-14T19:28:11.0650541Z 	Error: (in /runner/work/haikuports/haikuports/app-text/hoedown/hoedown-3.0.7.recipe)
2025-06-14T19:28:11.0650975Z 	updating dependency infos of homeworld_sdl-0.6
2025-06-14T19:28:11.0651600Z 	updating dependency infos of hqx-1.2
2025-06-14T19:28:11.0651844Z 	updating dependency infos of hstr-3.1
2025-06-14T19:28:11.0652145Z 	hteditor-2.1.0 is still marked as untested on target architecture
2025-06-14T19:28:11.0652499Z 	updating dependency infos of html2text-2020.1.16
2025-06-14T19:28:11.0652792Z 	updating dependency infos of html5_parser-0.4.10
2025-06-14T19:28:11.0653063Z 	updating dependency infos of html5lib-1.1
2025-06-14T19:28:11.0653330Z 	updating dependency infos of html_parser-3.82
2025-06-14T19:28:11.0653589Z 	updating dependency infos of htmlcxx-0.87
2025-06-14T19:28:11.0653842Z 	updating dependency infos of htmldoc-1.9.16
2025-06-14T19:28:11.0654118Z 	updating dependency infos of htop_rivoreo-2.3.1
2025-06-14T19:28:11.0654407Z 	updating dependency infos of http_cookiejar-0.014
2025-06-14T19:28:11.0654692Z 	updating dependency infos of http_cookies-6.11
2025-06-14T19:28:11.0654972Z 	updating dependency infos of http_daemon-6.16
2025-06-14T19:28:11.0655237Z 	updating dependency infos of http_date-6.06
2025-06-14T19:28:11.0655497Z 	updating dependency infos of http_message-7.00
2025-06-14T19:28:11.0655778Z 	updating dependency infos of http_negotiate-6.01
2025-06-14T19:28:11.0656180Z 	updating dependency infos of httpflow-0.0.9
2025-06-14T19:28:11.0656452Z 	updating dependency infos of httplib2-0.20.4
2025-06-14T19:28:11.0656711Z 	updating dependency infos of httrack-3.49.2
2025-06-14T19:28:11.0656969Z 	updating dependency infos of httraqt-1.4.9
2025-06-14T19:28:11.0657222Z 	updating dependency infos of hub-1.12.4
2025-06-14T19:28:11.0657472Z 	updating dependency infos of hubbub-0.3.8
2025-06-14T19:28:11.0657774Z 	hugo-3.1.03 is still marked as untested on target architecture
2025-06-14T19:28:11.0658080Z 	updating dependency infos of hugs98-dec2001
2025-06-14T19:28:11.0658385Z 	humor_sans-1.0 is still marked as broken on target architecture
2025-06-14T19:28:11.0658695Z 	updating dependency infos of hunspell-1.7.2
2025-06-14T19:28:11.0658962Z 	updating dependency infos of hw_probe-1.6.3~git
2025-06-14T19:28:11.0659225Z 	updating dependency infos of hwdata-0.392
2025-06-14T19:28:11.0659483Z 	updating dependency infos of hwloc-1.11.11
2025-06-14T19:28:11.0659741Z 	updating dependency infos of hwloc2-2.10.0
2025-06-14T19:28:11.0660037Z 	updating dependency infos of hxcfloppyemulator-2.15.2.3
2025-06-14T19:28:11.0660411Z 	hxtools-20221119 is still marked as untested on target architecture
2025-06-14T19:28:11.0660739Z 	updating dependency infos of hydrogen-1.2.2
2025-06-14T19:28:11.0661002Z 	updating dependency infos of hyperfine-1.8.0
2025-06-14T19:28:11.0661576Z 	hyperstudio-1.1_git is still marked as broken on target architecture
2025-06-14T19:28:11.0661909Z 	updating dependency infos of hyphen-2.8.8
2025-06-14T19:28:11.0662161Z 	updating dependency infos of i2pd-2.57.0
2025-06-14T19:28:11.0662409Z 	updating dependency infos of iaito-5.9.9
2025-06-14T19:28:11.0662661Z 	updating dependency infos of iasl-20230628
2025-06-14T19:28:11.0662904Z 	updating dependency infos of iat-0.1.7
2025-06-14T19:28:11.0663157Z 	updating dependency infos of ibm_plex-5.1.3
2025-06-14T19:28:11.3926840Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.3940497Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.3955039Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.3968665Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.3982932Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.3996493Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.4009923Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.4023613Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.4037212Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.4050692Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.4064970Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.4078682Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.4092155Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.9169110Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.9182494Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.9196254Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.9404578Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.9418532Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:11.9432212Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:13.1933745Z 	updating dependency infos of icebreaker-2.2.1
2025-06-14T19:28:13.1934411Z 	updating dependency infos of icecast-2.4.4
2025-06-14T19:28:13.1935205Z 	updating dependency infos of icecream-2.1.3
2025-06-14T19:28:13.1935826Z 	icedove-138.0.1 is still marked as broken on target architecture
2025-06-14T19:28:13.1936456Z 	updating dependency infos of icedove_bin-138.0.1
2025-06-14T19:28:13.1937093Z 	iceweasel-139.0.1 is still marked as broken on target architecture
2025-06-14T19:28:13.1937795Z 	iceweasel-128.5.0 is still marked as broken on target architecture
2025-06-14T19:28:13.1938442Z 	updating dependency infos of iceweasel_bin-139.0.1
2025-06-14T19:28:13.1938998Z 	updating dependency infos of icoutils-0.32.3
2025-06-14T19:28:13.1939561Z 	icu-57.2 is still marked as untested on target architecture
2025-06-14T19:28:13.1940116Z 	updating dependency infos of icu66-66.1
2025-06-14T19:28:13.1940667Z 	icu67-67.1 is still marked as broken on target architecture
2025-06-14T19:28:13.1941702Z 	updating dependency infos of icu70-70.1
2025-06-14T19:28:13.1942185Z 	updating dependency infos of icu73-73.2
2025-06-14T19:28:13.1942654Z 	updating dependency infos of icu74-74.1
2025-06-14T19:28:13.1943217Z 	icu75-75.1 is still marked as untested on target architecture
2025-06-14T19:28:13.1943863Z 	icu76-76.1 is still marked as untested on target architecture
2025-06-14T19:28:13.1944500Z 	icu77-77.1 is still marked as untested on target architecture
2025-06-14T19:28:13.1945050Z 	updating dependency infos of id3lib-3.8.3
2025-06-14T19:28:13.1945603Z 	updating dependency infos of idea_community_bin-2024.3.5
2025-06-14T19:28:13.1946230Z 	ideam-0.7.7 is still marked as untested on target architecture
2025-06-14T19:28:13.1946799Z 	updating dependency infos of idna-3.3
2025-06-14T19:28:13.1947248Z 	recipe for idutils-4.6 is still broken:
2025-06-14T19:28:13.1947846Z 	Error: package idutils-4.6 cannot be built for architecture x86_64
2025-06-14T19:28:13.1948459Z 	updating dependency infos of iec16022-0.3.0
2025-06-14T19:28:13.1948937Z 	updating dependency infos of ifaddr-0.2.0
2025-06-14T19:28:13.1949441Z 	updating dependency infos of iff_catalog-0.5
2025-06-14T19:28:13.1950081Z 	iff_ilbm_translator-2.0.2 is still marked as untested on target architecture
2025-06-14T19:28:13.1950925Z 	updating dependency infos of im-3.13
2025-06-14T19:28:13.1951612Z 	updating dependency infos of imagemagick-7.1.1.38
2025-06-14T19:28:13.1952166Z 	updating dependency infos of imageplay-6.1.1~git
2025-06-14T19:28:13.1952690Z 	updating dependency infos of imagesize-1.4.1
2025-06-14T19:28:13.1953176Z 	updating dependency infos of imagetoicon-1.0
2025-06-14T19:28:13.1953652Z 	updating dependency infos of imgcat-1.1.1
2025-06-14T19:28:13.1954114Z 	updating dependency infos of imlib2-1.12.3
2025-06-14T19:28:13.1954578Z 	updating dependency infos of immer-0.8.1
2025-06-14T19:28:13.1955101Z 	updating dependency infos of importlib_metadata-6.8.0
2025-06-14T19:28:13.1955650Z 	updating dependency infos of inconsolata-1.0
2025-06-14T19:28:13.1956134Z 	updating dependency infos of indent-2.2.11
2025-06-14T19:28:13.1956613Z 	updating dependency infos of iniconfig-1.1.1
2025-06-14T19:28:13.1957071Z 	updating dependency infos of inih-r56
2025-06-14T19:28:13.1957499Z 	updating dependency infos of inkscape-1.3.2
2025-06-14T19:28:13.1957967Z 	updating dependency infos of innoextract-1.9
2025-06-14T19:28:13.1958424Z 	updating dependency infos of installer-0.7.0
2025-06-14T19:28:13.1958875Z 	updating dependency infos of instead-3.5.0
2025-06-14T19:28:13.1959363Z 	updating dependency infos of intel_microcode-20250512
2025-06-14T19:28:13.1959894Z 	updating dependency infos of intel_one_mono-1.4.0
2025-06-14T19:28:13.1960467Z 	updating dependency infos of intel_wifi_firmwares-2025_02_11
2025-06-14T19:28:13.1960992Z 	updating dependency infos of inter-4.0
2025-06-14T19:28:13.1961668Z 	updating dependency infos of interface_elements-1.0
2025-06-14T19:28:13.1962176Z 	updating dependency infos of internalmidi-2.5.3
2025-06-14T19:28:13.1962660Z 	updating dependency infos of intltool-0.51.0
2025-06-14T19:28:13.1963111Z 	updating dependency infos of io_html-1.004
2025-06-14T19:28:13.1963580Z 	updating dependency infos of io_socket_ssl-2.089
2025-06-14T19:28:13.1964238Z 	updating dependency infos of io_string-1.08
2025-06-14T19:28:13.1964692Z 	updating dependency infos of iozone-3.493
2025-06-14T19:28:13.1965123Z 	updating dependency infos of ipc_run3-0.049
2025-06-14T19:28:13.1965596Z 	updating dependency infos of ipc_system_simple-1.30
2025-06-14T19:28:13.1966083Z 	updating dependency infos of iperf-2.1.9
2025-06-14T19:28:13.1966514Z 	updating dependency infos of iperf3-3.14
2025-06-14T19:28:13.1966956Z 	updating dependency infos of irrlicht-1.8.4
2025-06-14T19:28:13.1967392Z 	updating dependency infos of irrxml-1.2
2025-06-14T19:28:13.1967820Z 	updating dependency infos of irssi-1.4.5
2025-06-14T19:28:13.1968239Z 	updating dependency infos of isl-0.25
2025-06-14T19:28:13.1968684Z 	updating dependency infos of iso_codes-4.17.0
2025-06-14T19:28:13.1969184Z 	updating dependency infos of itinerary-25.04.0
2025-06-14T19:28:13.1969660Z 	updating dependency infos of itstool-2.0.7
2025-06-14T19:28:13.1970184Z 	iup-3.8 is still marked as untested on target architecture
2025-06-14T19:28:13.1970716Z 	updating dependency infos of ixion-0.17.0
2025-06-14T19:28:13.1971349Z 	updating dependency infos of ixion0.18-0.19.0
2025-06-14T19:28:13.1971689Z 	updating dependency infos of ja2_stracciatella-0.16.1
2025-06-14T19:28:13.1972055Z 	jack2-1.9.10~git is still marked as broken on target architecture
2025-06-14T19:28:13.1972417Z 	updating dependency infos of jam-2.5_2021_10_29
2025-06-14T19:28:13.1972706Z 	updating dependency infos of jamfile_engine-1.0.3
2025-06-14T19:28:13.1973036Z 	jammin-0.1.0 is still marked as broken on target architecture
2025-06-14T19:28:13.1973357Z 	updating dependency infos of jamvm-2.0.0
2025-06-14T19:28:13.1973615Z 	updating dependency infos of janet-1.32.1
2025-06-14T19:28:13.1973873Z 	updating dependency infos of jansson-2.14
2025-06-14T19:28:13.1974131Z 	updating dependency infos of jasper-2.0.33
2025-06-14T19:28:13.1974392Z 	updating dependency infos of jbig2dec-0.19
2025-06-14T19:28:13.1974651Z 	updating dependency infos of jbigkit-2.1
2025-06-14T19:28:13.1974907Z 	updating dependency infos of jdreplace-2.2
2025-06-14T19:28:13.1975305Z 	updating dependency infos of jdtextedit-9.1
2025-06-14T19:28:13.1975606Z 	updating dependency infos of jdtranslationhelper-3.3
2025-06-14T19:28:13.1975906Z 	updating dependency infos of jed-0.99.20_158
2025-06-14T19:28:13.1976178Z 	updating dependency infos of jetbrains_mono-2.304
2025-06-14T19:28:13.1976489Z 	updating dependency infos of jetbrains_mono_nerd-3.0.1
2025-06-14T19:28:13.1976775Z 	updating dependency infos of jigdo-0.8.2
2025-06-14T19:28:13.1977028Z 	updating dependency infos of jigit-1.22
2025-06-14T19:28:13.1977272Z 	updating dependency infos of jinja-3.1.2
2025-06-14T19:28:13.1977516Z 	updating dependency infos of jo-1.6
2025-06-14T19:28:13.1977756Z 	updating dependency infos of joe-4.6
2025-06-14T19:28:13.1978018Z 	updating dependency infos of johntheripper-1.9.0
2025-06-14T19:28:13.1978298Z 	updating dependency infos of josm_bin-18907
2025-06-14T19:28:13.1978549Z 	updating dependency infos of joyce-2.4.2
2025-06-14T19:28:13.1978826Z 	updating dependency infos of joystickutilizer-2.0.1
2025-06-14T19:28:13.1979104Z 	updating dependency infos of jpeg-9c
2025-06-14T19:28:13.1979358Z 	updating dependency infos of jpegoptim-1.4.7
2025-06-14T19:28:13.1979610Z 	updating dependency infos of jq-1.7
2025-06-14T19:28:13.1979847Z 	updating dependency infos of json_c-0.15
2025-06-14T19:28:13.1980100Z 	updating dependency infos of json_c4-0.13.1
2025-06-14T19:28:13.1980358Z 	updating dependency infos of json_glib-1.6.6
2025-06-14T19:28:13.1980623Z 	updating dependency infos of jsoncpp-1.9.5
2025-06-14T19:28:13.1980882Z 	updating dependency infos of jsoncpp24-1.9.4
2025-06-14T19:28:13.1981402Z 	julia-0.3.5 is still marked as untested on target architecture
2025-06-14T19:28:13.1981721Z 	updating dependency infos of julius-1.6.0
2025-06-14T19:28:13.1981983Z 	updating dependency infos of jumpnbump-1.61
2025-06-14T19:28:13.1982254Z 	updating dependency infos of jxl_translator-0.1.0
2025-06-14T19:28:13.1982709Z 	updating dependency infos of kaccounts_integration-23.08.5
2025-06-14T19:28:13.1983084Z 	updating dependency infos of kaccounts_integration_kf6-25.04.0
2025-06-14T19:28:13.1983440Z 	updating dependency infos of kaccounts_providers-23.08.5
2025-06-14T19:28:13.1983793Z 	updating dependency infos of kaccounts_providers_kf6-25.04.0
2025-06-14T19:28:13.1984103Z 	updating dependency infos of kacst_fonts-5.0
2025-06-14T19:28:13.1984386Z 	updating dependency infos of kactivities-5.115.0
2025-06-14T19:28:13.1984690Z 	updating dependency infos of kactivities_stats-5.115.0
2025-06-14T19:28:13.1985003Z 	updating dependency infos of kaiten_patissier-1.06
2025-06-14T19:28:13.1985290Z 	updating dependency infos of kak_lsp-12.1.0
2025-06-14T19:28:13.1985555Z 	updating dependency infos of kakoune-2021.11.08
2025-06-14T19:28:13.1985831Z 	updating dependency infos of kapman-25.04.0
2025-06-14T19:28:13.1986085Z 	updating dependency infos of kapow-1.6.2
2025-06-14T19:28:13.1986360Z 	updating dependency infos of kapptemplate-25.04.0
2025-06-14T19:28:13.1986649Z 	updating dependency infos of karchive-5.115.0
2025-06-14T19:28:13.1986927Z 	updating dependency infos of karchive6-6.13.0
2025-06-14T19:28:13.1987199Z 	updating dependency infos of kasts-25.04.0
2025-06-14T19:28:13.1987451Z 	updating dependency infos of kate-25.04.0
2025-06-14T19:28:13.1987715Z 	updating dependency infos of katomic-25.04.0
2025-06-14T19:28:13.1987969Z 	updating dependency infos of kauth-5.115.0
2025-06-14T19:28:13.1988418Z 	updating dependency infos of kauth6-6.13.0
2025-06-14T19:28:13.1988782Z 	updating dependency infos of kbbi_qt-1.1
2025-06-14T19:28:13.1989042Z 	updating dependency infos of kbibtex-0.10.0
2025-06-14T19:28:13.1989306Z 	updating dependency infos of kblocks-25.04.0
2025-06-14T19:28:13.1989583Z 	updating dependency infos of kbookmarks-5.115.0
2025-06-14T19:28:13.1989873Z 	updating dependency infos of kbookmarks6-6.13.0
2025-06-14T19:28:13.1990143Z 	updating dependency infos of kbounce-25.04.0
2025-06-14T19:28:13.1990425Z 	updating dependency infos of kbreakout-25.04.0
2025-06-14T19:28:13.1990687Z 	updating dependency infos of kbruch-25.04.0
2025-06-14T19:28:13.1991272Z 	updating dependency infos of kbuild-0.1.9998svn3572
2025-06-14T19:28:13.1991782Z 	updating dependency infos of kc-2.5.1
2025-06-14T19:28:13.1992058Z 	updating dependency infos of kcachegrind-25.04.0
2025-06-14T19:28:13.1992329Z 	updating dependency infos of kcalc-25.04.0
2025-06-14T19:28:13.1992608Z 	updating dependency infos of kcalendarcore-5.115.0
2025-06-14T19:28:13.1992909Z 	updating dependency infos of kcalendarcore6-6.13.0
2025-06-14T19:28:13.1993192Z 	updating dependency infos of kcalutils-23.08.5
2025-06-14T19:28:13.1993476Z 	updating dependency infos of kcharselect-25.04.0
2025-06-14T19:28:13.1993749Z 	updating dependency infos of kchmviewer-7.7
2025-06-14T19:28:13.1994016Z 	updating dependency infos of kcmutils-5.115.0
2025-06-14T19:28:13.1994282Z 	updating dependency infos of kcmutils6-6.13.0
2025-06-14T19:28:13.1994550Z 	updating dependency infos of kcodecs-5.115.0
2025-06-14T19:28:13.1994821Z 	updating dependency infos of kcodecs6-6.13.0
2025-06-14T19:28:13.1995093Z 	updating dependency infos of kcolorpicker-0.3.1
2025-06-14T19:28:13.1995384Z 	updating dependency infos of kcolorscheme6-6.13.0
2025-06-14T19:28:13.1995671Z 	updating dependency infos of kcompletion-5.115.0
2025-06-14T19:28:13.1995957Z 	updating dependency infos of kcompletion6-6.13.0
2025-06-14T19:28:13.1996229Z 	updating dependency infos of kconfig-5.115.0
2025-06-14T19:28:13.1996500Z 	updating dependency infos of kconfig6-6.13.0
2025-06-14T19:28:13.1996788Z 	updating dependency infos of kconfigwidgets-5.115.0
2025-06-14T19:28:13.1997098Z 	updating dependency infos of kconfigwidgets6-6.13.0
2025-06-14T19:28:13.1997393Z 	updating dependency infos of kcontacts-5.115.0
2025-06-14T19:28:13.1997669Z 	updating dependency infos of kcontacts6-6.13.0
2025-06-14T19:28:13.1997951Z 	updating dependency infos of kcoreaddons-5.115.0
2025-06-14T19:28:13.1998235Z 	updating dependency infos of kcoreaddons6-6.13.0
2025-06-14T19:28:13.1998645Z 	updating dependency infos of kcrash-5.115.0
2025-06-14T19:28:13.1998909Z 	updating dependency infos of kcrash6-6.13.0
2025-06-14T19:28:13.1999168Z 	updating dependency infos of kdav-5.115.0
2025-06-14T19:28:13.1999417Z 	updating dependency infos of kdav6-6.13.0
2025-06-14T19:28:13.1999669Z 	updating dependency infos of kdb-3.2.0
2025-06-14T19:28:13.1999939Z 	updating dependency infos of kdbusaddons-5.115.0
2025-06-14T19:28:13.2000220Z 	updating dependency infos of kdbusaddons6-6.13.0
2025-06-14T19:28:13.2000510Z 	updating dependency infos of kde_cli_tools6-6.3.4
2025-06-14T19:28:15.2157268Z 	updating dependency infos of kdebugsettings-24.12.3
2025-06-14T19:28:15.2157965Z 	updating dependency infos of kdeclarative-5.115.0
2025-06-14T19:28:15.2158536Z 	updating dependency infos of kdeclarative6-6.13.0
2025-06-14T19:28:15.2159094Z 	updating dependency infos of kdecoration6-6.3.4
2025-06-14T19:28:15.2159632Z 	updating dependency infos of kded-5.115.0
2025-06-14T19:28:15.2160147Z 	updating dependency infos of kded6-6.13.0
2025-06-14T19:28:15.2160671Z 	updating dependency infos of kdeedu_data-25.04.0
2025-06-14T19:28:15.2161497Z 	updating dependency infos of kdegraphics_mobipocket-23.08.5
2025-06-14T19:28:15.2162212Z 	updating dependency infos of kdegraphics_mobipocket_kf6-25.04.0
2025-06-14T19:28:15.2162917Z 	updating dependency infos of kdegraphics_thumbnailers-25.04.0
2025-06-14T19:28:15.2163564Z 	updating dependency infos of kdelibs4support-5.115.0
2025-06-14T19:28:15.2164237Z 	kdenlive-23.08.5 is still marked as untested on target architecture
2025-06-14T19:28:15.2164953Z 	kdenlive_kf6-25.04.0 is still marked as untested on target architecture
2025-06-14T19:28:15.2165653Z 	updating dependency infos of kdesdk_thumbnailers-23.08.5
2025-06-14T19:28:15.2166306Z 	updating dependency infos of kdesdk_thumbnailers_kf6-25.04.0
2025-06-14T19:28:15.2166946Z 	updating dependency infos of kdesignerplugin-5.115.0
2025-06-14T19:28:15.2167479Z 	updating dependency infos of kdesu6-6.13.0
2025-06-14T19:28:15.2167979Z 	updating dependency infos of kdevelop-24.05.2
2025-06-14T19:28:15.2168779Z 	updating dependency infos of kdevelop_pg_qt-2.2.2
2025-06-14T19:28:15.2169365Z 	updating dependency infos of kdevelop_pg_qt6-2.4.0
2025-06-14T19:28:15.2170030Z 	kdevelop_php-25.04.0 is still marked as untested on target architecture
2025-06-14T19:28:15.2170786Z 	kdevelop_python-25.04.0 is still marked as untested on target architecture
2025-06-14T19:28:15.2171706Z 	updating dependency infos of kdewebkit-5.115.0
2025-06-14T19:28:15.2172234Z 	updating dependency infos of kdiagram-2.8.0
2025-06-14T19:28:15.2172733Z 	updating dependency infos of kdiagram3-3.0.1
2025-06-14T19:28:15.2173242Z 	updating dependency infos of kdialog-23.08.5
2025-06-14T19:28:15.2173751Z 	updating dependency infos of kdialog_kf6-25.04.0
2025-06-14T19:28:15.2174282Z 	updating dependency infos of kdiamond-25.04.0
2025-06-14T19:28:15.2174783Z 	updating dependency infos of kdiff3-1.12.3
2025-06-14T19:28:15.2175278Z 	updating dependency infos of kdnssd-5.115.0
2025-06-14T19:28:15.2175770Z 	updating dependency infos of kdnssd6-6.13.0
2025-06-14T19:28:15.2176289Z 	updating dependency infos of kdoctools-5.115.0
2025-06-14T19:28:15.2176824Z 	updating dependency infos of kdoctools6-6.13.0
2025-06-14T19:28:15.2177391Z 	updating dependency infos of kdsingleapplication-1.1.0
2025-06-14T19:28:15.2177965Z 	updating dependency infos of kdsoap_qt5-2.2.0
2025-06-14T19:28:15.2178459Z 	updating dependency infos of kdsoap_qt6-2.2.0
2025-06-14T19:28:15.2179070Z 	updating dependency infos of kdsoap_ws_discovery_client_qt5-0.4.0
2025-06-14T19:28:15.2179789Z 	updating dependency infos of kdsoap_ws_discovery_client_qt6-0.4.0
2025-06-14T19:28:15.2180415Z 	updating dependency infos of keepassxc-2.6.2
2025-06-14T19:28:15.2180933Z 	updating dependency infos of kemoticons-5.115.0
2025-06-14T19:28:15.2181590Z 	updating dependency infos of kexi-3.2.0
2025-06-14T19:28:15.2182065Z 	updating dependency infos of keychain-2.8.5
2025-06-14T19:28:15.2182559Z 	updating dependency infos of keycursor-1.2
2025-06-14T19:28:15.2183341Z 	updating dependency infos of keymapswitcher-1.2.7.16
2025-06-14T19:28:15.2183968Z 	keystone-0.9.1 is still marked as untested on target architecture
2025-06-14T19:28:15.2184565Z 	updating dependency infos of kfilemetadata-5.115.0
2025-06-14T19:28:15.2185084Z 	updating dependency infos of kfilemetadata6-6.13.0
2025-06-14T19:28:15.2185596Z 	updating dependency infos of kfourinline-25.04.0
2025-06-14T19:28:15.2186100Z 	updating dependency infos of kgeography-25.04.0
2025-06-14T19:28:15.2186566Z 	updating dependency infos of kget-23.08.5
2025-06-14T19:28:15.2187037Z 	updating dependency infos of kglobalaccel-5.115.0
2025-06-14T19:28:15.2187543Z 	updating dependency infos of kglobalaccel6-6.13.0
2025-06-14T19:28:15.2188048Z 	updating dependency infos of kgoldrunner-25.04.0
2025-06-14T19:28:15.2188541Z 	updating dependency infos of kgraphviewer-25.04.0
2025-06-14T19:28:15.2189041Z 	updating dependency infos of kguiaddons-5.115.0
2025-06-14T19:28:15.2189535Z 	updating dependency infos of kguiaddons6-6.13.0
2025-06-14T19:28:15.2190017Z 	updating dependency infos of khangman-25.04.0
2025-06-14T19:28:15.2190571Z 	updating dependency infos of khealthcertificate_kf6-25.04.0
2025-06-14T19:28:15.2191541Z 	updating dependency infos of kholidays-5.115.0
2025-06-14T19:28:15.2192039Z 	updating dependency infos of kholidays6-6.13.0
2025-06-14T19:28:15.2192496Z 	updating dependency infos of khtml-5.115.0
2025-06-14T19:28:15.2192947Z 	updating dependency infos of ki18n-5.115.0
2025-06-14T19:28:15.2193377Z 	updating dependency infos of ki18n6-6.13.0
2025-06-14T19:28:15.2193841Z 	updating dependency infos of kiconthemes-5.115.0
2025-06-14T19:28:15.2194341Z 	updating dependency infos of kiconthemes6-6.13.0
2025-06-14T19:28:15.2194805Z 	updating dependency infos of kid3-3.9.6
2025-06-14T19:28:15.2195323Z 	updating dependency infos of kidentitymanagement-23.08.5
2025-06-14T19:28:15.2195854Z 	updating dependency infos of kidletime-5.115.0
2025-06-14T19:28:15.2196341Z 	updating dependency infos of kidletime6-6.13.0
2025-06-14T19:28:15.2196810Z 	updating dependency infos of kig-25.04.0
2025-06-14T19:28:15.2197435Z 	updating dependency infos of kigo-25.04.0
2025-06-14T19:28:15.2197906Z 	updating dependency infos of kile-3.0~b3
2025-06-14T19:28:15.2198396Z 	updating dependency infos of kimageannotator-0.7.1
2025-06-14T19:28:15.2198890Z 	updating dependency infos of kimageformats-5.115.0
2025-06-14T19:28:15.2199194Z 	updating dependency infos of kimageformats6-6.13.0
2025-06-14T19:28:15.2199478Z 	updating dependency infos of kimap-23.08.5
2025-06-14T19:28:15.2199734Z 	updating dependency infos of kinit-5.115.0
2025-06-14T19:28:15.2199985Z 	updating dependency infos of kio-5.115.0
2025-06-14T19:28:15.2200229Z 	updating dependency infos of kio6-6.13.0
2025-06-14T19:28:15.2200494Z 	updating dependency infos of kio_extras-23.08.5
2025-06-14T19:28:15.2200789Z 	updating dependency infos of kio_extras_kf6-25.04.0
2025-06-14T19:28:15.2201074Z 	updating dependency infos of kio_gdrive-23.08.5
2025-06-14T19:28:15.2201638Z 	updating dependency infos of kio_gdrive_kf6-25.04.0
2025-06-14T19:28:15.2201931Z 	updating dependency infos of kirigami-5.115.0
2025-06-14T19:28:15.2202209Z 	updating dependency infos of kirigami6-6.13.0
2025-06-14T19:28:15.2202488Z 	updating dependency infos of kirigami_addons-0.11.0
2025-06-14T19:28:15.2202810Z 	updating dependency infos of kirigami_addons_kf6-1.8.1
2025-06-14T19:28:15.2203111Z 	updating dependency infos of kitemmodels-5.115.0
2025-06-14T19:28:15.2203401Z 	updating dependency infos of kitemmodels6-6.13.0
2025-06-14T19:28:15.2203687Z 	updating dependency infos of kitemviews-5.115.0
2025-06-14T19:28:15.2203965Z 	updating dependency infos of kitemviews6-6.13.0
2025-06-14T19:28:15.2204238Z 	updating dependency infos of kiten-25.04.0
2025-06-14T19:28:15.2204509Z 	updating dependency infos of kitinerary_kf6-25.04.0
2025-06-14T19:28:15.2204798Z 	updating dependency infos of kiwisolver-1.3.1
2025-06-14T19:28:15.2205068Z 	updating dependency infos of kiwix_tools-3.7.0
2025-06-14T19:28:15.2205501Z 	updating dependency infos of kjobwidgets-5.115.0
2025-06-14T19:28:15.2205814Z 	updating dependency infos of kjobwidgets6-6.13.0
2025-06-14T19:28:15.2206085Z 	updating dependency infos of kjs-5.115.0
2025-06-14T19:28:15.2206361Z 	updating dependency infos of kjumpingcube-25.04.0
2025-06-14T19:28:15.2206638Z 	updating dependency infos of kldap-23.08.5
2025-06-14T19:28:15.2206907Z 	updating dependency infos of klettres-25.04.0
2025-06-14T19:28:15.2207175Z 	updating dependency infos of klickety-25.04.0
2025-06-14T19:28:15.2207444Z 	updating dependency infos of klines-25.04.0
2025-06-14T19:28:15.2207700Z 	recipe for klystron-0.0.0 is still broken:
2025-06-14T19:28:15.2208056Z 	Error: package klystron-0.0.0 cannot be built for architecture x86_64
2025-06-14T19:28:15.2208424Z 	updating dependency infos of kmahjongg-25.04.0
2025-06-14T19:28:15.2208720Z 	updating dependency infos of kmailtransport-23.08.5
2025-06-14T19:28:15.2209013Z 	updating dependency infos of kmbox-23.08.5
2025-06-14T19:28:15.2209266Z 	updating dependency infos of kmime-23.08.5
2025-06-14T19:28:15.2209530Z 	updating dependency infos of kmime_kf6-25.04.0
2025-06-14T19:28:15.2209794Z 	updating dependency infos of kmines-25.04.0
2025-06-14T19:28:15.2210052Z 	updating dependency infos of kmplot-25.04.0
2025-06-14T19:28:15.2210311Z 	updating dependency infos of kmymoney-5.1.3
2025-06-14T19:28:15.2210583Z 	updating dependency infos of knavalbattle-25.04.0
2025-06-14T19:28:15.2210869Z 	updating dependency infos of knetwalk-25.04.0
2025-06-14T19:28:15.2211344Z 	updating dependency infos of knewstuff-5.115.0
2025-06-14T19:28:15.2211843Z 	updating dependency infos of knewstuff6-6.13.0
2025-06-14T19:28:15.2212153Z 	updating dependency infos of knights-25.04.0
2025-06-14T19:28:15.2212445Z 	updating dependency infos of knotifications-5.115.0
2025-06-14T19:28:15.2212755Z 	updating dependency infos of knotifications6-6.13.0
2025-06-14T19:28:15.2213055Z 	updating dependency infos of knotifyconfig-5.115.0
2025-06-14T19:28:15.2213355Z 	updating dependency infos of knotifyconfig6-6.13.0
2025-06-14T19:28:15.2213644Z 	updating dependency infos of kobodeluxe-0.5.1
2025-06-14T19:28:15.2214038Z 	updating dependency infos of koder-0.6.0
2025-06-14T19:28:15.2214317Z 	updating dependency infos of kolourpaint-24.02.2
2025-06-14T19:28:15.2214597Z 	updating dependency infos of kommit-1.6.0
2025-06-14T19:28:15.2214854Z 	updating dependency infos of kompare-25.04.0
2025-06-14T19:28:15.2215119Z 	updating dependency infos of kona-20190226
2025-06-14T19:28:15.2215374Z 	updating dependency infos of konfetti-1.0.0
2025-06-14T19:28:15.2215632Z 	updating dependency infos of konsole-23.08.5
2025-06-14T19:28:15.2215905Z 	updating dependency infos of konsole_kf6-25.04.0
2025-06-14T19:28:15.2216207Z 	updating dependency infos of kontactinterface-23.08.5
2025-06-14T19:28:15.2216649Z 	updating dependency infos of konversation-25.04.0
2025-06-14T19:28:15.2217143Z 	updating dependency infos of kopeninghours_kf6-25.04.0
2025-06-14T19:28:15.2217442Z 	updating dependency infos of koreanim-0.0.2
2025-06-14T19:28:15.2217735Z 	updating dependency infos of kosmindoormap_kf6-25.04.0
2025-06-14T19:28:15.2218056Z 	updating dependency infos of kotatogram_desktop-1.4.9
2025-06-14T19:28:15.2218348Z 	updating dependency infos of kottan-0.14.4
2025-06-14T19:28:15.2218600Z 	updating dependency infos of kovel-1.0.0
2025-06-14T19:28:15.2218866Z 	updating dependency infos of kpackage-5.115.0
2025-06-14T19:28:15.2219133Z 	updating dependency infos of kpackage6-6.13.0
2025-06-14T19:28:15.2219400Z 	updating dependency infos of kparts-5.115.0
2025-06-14T19:28:15.2219650Z 	updating dependency infos of kparts6-6.13.0
2025-06-14T19:28:15.2219912Z 	updating dependency infos of kpeople-5.115.0
2025-06-14T19:28:15.2220172Z 	updating dependency infos of kpeople6-6.13.0
2025-06-14T19:28:15.2220506Z 	kphotoalbum-5.13.0 is still marked as untested on target architecture
2025-06-14T19:28:15.2220867Z 	updating dependency infos of kpimtextedit-23.08.5
2025-06-14T19:28:15.2221355Z 	updating dependency infos of kpkpass_kf6-25.04.0
2025-06-14T19:28:15.2221799Z 	updating dependency infos of kplotting-5.115.0
2025-06-14T19:28:15.2222086Z 	updating dependency infos of kplotting6-6.13.0
2025-06-14T19:28:15.2222357Z 	updating dependency infos of kpmcore-21.12.0
2025-06-14T19:28:15.2222620Z 	updating dependency infos of kproperty-3.2.0
2025-06-14T19:28:15.2222888Z 	updating dependency infos of kpty-5.115.0
2025-06-14T19:28:15.2223140Z 	updating dependency infos of kpty6-6.13.0
2025-06-14T19:28:15.2223438Z 	updating dependency infos of kpublictransport_kf6-25.04.0
2025-06-14T19:28:15.2223746Z 	updating dependency infos of kqlives-0.99
2025-06-14T19:28:15.2224020Z 	updating dependency infos of kqtquickcharts-25.04.0
2025-06-14T19:28:15.2224319Z 	updating dependency infos of kquickcharts-5.115.0
2025-06-14T19:28:15.2224607Z 	updating dependency infos of kquickcharts6-6.13.0
2025-06-14T19:28:15.2224910Z 	updating dependency infos of kquickimageeditor-0.3.0
2025-06-14T19:28:15.2225239Z 	updating dependency infos of kquickimageeditor_kf6-0.5.1
2025-06-14T19:28:15.2225593Z 	kraptor-4.4.14 is still marked as untested on target architecture
2025-06-14T19:28:15.2225912Z 	updating dependency infos of krb5-1.20
2025-06-14T19:28:15.2226157Z 	updating dependency infos of krdc-24.12.3
2025-06-14T19:28:17.0806978Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:17.0820471Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:17.0834145Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:17.0847837Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:17.0861524Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:17.0875180Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:17.0888544Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:17.0901993Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:17.0916239Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:17.0930224Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:17.0944258Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:17.4256964Z 	updating dependency infos of kreport-3.2.0
2025-06-14T19:28:17.4257521Z 	updating dependency infos of kreversi-25.04.0
2025-06-14T19:28:17.4257999Z 	updating dependency infos of kristall-0.4
2025-06-14T19:28:17.4258443Z 	updating dependency infos of krita-5.2.9
2025-06-14T19:28:17.4258872Z 	updating dependency infos of kross-5.115.0
2025-06-14T19:28:17.4259320Z 	updating dependency infos of kruler-25.04.0
2025-06-14T19:28:17.4259768Z 	updating dependency infos of krunner-5.115.0
2025-06-14T19:28:17.4260236Z 	updating dependency infos of krunner6-6.13.0
2025-06-14T19:28:17.4260582Z 	updating dependency infos of krusader-2.7.2
2025-06-14T19:28:17.4260906Z 	updating dependency infos of ksanecore-23.08.5
2025-06-14T19:28:17.4261498Z 	updating dependency infos of ksanecore_kf6-25.04.0
2025-06-14T19:28:17.4261807Z 	updating dependency infos of kservice-5.115.0
2025-06-14T19:28:17.4262094Z 	updating dependency infos of kservice6-6.13.0
2025-06-14T19:28:17.4262356Z 	updating dependency infos of kshisen-25.04.0
2025-06-14T19:28:17.4262618Z 	updating dependency infos of ksirk-25.04.0
2025-06-14T19:28:17.4262872Z 	updating dependency infos of ksmtp-23.08.5
2025-06-14T19:28:17.4263129Z 	updating dependency infos of ksquares-25.04.0
2025-06-14T19:28:17.4263395Z 	updating dependency infos of kstars-3.6.6
2025-06-14T19:28:17.4263698Z 	updating dependency infos of kstatusnotifieritem6-6.13.0
2025-06-14T19:28:17.4264016Z 	updating dependency infos of ksudoku-25.04.0
2025-06-14T19:28:17.4264275Z 	updating dependency infos of ksvg6-6.13.0
2025-06-14T19:28:17.4264579Z 	updating dependency infos of ksyntax_highlighting-5.115.0
2025-06-14T19:28:17.4265140Z 	updating dependency infos of ksyntax_highlighting6-6.13.0
2025-06-14T19:28:17.4265466Z 	updating dependency infos of ksystemlog-25.04.0
2025-06-14T19:28:17.4265789Z 	updating dependency infos of ktechlab-0.50.0~git
2025-06-14T19:28:17.4266148Z 	ktextaddons-1.6.0 is still marked as untested on target architecture
2025-06-14T19:28:17.4266490Z 	updating dependency infos of ktextaddons-1.5.4
2025-06-14T19:28:17.4266780Z 	updating dependency infos of ktexteditor-5.115.0
2025-06-14T19:28:17.4267063Z 	updating dependency infos of ktexteditor6-6.13.0
2025-06-14T19:28:17.4267355Z 	updating dependency infos of ktexttemplate6-6.13.0
2025-06-14T19:28:17.4267656Z 	updating dependency infos of ktextwidgets-5.115.0
2025-06-14T19:28:17.4267943Z 	updating dependency infos of ktextwidgets6-6.13.0
2025-06-14T19:28:17.4268226Z 	updating dependency infos of ktnef-23.08.5
2025-06-14T19:28:17.4268483Z 	updating dependency infos of ktorrent-5.1.2
2025-06-14T19:28:17.4268747Z 	updating dependency infos of ktouch-25.04.0
2025-06-14T19:28:17.4269015Z 	updating dependency infos of ktuberling-25.04.0
2025-06-14T19:28:17.4269299Z 	updating dependency infos of kubrick-25.04.0
2025-06-14T19:28:17.4269568Z 	updating dependency infos of kumoworks-1.0.1~git
2025-06-14T19:28:17.4269870Z 	updating dependency infos of kunitconversion-5.115.0
2025-06-14T19:28:17.4270193Z 	updating dependency infos of kunitconversion6-6.13.0
2025-06-14T19:28:17.4270488Z 	updating dependency infos of kuserfeedback-1.3.0
2025-06-14T19:28:17.4270784Z 	updating dependency infos of kuserfeedback6-6.13.0
2025-06-14T19:28:17.4271064Z 	updating dependency infos of kvazaar-2.3.1
2025-06-14T19:28:17.4271631Z 	updating dependency infos of kwallet-5.115.0
2025-06-14T19:28:17.4271894Z 	updating dependency infos of kwallet6-6.13.0
2025-06-14T19:28:17.4272172Z 	updating dependency infos of kwave-23.08.5
2025-06-14T19:28:17.4272446Z 	updating dependency infos of kweathercore-0.7
2025-06-14T19:28:17.4272730Z 	updating dependency infos of kweathercore_kf6-0.8.0
2025-06-14T19:28:17.4273044Z 	updating dependency infos of kwidgetsaddons-5.115.0
2025-06-14T19:28:17.4273467Z 	updating dependency infos of kwidgetsaddons6-6.13.0
2025-06-14T19:28:17.4273771Z 	updating dependency infos of kwindowsystem-5.115.0
2025-06-14T19:28:17.4274062Z 	updating dependency infos of kwindowsystem6-6.13.0
2025-06-14T19:28:17.4274342Z 	updating dependency infos of kwrite-25.04.0
2025-06-14T19:28:17.4274601Z 	updating dependency infos of kxmlgui-5.115.0
2025-06-14T19:28:17.4274862Z 	updating dependency infos of kxmlgui6-6.13.0
2025-06-14T19:28:17.4275119Z 	updating dependency infos of kyua-0.13
2025-06-14T19:28:17.4275364Z 	updating dependency infos of lab3d-3.0.1
2025-06-14T19:28:17.4275623Z 	updating dependency infos of labplot-2.12.0
2025-06-14T19:28:17.4275882Z 	updating dependency infos of ladspa_sdk-1.13
2025-06-14T19:28:17.4276171Z 	updating dependency infos of ladybird-pre20220728
2025-06-14T19:28:17.4276457Z 	updating dependency infos of lager-0.1.1
2025-06-14T19:28:17.4276724Z 	updating dependency infos of lagrange-1.17.6
2025-06-14T19:28:17.4276984Z 	updating dependency infos of lame-3.100
2025-06-14T19:28:17.4277243Z 	updating dependency infos of lapack-3.10.0
2025-06-14T19:28:17.4277505Z 	updating dependency infos of laserkombat-1.0
2025-06-14T19:28:17.4277772Z 	updating dependency infos of lateef_font-1.001
2025-06-14T19:28:17.4278042Z 	updating dependency infos of latex2html-2024
2025-06-14T19:28:17.4278304Z 	updating dependency infos of lato_fonts-2.015
2025-06-14T19:28:17.4278584Z 	updating dependency infos of launchpad-1.3~git
2025-06-14T19:28:17.4278900Z 	lava-1.0 is still marked as untested on target architecture
2025-06-14T19:28:17.4279214Z 	updating dependency infos of lazarus_bin-4.0
2025-06-14T19:28:17.4279508Z 	updating dependency infos of lazy_object_proxy-1.5.2
2025-06-14T19:28:17.4279798Z 	updating dependency infos of lbreakout2-2.6.5
2025-06-14T19:28:17.4280084Z 	updating dependency infos of lbreakout2_levels-1.0
2025-06-14T19:28:17.4280371Z 	updating dependency infos of lbreakout2_themes-1.0
2025-06-14T19:28:17.4281487Z 	updating dependency infos of lbreakouthd-1.1.1
2025-06-14T19:28:17.4281784Z 	updating dependency infos of lcab-1.0b12
2025-06-14T19:28:17.4282084Z 	updating dependency infos of lcdf_typetools-2.110
2025-06-14T19:28:17.4282469Z 	updating dependency infos of lcdproc-0.5.9
2025-06-14T19:28:17.4282730Z 	updating dependency infos of lcms-2.16
2025-06-14T19:28:17.4283049Z 	updating dependency infos of lcov-1.16
2025-06-14T19:28:17.4283336Z 	updating dependency infos of ldmicroqt-2.3.2
2025-06-14T19:28:17.4283603Z 	updating dependency infos of lemon-1.0~src
2025-06-14T19:28:17.4283966Z 	updating dependency infos of lensfun-0.3.2
2025-06-14T19:28:17.4284227Z 	updating dependency infos of leocad-23.03
2025-06-14T19:28:17.4284498Z 	updating dependency infos of leptonica-1.82.0
2025-06-14T19:28:17.4284862Z 	updating dependency infos of less-668
2025-06-14T19:28:17.4285105Z 	updating dependency infos of leveldb-1.23
2025-06-14T19:28:17.4285407Z 	updating dependency infos of lexilla-5.2.4
2025-06-14T19:28:17.4285755Z 	updating dependency infos of lftp-4.9.2
2025-06-14T19:28:17.4286015Z 	updating dependency infos of lgeneral-1.4.3
2025-06-14T19:28:17.4286397Z 	updating dependency infos of lgogdownloader-3.16
2025-06-14T19:28:17.4286667Z 	updating dependency infos of lgrep-1.0
2025-06-14T19:28:17.4286932Z 	updating dependency infos of lha-1.14i.ac20211125
2025-06-14T19:28:17.4287303Z 	updating dependency infos of lib3ds-2.0.0
2025-06-14T19:28:17.4287562Z 	updating dependency infos of libaacs-0.11.0
2025-06-14T19:28:17.4287875Z 	updating dependency infos of libabw-0.1.3
2025-06-14T19:28:17.4288198Z 	updating dependency infos of libaccounts_glib-1.27
2025-06-14T19:28:17.4288500Z 	updating dependency infos of libaccounts_qt5-1.17
2025-06-14T19:28:17.4288892Z 	updating dependency infos of libaccounts_qt6-1.17
2025-06-14T19:28:17.4289199Z 	updating dependency infos of libalkimia-8.1.2
2025-06-14T19:28:17.4289551Z 	updating dependency infos of libao-1.2.2
2025-06-14T19:28:17.4289837Z 	updating dependency infos of libarchive-3.7.9
2025-06-14T19:28:17.4290114Z 	updating dependency infos of libart_lgpl-2.3.21
2025-06-14T19:28:17.4290697Z 	updating dependency infos of libasr-1.0.2
2025-06-14T19:28:17.4290969Z 	updating dependency infos of libass-0.17.4
2025-06-14T19:28:17.4291473Z 	updating dependency infos of libassuan-2.5.5
2025-06-14T19:28:17.4291758Z 	updating dependency infos of libatomic_ops-7.8.2
2025-06-14T19:28:17.4292131Z 	updating dependency infos of libaubio-0.4.9
2025-06-14T19:28:17.4292403Z 	updating dependency infos of libavif-0.9.3
2025-06-14T19:28:17.4292685Z 	updating dependency infos of libavif1.0-1.1.0
2025-06-14T19:28:17.4303059Z 	libavlduptree-1.0.0 is still marked as untested on target architecture
2025-06-14T19:28:17.4303453Z 	updating dependency infos of libb2-0.98.1
2025-06-14T19:28:17.4303838Z 	updating dependency infos of libbase58-0.1.4
2025-06-14T19:28:17.4304126Z 	updating dependency infos of libbdplus-0.1.2
2025-06-14T19:28:17.4304425Z 	updating dependency infos of libblkmaker-0.5.3
2025-06-14T19:28:17.4304820Z 	updating dependency infos of libbluray-1.3.1
2025-06-14T19:28:17.4305163Z 	libbluray1-0.9.3 is still marked as untested on target architecture
2025-06-14T19:28:17.4305649Z 	libbpg-0.9.8 is still marked as untested on target architecture
2025-06-14T19:28:17.4305969Z 	updating dependency infos of libbs2b-3.1.0
2025-06-14T19:28:17.4306328Z 	updating dependency infos of libbson-1.1.10
2025-06-14T19:28:17.4306590Z 	updating dependency infos of libburn-1.4.8
2025-06-14T19:28:17.4306870Z 	updating dependency infos of libburndevice-1.0
2025-06-14T19:28:17.4307245Z 	updating dependency infos of libcaca-0.99.beta19
2025-06-14T19:28:17.4307520Z 	updating dependency infos of libcangjie-1.3
2025-06-14T19:28:17.4307877Z 	updating dependency infos of libcddb-1.3.2
2025-06-14T19:28:17.4308135Z 	updating dependency infos of libcdio-2.1.0
2025-06-14T19:28:17.4308391Z 	updating dependency infos of libcdio0-0.94
2025-06-14T19:28:17.4308753Z 	updating dependency infos of libcdio1-2.0.0
2025-06-14T19:28:17.4309241Z 	updating dependency infos of libcdio_paranoia-10.2_2.0.1
2025-06-14T19:28:17.4309669Z 	updating dependency infos of libcdr-0.1.8
2025-06-14T19:28:17.4309922Z 	updating dependency infos of libcec-4.0.3
2025-06-14T19:28:17.4310252Z 	updating dependency infos of libcerf-2.4
2025-06-14T19:28:17.4310542Z 	updating dependency infos of libchewing-0.5.1
2025-06-14T19:28:17.4310817Z 	updating dependency infos of libclaw-1.7.4
2025-06-14T19:28:17.4311371Z 	updating dependency infos of libcmis-0.5.2
2025-06-14T19:28:17.4311650Z 	updating dependency infos of libcmis0.6-0.6.2
2025-06-14T19:28:17.4312034Z 	updating dependency infos of libconfig-1.7.2
2025-06-14T19:28:17.4312379Z 	libcoverart-1.0.0~git is still marked as untested on target architecture
2025-06-14T19:28:17.4312836Z 	updating dependency infos of libcpuid-0.6.5
2025-06-14T19:28:17.4313102Z 	updating dependency infos of libcroco-0.6.13
2025-06-14T19:28:17.4313386Z 	updating dependency infos of libcss-0.9.2
2025-06-14T19:28:17.4313735Z 	updating dependency infos of libcuefile-475
2025-06-14T19:28:17.4313995Z 	updating dependency infos of libdaemon-0.14
2025-06-14T19:28:17.4314355Z 	updating dependency infos of libdatrie-0.2.12
2025-06-14T19:28:17.4314637Z 	updating dependency infos of libdazzle-3.44.0
2025-06-14T19:28:17.4314902Z 	updating dependency infos of libdbi-0.9.0
2025-06-14T19:28:17.4315302Z 	updating dependency infos of libdbi_drivers-0.9.0
2025-06-14T19:28:17.4315590Z 	updating dependency infos of libdca-0.0.7
2025-06-14T19:28:17.4315912Z 	updating dependency infos of libde265-1.0.8
2025-06-14T19:28:17.4316209Z 	updating dependency infos of libdeflate-1.18
2025-06-14T19:28:17.4316479Z 	updating dependency infos of libdiscid-0.6.4
2025-06-14T19:28:17.4316846Z 	updating dependency infos of libdmtx-0.7.5
2025-06-14T19:28:17.4317105Z 	updating dependency infos of libdom-0.4.2
2025-06-14T19:28:17.4317357Z 	updating dependency infos of libdsk-1.5.8
2025-06-14T19:28:17.4317707Z 	updating dependency infos of libdsm-0.3.2
2025-06-14T19:28:17.4317964Z 	updating dependency infos of libdv-1.0.0
2025-06-14T19:28:17.4318440Z 	updating dependency infos of libdvbpsi-1.3.3
2025-06-14T19:28:17.4318748Z 	updating dependency infos of libdvbpsi12-1.2.0
2025-06-14T19:28:17.4319065Z 	updating dependency infos of libdvdcss-1.4.3
2025-06-14T19:28:17.4319425Z 	updating dependency infos of libdvdnav-6.1.1
2025-06-14T19:28:17.4319690Z 	updating dependency infos of libdvdread-6.1.3
2025-06-14T19:28:17.4320072Z 	updating dependency infos of libdwarf-0.11.1
2025-06-14T19:28:17.4320536Z 	updating dependency infos of libdxfrw-2.2.0
2025-06-14T19:28:17.4320999Z 	updating dependency infos of libebml-1.4.4
2025-06-14T19:28:17.4321597Z 	updating dependency infos of libebml4-1.3.10
2025-06-14T19:28:17.4322087Z 	updating dependency infos of libebook-0.1.3
2025-06-14T19:28:17.4322575Z 	updating dependency infos of libebur128-1.2.6
2025-06-14T19:28:17.4323076Z 	updating dependency infos of libeconf-0.5.2
2025-06-14T19:28:17.4323568Z 	updating dependency infos of libedit-20230828_3.1
2025-06-14T19:28:17.4324104Z 	updating dependency infos of libeditline-1.17.1
2025-06-14T19:28:17.4324596Z 	updating dependency infos of libelf-0.8.13
2025-06-14T19:28:17.4325063Z 	updating dependency infos of libepoxy-1.5.8
2025-06-14T19:28:18.9975320Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:18.9988341Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:19.6234243Z 	updating dependency infos of libepubgen-0.1.1
2025-06-14T19:28:19.6234856Z 	updating dependency infos of liberation_fonts-2.1.5
2025-06-14T19:28:19.6235413Z 	updating dependency infos of libertine-5.3.0_2012_07_02
2025-06-14T19:28:19.6235827Z 	updating dependency infos of libetonyek-0.1.12
2025-06-14T19:28:19.6236120Z 	updating dependency infos of libetpan-1.9.4
2025-06-14T19:28:19.6236393Z 	updating dependency infos of libev-4.33
2025-06-14T19:28:19.6236664Z 	updating dependency infos of libevent-2.1.12
2025-06-14T19:28:19.6237174Z 	updating dependency infos of libexecinfo-1.1
2025-06-14T19:28:19.6237438Z 	updating dependency infos of libexif-0.6.22
2025-06-14T19:28:19.6237779Z 	libextractor-1.3 is still marked as untested on target architecture
2025-06-14T19:28:19.6238142Z 	updating dependency infos of libexttextcat-3.4.6
2025-06-14T19:28:19.6238426Z 	updating dependency infos of libffi-3.4.6
2025-06-14T19:28:19.6238692Z 	updating dependency infos of libfilezilla-0.49.0
2025-06-14T19:28:19.6238970Z 	updating dependency infos of libfm-1.3.2
2025-06-14T19:28:19.6239229Z 	updating dependency infos of libfm_extra-1.3.2
2025-06-14T19:28:19.6239499Z 	updating dependency infos of libfm_qt-1.3.0
2025-06-14T19:28:19.6239751Z 	updating dependency infos of libfmt-11.1.2
2025-06-14T19:28:19.6240007Z 	updating dependency infos of libfmt8-8.1.1
2025-06-14T19:28:19.6240269Z 	updating dependency infos of libfontenc-1.1.4
2025-06-14T19:28:19.6240551Z 	updating dependency infos of libfossil-2025.04.04
2025-06-14T19:28:19.6240836Z 	updating dependency infos of libfprint-0.7.0
2025-06-14T19:28:19.6241519Z 	updating dependency infos of libfpx-1.3.1.10
2025-06-14T19:28:19.6241835Z 	updating dependency infos of libfreehand-0.1.2
2025-06-14T19:28:19.6242128Z 	updating dependency infos of libfresample-2022.05.31
2025-06-14T19:28:19.6242414Z 	updating dependency infos of libfstrcmp-0.7
2025-06-14T19:28:19.6242665Z 	updating dependency infos of libftdi-1.5
2025-06-14T19:28:19.6242932Z 	updating dependency infos of libgcrypt-1.11.0
2025-06-14T19:28:19.6243197Z 	updating dependency infos of libgee-0.20.4
2025-06-14T19:28:19.6243451Z 	updating dependency infos of libgeotiff-1.7.1
2025-06-14T19:28:19.6243718Z 	updating dependency infos of libggz-0.99.5
2025-06-14T19:28:19.6243973Z 	updating dependency infos of libgit2_0.25-0.25.1
2025-06-14T19:28:19.6244244Z 	updating dependency infos of libgit2_1.5-1.5.0
2025-06-14T19:28:19.6244503Z 	updating dependency infos of libgit2_1.8-1.8.4
2025-06-14T19:28:19.6244821Z 	libglvnd-1.7.0 is still marked as untested on target architecture
2025-06-14T19:28:19.6245147Z 	updating dependency infos of libgnt-2.14.1
2025-06-14T19:28:19.6245541Z 	updating dependency infos of libgpg_error-1.55
2025-06-14T19:28:19.6245822Z 	updating dependency infos of libgphoto2-2.5.27
2025-06-14T19:28:19.6246086Z 	updating dependency infos of libgrapheme-2.0.2
2025-06-14T19:28:19.6246360Z 	updating dependency infos of libgravatar-23.08.5
2025-06-14T19:28:19.6246626Z 	updating dependency infos of libgsf-1.14.47
2025-06-14T19:28:19.6246895Z 	updating dependency infos of libguess-1.2_20150906
2025-06-14T19:28:19.6247166Z 	updating dependency infos of libgusb-0.4.5
2025-06-14T19:28:19.6247418Z 	updating dependency infos of libhandy-1.6.3
2025-06-14T19:28:19.6247675Z 	updating dependency infos of libhangul-0.1.0
2025-06-14T19:28:19.6247929Z 	updating dependency infos of libharu-2.4.3
2025-06-14T19:28:19.6248178Z 	updating dependency infos of libheif-1.19.8
2025-06-14T19:28:19.6248420Z 	updating dependency infos of libhx-3.26
2025-06-14T19:28:19.6248674Z 	updating dependency infos of libical-3.0.16
2025-06-14T19:28:19.6248919Z 	updating dependency infos of libice-1.0.10
2025-06-14T19:28:19.6249169Z 	updating dependency infos of libicns-0.8.1
2025-06-14T19:28:19.6249413Z 	updating dependency infos of libiconv-1.17
2025-06-14T19:28:19.6249678Z 	updating dependency infos of libid3tag-0.16.3
2025-06-14T19:28:19.6249954Z 	updating dependency infos of libidl-0.8.14
2025-06-14T19:28:19.6250207Z 	updating dependency infos of libidn-1.38
2025-06-14T19:28:19.6250460Z 	updating dependency infos of libidn2-2.0.5
2025-06-14T19:28:19.6250711Z 	updating dependency infos of libigloo-0.9.2
2025-06-14T19:28:19.6251049Z 	libimagemanip-1.1.0 is still marked as untested on target architecture
2025-06-14T19:28:19.6251606Z 	updating dependency infos of libimagequant-2.13.1
2025-06-14T19:28:19.6251955Z 	updating dependency infos of libimobiledevice_glue-1.2.0
2025-06-14T19:28:19.6252285Z 	updating dependency infos of libinstpatch-1.1.6
2025-06-14T19:28:19.6252569Z 	updating dependency infos of libiodbc-3.52.12
2025-06-14T19:28:19.6252975Z 	updating dependency infos of libiptcdata-1.0.4
2025-06-14T19:28:19.6253254Z 	updating dependency infos of libircclient-1.8
2025-06-14T19:28:19.6253539Z 	updating dependency infos of libjpeg_turbo-2.1.5.1
2025-06-14T19:28:19.6253820Z 	updating dependency infos of libjxl-0.6.1
2025-06-14T19:28:19.6254091Z 	updating dependency infos of libjxl0.11-0.11.1
2025-06-14T19:28:19.6254364Z 	updating dependency infos of libkcddb-25.04.0
2025-06-14T19:28:19.6254646Z 	updating dependency infos of libkcddb_kf6-25.04.0
2025-06-14T19:28:19.6254928Z 	updating dependency infos of libkdcraw-23.08.5
2025-06-14T19:28:19.6255205Z 	updating dependency infos of libkdcraw_kf6-25.04.0
2025-06-14T19:28:19.6255496Z 	updating dependency infos of libkdegames-23.08.5
2025-06-14T19:28:19.6255793Z 	updating dependency infos of libkdegames_kf6-25.04.0
2025-06-14T19:28:19.6256088Z 	updating dependency infos of libkdepim-23.08.5
2025-06-14T19:28:19.6256401Z 	updating dependency infos of libkeduvocdocument_kf6-25.04.0
2025-06-14T19:28:19.6256742Z 	updating dependency infos of libkexiv2-23.08.5
2025-06-14T19:28:19.6257025Z 	updating dependency infos of libkexiv2_kf6-25.04.0
2025-06-14T19:28:19.6257327Z 	updating dependency infos of libkgapi-23.08.5
2025-06-14T19:28:19.6257609Z 	updating dependency infos of libkgapi_kf6-25.04.0
2025-06-14T19:28:19.6257883Z 	updating dependency infos of libkiwix-13.1.0
2025-06-14T19:28:19.6258149Z 	updating dependency infos of libkleo-23.08.5
2025-06-14T19:28:19.6258512Z 	updating dependency infos of libkmahjongg-25.04.0
2025-06-14T19:28:19.6259082Z 	updating dependency infos of libkomparediff2-24.05.2
2025-06-14T19:28:19.6259700Z 	updating dependency infos of libkomparediff2_kf6-25.04.0
2025-06-14T19:28:19.6260018Z 	updating dependency infos of libksane-23.08.5
2025-06-14T19:28:19.6260305Z 	updating dependency infos of libksane_kf6-25.04.0
2025-06-14T19:28:19.6260583Z 	updating dependency infos of libksba-1.6.4
2025-06-14T19:28:19.6260856Z 	updating dependency infos of libksieve-23.08.5
2025-06-14T19:28:19.6261459Z 	updating dependency infos of libktorrent-2.1.1
2025-06-14T19:28:19.6261941Z 	updating dependency infos of liblangtag-0.6.3
2025-06-14T19:28:19.6262228Z 	updating dependency infos of liblastfm-1.1.0
2025-06-14T19:28:19.6262492Z 	updating dependency infos of liblayout-1.4.1
2025-06-14T19:28:19.6262748Z 	updating dependency infos of liblo-0.31
2025-06-14T19:28:19.6263004Z 	updating dependency infos of liblockfile-1.16
2025-06-14T19:28:19.6263267Z 	updating dependency infos of liblqr-0.4.2
2025-06-14T19:28:19.6263517Z 	updating dependency infos of liblrdf-0.5.0
2025-06-14T19:28:19.6263821Z 	liblxi-1.18 is still marked as broken on target architecture
2025-06-14T19:28:19.6264137Z 	updating dependency infos of libmad-0.16.4
2025-06-14T19:28:19.6264402Z 	updating dependency infos of libmatroska-1.7.1
2025-06-14T19:28:19.6264687Z 	updating dependency infos of libmatroska6-1.5.2
2025-06-14T19:28:19.6264970Z 	updating dependency infos of libmaxminddb-1.3.2
2025-06-14T19:28:19.6265258Z 	updating dependency infos of libmcrypt-2.5.8
2025-06-14T19:28:19.6265520Z 	updating dependency infos of libmd-1.1.0
2025-06-14T19:28:19.6265827Z 	libmdi-0.5 is still marked as untested on target architecture
2025-06-14T19:28:19.6266149Z 	updating dependency infos of libmediainfo-24.12
2025-06-14T19:28:19.6266428Z 	updating dependency infos of libmetalink-0.1.3
2025-06-14T19:28:19.6266714Z 	updating dependency infos of libmicrohttpd-1.0.1
2025-06-14T19:28:19.6266995Z 	updating dependency infos of libmikmod-3.3.11.1
2025-06-14T19:28:19.6267327Z 	libmirage-3.2.3 is still marked as untested on target architecture
2025-06-14T19:28:19.6267646Z 	updating dependency infos of libmkv-0.6.5.1
2025-06-14T19:28:19.6267908Z 	updating dependency infos of libmms-0.6.4
2025-06-14T19:28:19.6268154Z 	updating dependency infos of libmng-2.0.3
2025-06-14T19:28:19.6268412Z 	updating dependency infos of libmodbus-3.1.7
2025-06-14T19:28:19.6268688Z 	updating dependency infos of libmodplug-0.8.9.0
2025-06-14T19:28:19.6269068Z 	updating dependency infos of libmp4v2-2.1.1
2025-06-14T19:28:19.6269337Z 	updating dependency infos of libmpdclient-2.18
2025-06-14T19:28:19.6269599Z 	updating dependency infos of libmpeg2-0.5.1
2025-06-14T19:28:19.6269881Z 	updating dependency infos of libmspack-0.10.1~alpha
2025-06-14T19:28:19.6270159Z 	updating dependency infos of libmspub-0.1.4
2025-06-14T19:28:19.6270418Z 	updating dependency infos of libmtp-1.1.22
2025-06-14T19:28:19.6270674Z 	updating dependency infos of libmwaw-0.3.22
2025-06-14T19:28:19.6270929Z 	updating dependency infos of libmygpo_qt-1.1.0
2025-06-14T19:28:19.6271654Z 	updating dependency infos of libmypaint-1.6.1
2025-06-14T19:28:19.6271951Z 	updating dependency infos of libmysqlclient-6.1.6
2025-06-14T19:28:19.6272250Z 	updating dependency infos of libnatpmp-20150609
2025-06-14T19:28:19.6272519Z 	updating dependency infos of libnfs-5.0.2
2025-06-14T19:28:19.6272780Z 	updating dependency infos of libnice-0.1.18
2025-06-14T19:28:19.6273036Z 	updating dependency infos of libnotify-0.8.1
2025-06-14T19:28:19.6273306Z 	updating dependency infos of libnova-0.16.0
2025-06-14T19:28:19.6273571Z 	updating dependency infos of libnpupnp-5.0.1
2025-06-14T19:28:19.6273829Z 	updating dependency infos of libnsbmp-0.1.7
2025-06-14T19:28:19.6274083Z 	updating dependency infos of libnsgif-1.0.0
2025-06-14T19:28:19.6274345Z 	updating dependency infos of libnsgif0.2-0.2.1
2025-06-14T19:28:19.6274608Z 	updating dependency infos of libnslog-0.1.3
2025-06-14T19:28:19.6274862Z 	updating dependency infos of libnspsl-0.1.7
2025-06-14T19:28:19.6275123Z 	updating dependency infos of libnsutils-0.1.1
2025-06-14T19:28:19.6275405Z 	updating dependency infos of libnumbertext-1.0.6
2025-06-14T19:28:19.6275679Z 	updating dependency infos of liboauth-1.0.3
2025-06-14T19:28:19.6275942Z 	updating dependency infos of libodfgen-0.1.7
2025-06-14T19:28:19.6276201Z 	updating dependency infos of libofx-0.10.9
2025-06-14T19:28:19.6276454Z 	updating dependency infos of libogg-1.3.5
2025-06-14T19:28:19.6276705Z 	updating dependency infos of liboil-0.3.17
2025-06-14T19:28:19.6276967Z 	updating dependency infos of libopenmpt-0.7.11
2025-06-14T19:28:19.6277403Z 	updating dependency infos of libopenmpt_modplug-0.8.9.0
2025-06-14T19:28:19.6277712Z 	updating dependency infos of libopenshot-0.3.2
2025-06-14T19:28:19.6278004Z 	updating dependency infos of libopenshot_audio-0.3.2
2025-06-14T19:28:19.6278294Z 	updating dependency infos of libopusenc-0.2.1
2025-06-14T19:28:19.6278564Z 	updating dependency infos of liborigin-3.0.3
2025-06-14T19:28:19.6278817Z 	updating dependency infos of libotr-4.1.1
2025-06-14T19:28:19.6279072Z 	updating dependency infos of libp11-0.4.10
2025-06-14T19:28:19.6279347Z 	updating dependency infos of libp8_platform-2.1.0.1
2025-06-14T19:28:19.6279638Z 	updating dependency infos of libpagemaker-0.0.4
2025-06-14T19:28:19.6279918Z 	updating dependency infos of libpaper2-2.2.6
2025-06-14T19:28:19.6280193Z 	updating dependency infos of libparserutils-0.2.5
2025-06-14T19:28:19.6280477Z 	updating dependency infos of libpcap-1.10.5
2025-06-14T19:28:19.6280750Z 	updating dependency infos of libpciaccess-0.18.1
2025-06-14T19:28:19.6281028Z 	updating dependency infos of libpcre-8.45
2025-06-14T19:28:19.6281402Z 	updating dependency infos of libpcre0-8.21
2025-06-14T19:28:19.6281661Z 	updating dependency infos of libpcre2-10.45
2025-06-14T19:28:19.6281917Z 	updating dependency infos of libpeas-1.34.0
2025-06-14T19:28:19.6282167Z 	updating dependency infos of libpgf-7.21.7
2025-06-14T19:28:19.6282424Z 	updating dependency infos of libpinyin-2.8.1
2025-06-14T19:28:19.6282690Z 	updating dependency infos of libpipeline-1.5.3
2025-06-14T19:28:19.6282968Z 	updating dependency infos of libplacebo-7.349.0
2025-06-14T19:28:19.6283233Z 	updating dependency infos of libplist-2.4.0
2025-06-14T19:28:19.6283486Z 	recipe for libpng12-1.2.59 is still broken:
2025-06-14T19:28:19.6283814Z 	Error: package libpng12-1.2.59 cannot be built for architecture x86_64
2025-06-14T19:28:19.6284169Z 	updating dependency infos of libpng16-1.6.44
2025-06-14T19:28:19.6284554Z 	updating dependency infos of libportal-0.6
2025-06-14T19:28:19.6284831Z 	updating dependency infos of libpostproc-10~20172510
2025-06-14T19:28:19.6285120Z 	updating dependency infos of libprefs-1.2.5
2025-06-14T19:28:19.6285369Z 	updating dependency infos of libpsl-0.21.5
2025-06-14T19:28:19.6580592Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:21.1278907Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:21.1291733Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:21.1305191Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:21.1319095Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:22.0759446Z 	updating dependency infos of libpthread_stubs-0.4
2025-06-14T19:28:22.0760043Z 	updating dependency infos of libpurple-2.14.13
2025-06-14T19:28:22.0760553Z 	updating dependency infos of libqalculate-5.5.2
2025-06-14T19:28:22.0761270Z 	updating dependency infos of libqt5pas-1.2.16
2025-06-14T19:28:22.0761780Z 	updating dependency infos of libqt6pas-6.2.10
2025-06-14T19:28:22.0762256Z 	updating dependency infos of libquicktime-1.2.4
2025-06-14T19:28:22.0762765Z 	updating dependency infos of libquotient_qt5-0.8.2
2025-06-14T19:28:22.0763087Z 	updating dependency infos of libquotient_qt6-0.9.3
2025-06-14T19:28:22.0763383Z 	updating dependency infos of libqxp-0.0.2
2025-06-14T19:28:22.0763643Z 	updating dependency infos of libraqm-0.3.0
2025-06-14T19:28:22.0763903Z 	updating dependency infos of libraw-0.20.2
2025-06-14T19:28:22.0764182Z 	updating dependency infos of libraw19-0.19.5
2025-06-14T19:28:22.0764463Z 	updating dependency infos of librecad-2.2.0
2025-06-14T19:28:22.0764750Z 	updating dependency infos of libreoffice-24.8.1.1
2025-06-14T19:28:22.0765028Z 	updating dependency infos of librepcb-0.1.7
2025-06-14T19:28:22.0765299Z 	updating dependency infos of libreplaygain-475
2025-06-14T19:28:22.0765593Z 	updating dependency infos of libresprite-1.1~git
2025-06-14T19:28:22.0766106Z 	updating dependency infos of librevenge-0.0.5
2025-06-14T19:28:22.0766455Z 	librewolf-139.0.1 is still marked as broken on target architecture
2025-06-14T19:28:22.0766805Z 	updating dependency infos of librewolf_bin-139.0.1
2025-06-14T19:28:22.0767085Z 	updating dependency infos of librnp-0.17.0
2025-06-14T19:28:22.0767338Z 	updating dependency infos of librsb-1.2.0.9
2025-06-14T19:28:22.0767595Z 	updating dependency infos of librsvg-2.50.7
2025-06-14T19:28:22.0767844Z 	updating dependency infos of librsync-2.3.4
2025-06-14T19:28:22.0768110Z 	updating dependency infos of librsync2.0-2.0.0
2025-06-14T19:28:22.0768378Z 	updating dependency infos of librttopo-1.1.0
2025-06-14T19:28:22.0768690Z 	libs3-2.0 is still marked as untested on target architecture
2025-06-14T19:28:22.0769019Z 	updating dependency infos of libsamplerate-0.2.2
2025-06-14T19:28:22.0769289Z 	updating dependency infos of libsanta-3.0.2
2025-06-14T19:28:22.0769552Z 	updating dependency infos of libsass-3.6.6
2025-06-14T19:28:22.0769808Z 	updating dependency infos of libsbsms-2.3.0
2025-06-14T19:28:22.0770068Z 	updating dependency infos of libsdl-1.2.15
2025-06-14T19:28:22.0770319Z 	updating dependency infos of libsdl2-2.30.10
2025-06-14T19:28:22.0770580Z 	updating dependency infos of libsdl3-3.2.8
2025-06-14T19:28:22.0770868Z 	updating dependency infos of libsecp256k1-20200327~git
2025-06-14T19:28:22.0771377Z 	updating dependency infos of libsecret-0.21.7
2025-06-14T19:28:22.0771654Z 	updating dependency infos of libshout-2.4.5
2025-06-14T19:28:22.0771920Z 	updating dependency infos of libsidplayfp-2.1.2
2025-06-14T19:28:22.0772226Z 	updating dependency infos of libsigc++-2.9.3
2025-06-14T19:28:22.0772493Z 	updating dependency infos of libsigc++3-3.0.3
2025-06-14T19:28:22.0772753Z 	updating dependency infos of libsigrok-0.5.2
2025-06-14T19:28:22.0773040Z 	updating dependency infos of libsigrokdecode-0.5.3
2025-06-14T19:28:22.0773471Z 	updating dependency infos of libsigsegv-2.14
2025-06-14T19:28:22.0773726Z 	updating dependency infos of libslirp-4.7.0
2025-06-14T19:28:22.0773994Z 	updating dependency infos of libslz-1.1.0
2025-06-14T19:28:22.0774246Z 	updating dependency infos of libsm-1.2.3
2025-06-14T19:28:22.0774501Z 	updating dependency infos of libsmb2-4.0.0
2025-06-14T19:28:22.0774761Z 	updating dependency infos of libsmdev-20170225
2025-06-14T19:28:22.0775028Z 	updating dependency infos of libsmf-1.3
2025-06-14T19:28:22.0775285Z 	updating dependency infos of libsndfile-1.2.2
2025-06-14T19:28:22.0775558Z 	updating dependency infos of libsodium-1.0.18
2025-06-14T19:28:22.0775871Z 	updating dependency infos of libsolv-0.3.0_haiku_2014_12_22
2025-06-14T19:28:22.0776188Z 	updating dependency infos of libsoundtouch-2.1.2
2025-06-14T19:28:22.0776468Z 	updating dependency infos of libsoup-2.60.2
2025-06-14T19:28:22.0776717Z 	updating dependency infos of libsoup3-3.2.2
2025-06-14T19:28:22.0776994Z 	updating dependency infos of libspatialindex-1.9.3
2025-06-14T19:28:22.0777282Z 	updating dependency infos of libspectre-0.2.12
2025-06-14T19:28:22.0777568Z 	updating dependency infos of libspectrum-1.4.4
2025-06-14T19:28:22.0777853Z 	updating dependency infos of libspiro-20220722
2025-06-14T19:28:22.0778147Z 	updating dependency infos of libspiro0-20180219~git
2025-06-14T19:28:22.0778439Z 	updating dependency infos of libspng-0.7.4
2025-06-14T19:28:22.0778699Z 	updating dependency infos of libsquish-1.15
2025-06-14T19:28:22.0778963Z 	updating dependency infos of libsrtp-1.5.4
2025-06-14T19:28:22.0779216Z 	updating dependency infos of libsrtp2-2.5.0
2025-06-14T19:28:22.0779474Z 	updating dependency infos of libssh-0.10.5
2025-06-14T19:28:22.0779719Z 	updating dependency infos of libssh2-1.11.1
2025-06-14T19:28:22.0779992Z 	updating dependency infos of libstaroffice-0.0.7
2025-06-14T19:28:22.0780294Z 	updating dependency infos of libsunpinyin-3.0.0~rc2
2025-06-14T19:28:22.0780581Z 	updating dependency infos of libsvgtiny-0.1.8
2025-06-14T19:28:22.0780851Z 	updating dependency infos of libsvm-3.35
2025-06-14T19:28:22.0781261Z 	updating dependency infos of libtar-1.2.20
2025-06-14T19:28:22.0781947Z 	updating dependency infos of libtasn1-4.19.0
2025-06-14T19:28:22.0782444Z 	updating dependency infos of libtermkey-0.22
2025-06-14T19:28:22.0782856Z 	updating dependency infos of libthai-0.1.29
2025-06-14T19:28:22.0783117Z 	updating dependency infos of libtheora-1.1.1
2025-06-14T19:28:22.0783394Z 	updating dependency infos of libtimidity-0.2.7
2025-06-14T19:28:22.0783669Z 	updating dependency infos of libtirpc-1.3.2
2025-06-14T19:28:22.0783936Z 	updating dependency infos of libtomcrypt-1.18.2
2025-06-14T19:28:22.0784226Z 	updating dependency infos of libtommath-1.2.0
2025-06-14T19:28:22.0784492Z 	updating dependency infos of libtool-2.4.7
2025-06-14T19:28:22.0784765Z 	updating dependency infos of libtorrent-0.13.8
2025-06-14T19:28:22.0785072Z 	updating dependency infos of libtorrent_rasterbar-1.2.3
2025-06-14T19:28:22.0785379Z 	updating dependency infos of libtxc_dxtn-1.0.1
2025-06-14T19:28:22.0785666Z 	updating dependency infos of libu2f_host-1.1.10
2025-06-14T19:28:22.0785949Z 	updating dependency infos of libu2f_server-1.1.0
2025-06-14T19:28:22.0786225Z 	updating dependency infos of libucl-0.9.2
2025-06-14T19:28:22.0786487Z 	updating dependency infos of libunibreak-5.1
2025-06-14T19:28:22.0786763Z 	updating dependency infos of libunibreak4.0-4.0
2025-06-14T19:28:22.0787039Z 	updating dependency infos of libunistring-1.2
2025-06-14T19:28:22.0787314Z 	updating dependency infos of libunistring2-1.0
2025-06-14T19:28:22.0787581Z 	updating dependency infos of libupnp-1.14.17
2025-06-14T19:28:22.0787854Z 	updating dependency infos of libupnp15-1.10.1
2025-06-14T19:28:22.0788121Z 	updating dependency infos of libusb-1.0.26
2025-06-14T19:28:22.0788388Z 	updating dependency infos of libusb_compat-0.1.7
2025-06-14T19:28:22.0788672Z 	updating dependency infos of libusbmuxd-2.1.0
2025-06-14T19:28:22.0788943Z 	updating dependency infos of libutf8proc2-2.5.0
2025-06-14T19:28:22.0789345Z 	updating dependency infos of libuuid-1.3.1
2025-06-14T19:28:22.0789597Z 	updating dependency infos of libuv-1.48.0
2025-06-14T19:28:22.0789860Z 	updating dependency infos of libvirt-8.10.0
2025-06-14T19:28:22.0790125Z 	updating dependency infos of libvirt_glib-4.0.0
2025-06-14T19:28:22.0790395Z 	updating dependency infos of libvisio-0.1.7
2025-06-14T19:28:22.0790667Z 	updating dependency infos of libvncserver-0.9.13
2025-06-14T19:28:22.0790945Z 	updating dependency infos of libvorbis-1.3.7
2025-06-14T19:28:22.0791600Z 	updating dependency infos of libvpx-1.13.1
2025-06-14T19:28:22.0791872Z 	updating dependency infos of libvpx1.11-1.11.0
2025-06-14T19:28:22.0792212Z 	libvterm-0.0.681 is still marked as untested on target architecture
2025-06-14T19:28:22.0792548Z 	updating dependency infos of libwalter-102
2025-06-14T19:28:22.0792913Z 	updating dependency infos of libwapcaplet-0.4.3
2025-06-14T19:28:22.0793197Z 	updating dependency infos of libwebm-1.0.0.27
2025-06-14T19:28:22.0793457Z 	updating dependency infos of libwebp-1.5.0
2025-06-14T19:28:22.0793735Z 	updating dependency infos of libwebsockets-4.3.3
2025-06-14T19:28:22.0794006Z 	updating dependency infos of libwmf-0.2.12
2025-06-14T19:28:22.0794262Z 	updating dependency infos of libwpd-0.10.3
2025-06-14T19:28:22.0794510Z 	updating dependency infos of libwpg-0.3.4
2025-06-14T19:28:22.0794763Z 	updating dependency infos of libwps-0.4.14
2025-06-14T19:28:22.0795016Z 	updating dependency infos of libwww_perl-6.77
2025-06-14T19:28:22.0795276Z 	updating dependency infos of libx11-1.6.9
2025-06-14T19:28:22.0795526Z 	updating dependency infos of libxau-1.0.9
2025-06-14T19:28:22.0795769Z 	updating dependency infos of libxaw-1.0.14
2025-06-14T19:28:22.0796017Z 	updating dependency infos of libxcb-1.13.1
2025-06-14T19:28:22.0796314Z 	libxcm-0.5.4 is still marked as untested on target architecture
2025-06-14T19:28:22.0796707Z 	libxcomposite-0.4.5 is still marked as untested on target architecture
2025-06-14T19:28:22.0797051Z 	updating dependency infos of libxcrypt-4.4.38
2025-06-14T19:28:22.0797385Z 	libxcursor-1.2.0 is still marked as untested on target architecture
2025-06-14T19:28:22.0797891Z 	libxdamage-1.1.5 is still marked as untested on target architecture
2025-06-14T19:28:22.0798234Z 	updating dependency infos of libxdg_basedir-1.2.0
2025-06-14T19:28:22.0798517Z 	updating dependency infos of libxdmcp-1.1.4
2025-06-14T19:28:22.0798823Z 	libxext-1.3.4 is still marked as untested on target architecture
2025-06-14T19:28:22.0799201Z 	libxfixes-5.0.3 is still marked as untested on target architecture
2025-06-14T19:28:22.0799523Z 	updating dependency infos of libxfont-1.5.4
2025-06-14T19:28:22.0799787Z 	updating dependency infos of libxfont2-2.0.5
2025-06-14T19:28:22.0800090Z 	libxft-2.3.3 is still marked as untested on target architecture
2025-06-14T19:28:22.0800440Z 	libxi-1.7.10 is still marked as untested on target architecture
2025-06-14T19:28:22.0800811Z 	libxinerama-1.1.4 is still marked as untested on target architecture
2025-06-14T19:28:22.0801351Z 	updating dependency infos of libxkbcommon-1.7.0
2025-06-14T19:28:22.0801707Z 	libxkbfile-1.1.0 is still marked as untested on target architecture
2025-06-14T19:28:22.0802036Z 	updating dependency infos of libxml++2-2.42.3
2025-06-14T19:28:22.0802308Z 	updating dependency infos of libxml++5-5.4.0
2025-06-14T19:28:22.0802566Z 	updating dependency infos of libxml2-2.12.10
2025-06-14T19:28:22.0802827Z 	updating dependency infos of libxmp-4.6.0
2025-06-14T19:28:22.0803082Z 	updating dependency infos of libxmu-1.1.3
2025-06-14T19:28:22.0803326Z 	updating dependency infos of libxo-1.6.0
2025-06-14T19:28:22.0803600Z 	updating dependency infos of libxpm-3.5.12
2025-06-14T19:28:22.0804097Z 	libxrandr-1.5.2 is still marked as untested on target architecture
2025-06-14T19:28:22.0804485Z 	libxrender-0.9.10 is still marked as untested on target architecture
2025-06-14T19:28:22.0804888Z 	libxscrnsaver-1.2.3 is still marked as untested on target architecture
2025-06-14T19:28:22.0805221Z 	updating dependency infos of libxslt-1.1.43
2025-06-14T19:28:22.0805613Z 	updating dependency infos of libxt-1.2.0
2025-06-14T19:28:22.0805926Z 	libxtst-1.2.3 is still marked as untested on target architecture
2025-06-14T19:28:22.0806235Z 	updating dependency infos of libyajl-2.1.0
2025-06-14T19:28:22.0806490Z 	updating dependency infos of libyaml-0.2.5
2025-06-14T19:28:22.0806744Z 	updating dependency infos of libyubikey-1.13
2025-06-14T19:28:22.0807006Z 	updating dependency infos of libzen-0.4.41
2025-06-14T19:28:22.0807252Z 	updating dependency infos of libzim-9.2.3
2025-06-14T19:28:22.0807505Z 	updating dependency infos of libzip-1.9.2
2025-06-14T19:28:22.0807747Z 	updating dependency infos of libzmf-0.0.2
2025-06-14T19:28:22.0807998Z 	updating dependency infos of lightsoff-1.1
2025-06-14T19:28:22.0808257Z 	updating dependency infos of lighttpd-1.4.53
2025-06-14T19:28:22.0808509Z 	updating dependency infos of lilv-0.24.20
2025-06-14T19:28:22.0808763Z 	updating dependency infos of lilypond-2.24.4
2025-06-14T19:28:22.0809013Z 	updating dependency infos of limine-9.3.2
2025-06-14T19:28:22.0809281Z 	updating dependency infos of linaro_qemu-2014.01
2025-06-14T19:28:22.0809563Z 	updating dependency infos of lincity_ng-2.9~git
2025-06-14T19:28:22.0809901Z 	linenoise-1.0~git is still marked as untested on target architecture
2025-06-14T19:28:22.0810224Z 	updating dependency infos of lingua-2.0.0
2025-06-14T19:28:22.0810487Z 	updating dependency infos of lingua_translit-0.29
2025-06-14T19:28:22.0810762Z 	updating dependency infos of links-2.30
2025-06-14T19:28:22.0811004Z 	updating dependency infos of lis-2.0.17
2025-06-14T19:28:23.9228626Z 	updating dependency infos of list_allutils-0.19
2025-06-14T19:28:23.9229212Z 	updating dependency infos of list_moreutils-0.430
2025-06-14T19:28:23.9229644Z 	updating dependency infos of list_moreutils_xs-0.430
2025-06-14T19:28:23.9229963Z 	updating dependency infos of list_someutils-0.59
2025-06-14T19:28:23.9230269Z 	updating dependency infos of list_someutils_xs-0.58
2025-06-14T19:28:23.9230574Z 	updating dependency infos of list_utilsby-0.12
2025-06-14T19:28:23.9230876Z 	updating dependency infos of litehtml-0.9
2025-06-14T19:28:23.9231585Z 	updating dependency infos of live555-2016.06.22
2025-06-14T19:28:23.9231877Z 	updating dependency infos of lizard-1.0
2025-06-14T19:28:23.9232145Z 	updating dependency infos of llama_cpp-b4889
2025-06-14T19:28:23.9232411Z 	updating dependency infos of llvm12-12.0.1
2025-06-14T19:28:23.9232694Z 	updating dependency infos of llvm16-16.0.6
2025-06-14T19:28:23.9232942Z 	updating dependency infos of llvm17-17.0.6
2025-06-14T19:28:23.9233188Z 	updating dependency infos of llvm18-18.1.7
2025-06-14T19:28:23.9233426Z 	updating dependency infos of llvm19-19.1.7
2025-06-14T19:28:23.9233672Z 	updating dependency infos of llvm20-20.1.4
2025-06-14T19:28:23.9233918Z 	updating dependency infos of lm4tools-0.1.3
2025-06-14T19:28:23.9234178Z 	updating dependency infos of lmarbles-1.0.8
2025-06-14T19:28:23.9234430Z 	updating dependency infos of lmdb-0.9.29
2025-06-14T19:28:23.9234676Z 	updating dependency infos of lmdbxx-1.0.0
2025-06-14T19:28:23.9234935Z 	updating dependency infos of lmms-1.2.2
2025-06-14T19:28:23.9235196Z 	updating dependency infos of lnlauncher-1.1.2
2025-06-14T19:28:23.9235523Z 	loadpng-1.5 is still marked as untested on target architecture
2025-06-14T19:28:23.9235880Z 	updating dependency infos of locale_maketext_lexicon-1.00
2025-06-14T19:28:23.9236264Z 	lockworkstation-0.99 is still marked as untested on target architecture
2025-06-14T19:28:23.9236614Z 	updating dependency infos of log4cxx-1.3.1
2025-06-14T19:28:23.9236877Z 	updating dependency infos of log_log4perl-1.57
2025-06-14T19:28:23.9237147Z 	updating dependency infos of lohit-2.3.8
2025-06-14T19:28:23.9237397Z 	updating dependency infos of lout-3.43
2025-06-14T19:28:23.9237640Z 	updating dependency infos of love-11.5
2025-06-14T19:28:23.9237879Z 	updating dependency infos of lpairs-1.0.5
2025-06-14T19:28:23.9238131Z 	updating dependency infos of lpeg-1.0.2
2025-06-14T19:28:23.9238374Z 	updating dependency infos of lpeg1.1-1.1.0
2025-06-14T19:28:23.9238800Z 	updating dependency infos of lpsolve-5.5.2.5
2025-06-14T19:28:23.9239068Z 	updating dependency infos of lrzip-0.631
2025-06-14T19:28:23.9239312Z 	updating dependency infos of lrzsz-0.12.20
2025-06-14T19:28:23.9239559Z 	updating dependency infos of lsdvd-0.17
2025-06-14T19:28:23.9239797Z 	updating dependency infos of lskat-25.04.0
2025-06-14T19:28:23.9240038Z 	recipe for ltp-20140422 is still broken:
2025-06-14T19:28:23.9240346Z 	Error: package ltp-20140422 cannot be built for architecture x86_64
2025-06-14T19:28:23.9240691Z 	updating dependency infos of ltris-1.0.19
2025-06-14T19:28:23.9240933Z 	updating dependency infos of lua-5.4.7
2025-06-14T19:28:23.9241355Z 	updating dependency infos of lua5.1-5.1.5
2025-06-14T19:28:23.9241600Z 	updating dependency infos of lua5.2-5.2.4
2025-06-14T19:28:23.9241838Z 	updating dependency infos of lua5.3-5.3.6
2025-06-14T19:28:23.9242083Z 	updating dependency infos of luabind-0.9.1
2025-06-14T19:28:23.9242338Z 	updating dependency infos of luacheck-0.21.0
2025-06-14T19:28:23.9242624Z 	updating dependency infos of luafilesystem-1.8.0
2025-06-14T19:28:23.9242917Z 	updating dependency infos of luajit-2.1.1727870382
2025-06-14T19:28:23.9243203Z 	updating dependency infos of luarocks-3.11.1
2025-06-14T19:28:23.9243475Z 	updating dependency infos of luckybackup-0.5.0
2025-06-14T19:28:23.9243734Z 	updating dependency infos of lugaru-1.2
2025-06-14T19:28:23.9244006Z 	updating dependency infos of luminance_hdr-2.6.1.1
2025-06-14T19:28:23.9244274Z 	updating dependency infos of lutok-0.4
2025-06-14T19:28:23.9244518Z 	updating dependency infos of luv-1.48.0_2
2025-06-14T19:28:23.9244759Z 	updating dependency infos of lv2-1.18.10
2025-06-14T19:28:23.9245028Z 	updating dependency infos of lwp_mediatypes-6.04
2025-06-14T19:28:23.9245329Z 	updating dependency infos of lwp_protocol_https-6.14
2025-06-14T19:28:23.9245622Z 	updating dependency infos of lwtools-4.22
2025-06-14T19:28:23.9245873Z 	updating dependency infos of lxml-5.3.0
2025-06-14T19:28:23.9246150Z 	updating dependency infos of lxqt_build_tools-0.13.0
2025-06-14T19:28:23.9246438Z 	updating dependency infos of lynx-2.8.9rel.1
2025-06-14T19:28:23.9246809Z 	updating dependency infos of lyx-2.3.7_1
2025-06-14T19:28:23.9247060Z 	updating dependency infos of lz4-1.9.4
2025-06-14T19:28:23.9247299Z 	updating dependency infos of lzip-1.23
2025-06-14T19:28:23.9247540Z 	updating dependency infos of lzo-2.10
2025-06-14T19:28:23.9247776Z 	updating dependency infos of lzop-1.04
2025-06-14T19:28:23.9248010Z 	updating dependency infos of m4-1.4.19
2025-06-14T19:28:23.9248271Z 	updating dependency infos of m68k_elf_binutils-2.44
2025-06-14T19:28:23.9248559Z 	updating dependency infos of m68k_elf_gcc-13.1.0
2025-06-14T19:28:23.9248830Z 	updating dependency infos of m_tx-0.63d
2025-06-14T19:28:23.9249069Z 	updating dependency infos of mac-9.20
2025-06-14T19:28:23.9249323Z 	updating dependency infos of maelstrom-3.0.6
2025-06-14T19:28:23.9249585Z 	updating dependency infos of maeparser-1.2.3
2025-06-14T19:28:23.9249862Z 	updating dependency infos of mailnews-2.0.0.25
2025-06-14T19:28:23.9250121Z 	updating dependency infos of make-4.4.1
2025-06-14T19:28:23.9250385Z 	updating dependency infos of makedepend-1.0.6
2025-06-14T19:28:23.9250674Z 	updating dependency infos of makeheaders-20181102
2025-06-14T19:28:23.9250949Z 	updating dependency infos of makeobj-60.2
2025-06-14T19:28:23.9251369Z 	updating dependency infos of mako-1.3.5
2025-06-14T19:28:23.9251608Z 	updating dependency infos of mame-0.277
2025-06-14T19:28:23.9251919Z 	updating dependency infos of mame2003_plus_libretro-1.0_20250420
2025-06-14T19:28:23.9252279Z 	man-1.6g is still marked as broken on target architecture
2025-06-14T19:28:23.9252597Z 	updating dependency infos of man_pages_posix-2013.a
2025-06-14T19:28:23.9252999Z 	updating dependency infos of manaplus-1.8.4.14
2025-06-14T19:28:23.9253498Z 	updating dependency infos of mandoc-1.14.3
2025-06-14T19:28:23.9253973Z 	updating dependency infos of manifold-3.0.1
2025-06-14T19:28:23.9254336Z 	updating dependency infos of maps-1.0
2025-06-14T19:28:23.9254781Z 	updating dependency infos of marble-24.08.0
2025-06-14T19:28:23.9255137Z 	updating dependency infos of mariadb-11.7.2
2025-06-14T19:28:23.9255394Z 	updating dependency infos of marisa-0.2.6
2025-06-14T19:28:23.9255726Z 	updating dependency infos of markdown-3.1.1
2025-06-14T19:28:23.9256014Z 	updating dependency infos of markdown_math-0.8
2025-06-14T19:28:23.9256305Z 	updating dependency infos of markdownpart-23.08.5
2025-06-14T19:28:23.9256613Z 	updating dependency infos of markdownpart_kf6-25.04.0
2025-06-14T19:28:23.9256902Z 	updating dependency infos of marknote-1.3.0
2025-06-14T19:28:23.9257158Z 	updating dependency infos of markups-3.1.3
2025-06-14T19:28:23.9257428Z 	updating dependency infos of markupsafe-2.1.3
2025-06-14T19:28:23.9257761Z 	masterpiece-r742 is still marked as untested on target architecture
2025-06-14T19:28:23.9258186Z 	matching_columns-0.1.0~git is still marked as untested on target architecture
2025-06-14T19:28:23.9258590Z 	mathfu-1.0.2 is still marked as untested on target architecture
2025-06-14T19:28:23.9258911Z 	updating dependency infos of matio-1.5.26
2025-06-14T19:28:23.9259186Z 	updating dependency infos of matplotlib-3.7.2
2025-06-14T19:28:23.9259463Z 	updating dependency infos of mawk-1.3.4_20231126
2025-06-14T19:28:23.9259739Z 	updating dependency infos of maxima-5.47.0
2025-06-14T19:28:23.9259991Z 	updating dependency infos of mbedtls-2.28.9
2025-06-14T19:28:23.9260275Z 	updating dependency infos of mc-4.8.32
2025-06-14T19:28:23.9260524Z 	updating dependency infos of mcrypt-2.6.8
2025-06-14T19:28:23.9260775Z 	updating dependency infos of md4c-0.5.2
2025-06-14T19:28:23.9261032Z 	updating dependency infos of mda_vst-20150618
2025-06-14T19:28:23.9261564Z 	updating dependency infos of mdate-1.7.0.3
2025-06-14T19:28:23.9261820Z 	updating dependency infos of mdds-1.5.0
2025-06-14T19:28:23.9262061Z 	updating dependency infos of mdds14-1.4.3
2025-06-14T19:28:23.9262315Z 	updating dependency infos of mdds2-2.0.1
2025-06-14T19:28:23.9262572Z 	updating dependency infos of mdds2.1-2.1.1
2025-06-14T19:28:23.9263017Z 	mdf2iso-0.3.1 is still marked as untested on target architecture
2025-06-14T19:28:23.9263387Z 	updating dependency infos of mdnsresponder-2200.140.11
2025-06-14T19:28:23.9263688Z 	recipe for mdocml-1.12.2 is still broken:
2025-06-14T19:28:23.9264013Z 	Error: package mdocml-1.12.2 cannot be built for architecture x86_64
2025-06-14T19:28:23.9264341Z 	updating dependency infos of mdp-1.0.15
2025-06-14T19:28:23.9264605Z 	updating dependency infos of mechanize-0.4.8
2025-06-14T19:28:23.9264877Z 	updating dependency infos of media_helpers-0.1
2025-06-14T19:28:23.9265154Z 	updating dependency infos of mediainfo-24.12
2025-06-14T19:28:23.9265418Z 	updating dependency infos of mednafen-1.29.0
2025-06-14T19:28:23.9265747Z 	updating dependency infos of mednafen_gba_libretro-0.9.36_20241021
2025-06-14T19:28:23.9266145Z 	updating dependency infos of mednafen_lynx_libretro-0.9.32_20241021
2025-06-14T19:28:23.9266541Z 	updating dependency infos of mednafen_ngp_libretro-0.9.36.1_20241021
2025-06-14T19:28:23.9266965Z 	updating dependency infos of mednafen_pce_fast_libretro-0.9.38.7_20250418
2025-06-14T19:28:23.9267380Z 	updating dependency infos of mednafen_pce_libretro-0.9.38.7_20241115
2025-06-14T19:28:23.9267779Z 	updating dependency infos of mednafen_pcfx_libretro-0.9.33.3_20241021
2025-06-14T19:28:23.9268176Z 	updating dependency infos of mednafen_psx_hw_libretro-0.9.44.1_20250418
2025-06-14T19:28:23.9268577Z 	updating dependency infos of mednafen_psx_libretro-0.9.44.1_20250418
2025-06-14T19:28:23.9268988Z 	updating dependency infos of mednafen_saturn_libretro-0.9.45.1_20250317
2025-06-14T19:28:23.9269416Z 	updating dependency infos of mednafen_supergrafx_libretro-0.9.38.7_20241115
2025-06-14T19:28:23.9269840Z 	updating dependency infos of mednafen_vb_libretro-0.9.36.1_20241021
2025-06-14T19:28:23.9270239Z 	updating dependency infos of mednafen_wswan_libretro-0.9.35.1_20241021
2025-06-14T19:28:23.9270586Z 	updating dependency infos of mednaffe-0.9.2
2025-06-14T19:28:23.9270966Z 	updating dependency infos of medo-1.0.0~beta1.5
2025-06-14T19:28:23.9271551Z 	updating dependency infos of melonds-0.9.5
2025-06-14T19:28:23.9271867Z 	updating dependency infos of melonds_libretro-0.8.3_20241021
2025-06-14T19:28:23.9272215Z 	melt-1.3.0 is still marked as broken on target architecture
2025-06-14T19:28:23.9272517Z 	recipe for memochip-1.3~git is still broken:
2025-06-14T19:28:23.9272768Z 	Error: No match found for license unknown
2025-06-14T19:28:23.9273054Z 	Error: Valid license filenames included with Haiku are:
2025-06-14T19:28:23.9274659Z 	Error: Anti-Grain Geometry, Apache v2, Artistic, Artistic v2.0, BSD (2-clause), BSD (3-clause), BSD (4-clause), Be Sample Code License, Bullet, CDDL v1, CQuantizer, DEC, GLUT (Mark Kilgard), GNU GPL font exception, GNU GPL v1, GNU GPL v2, GNU GPL v3, GNU LGPL v2, GNU LGPL v2.1, GNU LGPL v3, GPC, Intel (2xxx firmware), Intel (ACPICA), Intel (firmware), LibHTTPd, LibJPEG, LibPNG, MAPM, MIT, MIT (no promotion), MPL v1.1, MPL v2.0, Marvell (firmware), OpenGroup, PDFlib Lite, Public Domain, Ralink (firmware), SGI Free B, SIL Open Font License v1.1, Zlib
2025-06-14T19:28:23.9276399Z 	Error: (in /runner/work/haikuports/haikuports/haiku-apps/memochip/memochip-1.3~git.recipe)
2025-06-14T19:28:23.9276850Z 	updating dependency infos of menu_cache-1.1.0
2025-06-14T19:28:23.9277128Z 	updating dependency infos of mercurial-6.5.2
2025-06-14T19:28:23.9277430Z 	mesa-24.1.4 is still marked as untested on target architecture
2025-06-14T19:28:23.9277780Z 	mesa-23.1.9 is still marked as untested on target architecture
2025-06-14T19:28:23.9278075Z 	updating dependency infos of mesa-22.0.5
2025-06-14T19:28:23.9278376Z 	updating dependency infos of mesen_libretro-0.9.4_20241021
2025-06-14T19:28:23.9278682Z 	updating dependency infos of meson-1.6.0
2025-06-14T19:28:23.9278946Z 	updating dependency infos of meson_python-0.16.0
2025-06-14T19:28:25.0331770Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:25.0345069Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:25.9165805Z 	updating dependency infos of messagelib-23.08.5
2025-06-14T19:28:25.9166514Z 	updating dependency infos of meta_portsfile-1
2025-06-14T19:28:25.9167115Z 	updating dependency infos of meteor_libretro-1.4_20201228
2025-06-14T19:28:25.9167698Z 	recipe for mev-0.9.0 is still broken:
2025-06-14T19:28:25.9168275Z 	Error: package mev-0.9.0 cannot be built for architecture x86_64
2025-06-14T19:28:25.9168836Z 	updating dependency infos of mg-7.3
2025-06-14T19:28:25.9169284Z 	updating dependency infos of mgba-0.10.2
2025-06-14T19:28:25.9169840Z 	updating dependency infos of mgba_libretro-0.6.1_20250218
2025-06-14T19:28:25.9170401Z 	updating dependency infos of mhash-0.9.9.9
2025-06-14T19:28:25.9170960Z 	updating dependency infos of microbe-20130728
2025-06-14T19:28:25.9171687Z 	updating dependency infos of midikeyboard-1.0.0
2025-06-14T19:28:25.9172236Z 	updating dependency infos of midisynth-1.8.1
2025-06-14T19:28:25.9172780Z 	updating dependency infos of mightymike-3.0.1
2025-06-14T19:28:25.9173296Z 	updating dependency infos of mikmod-3.2.8
2025-06-14T19:28:25.9173811Z 	updating dependency infos of milkytracker-1.05.01
2025-06-14T19:28:25.9174347Z 	updating dependency infos of mimalloc-2.1.2
2025-06-14T19:28:25.9174867Z 	updating dependency infos of mime_charset-1.013.1
2025-06-14T19:28:25.9175386Z 	updating dependency infos of mimetic-0.9.8
2025-06-14T19:28:25.9175899Z 	updating dependency infos of minesweeper-20150109
2025-06-14T19:28:25.9176409Z 	updating dependency infos of minetest-5.9.1
2025-06-14T19:28:25.9176895Z 	updating dependency infos of minicom-2.7.1
2025-06-14T19:28:25.9177368Z 	updating dependency infos of minidlna-1.3.3
2025-06-14T19:28:25.9177876Z 	updating dependency infos of minimizeall-1.0.0
2025-06-14T19:28:25.9178378Z 	updating dependency infos of minipro-0.7
2025-06-14T19:28:25.9178850Z 	updating dependency infos of minisign-0.11
2025-06-14T19:28:25.9179347Z 	updating dependency infos of miniupnpc-2.2.7
2025-06-14T19:28:25.9180131Z 	updating dependency infos of minizip-1.3
2025-06-14T19:28:25.9180645Z 	updating dependency infos of minizip_ng-4.0.7
2025-06-14T19:28:25.9181594Z 	updating dependency infos of minuet-25.04.0
2025-06-14T19:28:25.9182221Z 	mirage2iso-0.4.2 is still marked as untested on target architecture
2025-06-14T19:28:25.9182843Z 	updating dependency infos of mirrormagic-3.0.0
2025-06-14T19:28:25.9183364Z 	updating dependency infos of mjpegtools-2.2.1
2025-06-14T19:28:25.9183856Z 	updating dependency infos of mkdepend-1.7
2025-06-14T19:28:25.9184302Z 	updating dependency infos of mksh-59c
2025-06-14T19:28:25.9184780Z 	updating dependency infos of mkvtoolnix-75.0.0
2025-06-14T19:28:25.9185277Z 	updating dependency infos of mlpack-3.4.2
2025-06-14T19:28:25.9185741Z 	updating dependency infos of mlt-7.32.0
2025-06-14T19:28:25.9186223Z 	updating dependency infos of mm_common-1.0.6
2025-06-14T19:28:25.9186739Z 	updating dependency infos of module_build-0.4234
2025-06-14T19:28:25.9187309Z 	updating dependency infos of module_build_tiny-0.051
2025-06-14T19:28:25.9187901Z 	updating dependency infos of module_implementation-0.09
2025-06-14T19:28:25.9188454Z 	updating dependency infos of module_pluggable-6.2
2025-06-14T19:28:25.9188964Z 	updating dependency infos of module_runtime-0.016
2025-06-14T19:28:25.9189476Z 	updating dependency infos of module_scandeps-1.35
2025-06-14T19:28:25.9189946Z 	updating dependency infos of moe-1.1.2
2025-06-14T19:28:25.9190382Z 	updating dependency infos of mog-0.63.1548
2025-06-14T19:28:25.9190840Z 	updating dependency infos of moleinvasion-0.4
2025-06-14T19:28:25.9191539Z 	updating dependency infos of moleinvasion_music-0.4
2025-06-14T19:28:25.9192158Z 	monkeystudio-1.9.0.4 is still marked as broken on target architecture
2025-06-14T19:28:25.9192735Z 	updating dependency infos of monoid-0.61
2025-06-14T19:28:25.9193187Z 	updating dependency infos of monsterz-0.7.1
2025-06-14T19:28:25.9193731Z 	updating dependency infos of moonlight_embedded-20240611~git
2025-06-14T19:28:25.9194288Z 	updating dependency infos of moreutils-0.70
2025-06-14T19:28:25.9194907Z 	updating dependency infos of mosh-1.3.2
2025-06-14T19:28:25.9195373Z 	updating dependency infos of mosquitto-2.0.20
2025-06-14T19:28:25.9195826Z 	updating dependency infos of most-5.2.0
2025-06-14T19:28:25.9196276Z 	updating dependency infos of mozc-2.26.4451.1
2025-06-14T19:28:25.9196740Z 	updating dependency infos of mp3gain-1.6.2
2025-06-14T19:28:25.9197174Z 	updating dependency infos of mpc-1.2.1
2025-06-14T19:28:25.9197607Z 	updating dependency infos of mpd-0.23.15
2025-06-14T19:28:25.9198058Z 	updating dependency infos of mpdecimal-4.0.0
2025-06-14T19:28:25.9198512Z 	updating dependency infos of mpfi-1.5.4
2025-06-14T19:28:25.9198935Z 	updating dependency infos of mpfr-4.2.0
2025-06-14T19:28:25.9199364Z 	updating dependency infos of mpfr3-3.1.6
2025-06-14T19:28:25.9199807Z 	updating dependency infos of mpg123-1.32.9
2025-06-14T19:28:25.9200242Z 	updating dependency infos of mpg321-0.3.2
2025-06-14T19:28:25.9200689Z 	updating dependency infos of mplayer-1.5
2025-06-14T19:28:25.9201245Z 	updating dependency infos of mplus-062
2025-06-14T19:28:25.9201681Z 	updating dependency infos of mpv-0.38.0
2025-06-14T19:28:25.9202114Z 	updating dependency infos of mpvqt-1.1.1
2025-06-14T19:28:25.9202640Z 	updating dependency infos of mrboom_libretro-5.2_20230321
2025-06-14T19:28:25.9203183Z 	updating dependency infos of mro_compat-0.15
2025-06-14T19:28:25.9203647Z 	updating dependency infos of mrpeeps-1.2
2025-06-14T19:28:25.9204109Z 	updating dependency infos of msgpack-1.0.3
2025-06-14T19:28:25.9204585Z 	updating dependency infos of msgpack_c_cpp-3.2.0
2025-06-14T19:28:25.9204866Z 	updating dependency infos of msieve-1.53
2025-06-14T19:28:25.9205128Z 	updating dependency infos of msttcorefonts-1.0
2025-06-14T19:28:25.9205399Z 	updating dependency infos of mtafsir-0.2
2025-06-14T19:28:25.9205640Z 	recipe for mtdev-1.1.5 is still broken:
2025-06-14T19:28:25.9205959Z 	Error: package mtdev-1.1.5 cannot be built for architecture x86_64
2025-06-14T19:28:25.9206434Z 	updating dependency infos of mtools-4.0.43
2025-06-14T19:28:25.9206687Z 	updating dependency infos of mtr-0.73
2025-06-14T19:28:25.9206944Z 	updating dependency infos of mtxclient-0.9.2
2025-06-14T19:28:25.9207203Z 	updating dependency infos of mudlet-4.0.3
2025-06-14T19:28:25.9207453Z 	updating dependency infos of mujs-1.3.5
2025-06-14T19:28:25.9207704Z 	updating dependency infos of multidict-4.5.2
2025-06-14T19:28:25.9207982Z 	updating dependency infos of multimarkdown-6.7.0
2025-06-14T19:28:25.9208251Z 	updating dependency infos of multitalk-1.4
2025-06-14T19:28:25.9208512Z 	updating dependency infos of mumble-1.5.634
2025-06-14T19:28:25.9208758Z 	updating dependency infos of muon-0.4.0
2025-06-14T19:28:25.9209007Z 	updating dependency infos of muparser-2.2.5
2025-06-14T19:28:25.9209262Z 	updating dependency infos of mupdf-1.20.3
2025-06-14T19:28:25.9209523Z 	updating dependency infos of mupen64plus-2.5.9
2025-06-14T19:28:25.9209864Z 	updating dependency infos of mupen64plus_next_libretro-1.0_20250121
2025-06-14T19:28:25.9210195Z 	updating dependency infos of muscle-6.70
2025-06-14T19:28:25.9210467Z 	updating dependency infos of musepack_tools-475
2025-06-14T19:28:25.9210739Z 	updating dependency infos of musescore-3.6.2
2025-06-14T19:28:25.9211014Z 	updating dependency infos of musicbrainz-5.1.0
2025-06-14T19:28:25.9211519Z 	updating dependency infos of musicpc-0.34
2025-06-14T19:28:25.9211785Z 	updating dependency infos of musikcube-3.0.0
2025-06-14T19:28:25.9212074Z 	updating dependency infos of musixtnt-2016_01_30
2025-06-14T19:28:25.9212343Z 	updating dependency infos of mustache-4.1
2025-06-14T19:28:25.9212605Z 	updating dependency infos of mutagen-1.47.0
2025-06-14T19:28:25.9212857Z 	updating dependency infos of mutt-2.2.13
2025-06-14T19:28:25.9213107Z 	updating dependency infos of mxml-3.1
2025-06-14T19:28:25.9213356Z 	updating dependency infos of mygui-3.2.3~git
2025-06-14T19:28:25.9213638Z 	updating dependency infos of mypaint_brushes-1.3.1
2025-06-14T19:28:25.9213935Z 	updating dependency infos of myspell-6.2.6.2
2025-06-14T19:28:25.9214320Z 	updating dependency infos of myspell_kv-0.0.1.0
2025-06-14T19:28:25.9214611Z 	updating dependency infos of myspell_udm-0.0.1.0
2025-06-14T19:28:25.9214874Z 	recipe for mysql-5.0.83 is still broken:
2025-06-14T19:28:25.9215203Z 	Error: package mysql-5.0.83 cannot be built for architecture x86_64
2025-06-14T19:28:25.9215528Z 	updating dependency infos of mythes-1.2.4
2025-06-14T19:28:25.9215811Z 	updating dependency infos of nafees_nastaleeq-1.02
2025-06-14T19:28:25.9216102Z 	updating dependency infos of nafees_riqa-1.00
2025-06-14T19:28:25.9216381Z 	updating dependency infos of naken_asm-2022.08.06
2025-06-14T19:28:25.9216687Z 	updating dependency infos of namespace_autoclean-0.31
2025-06-14T19:28:25.9216988Z 	updating dependency infos of namespace_clean-0.27
2025-06-14T19:28:25.9217258Z 	updating dependency infos of nano-8.1
2025-06-14T19:28:25.9217494Z 	recipe for nanodot-1.1b is still broken:
2025-06-14T19:28:25.9217746Z 	Error: No match found for license unknown
2025-06-14T19:28:25.9218031Z 	Error: Valid license filenames included with Haiku are:
2025-06-14T19:28:25.9219628Z 	Error: Anti-Grain Geometry, Apache v2, Artistic, Artistic v2.0, BSD (2-clause), BSD (3-clause), BSD (4-clause), Be Sample Code License, Bullet, CDDL v1, CQuantizer, DEC, GLUT (Mark Kilgard), GNU GPL font exception, GNU GPL v1, GNU GPL v2, GNU GPL v3, GNU LGPL v2, GNU LGPL v2.1, GNU LGPL v3, GPC, Intel (2xxx firmware), Intel (ACPICA), Intel (firmware), LibHTTPd, LibJPEG, LibPNG, MAPM, MIT, MIT (no promotion), MPL v1.1, MPL v2.0, Marvell (firmware), OpenGroup, PDFlib Lite, Public Domain, Ralink (firmware), SGI Free B, SIL Open Font License v1.1, Zlib
2025-06-14T19:28:25.9221503Z 	Error: (in /runner/work/haikuports/haikuports/haiku-apps/nanodot/nanodot-1.1b.recipe)
2025-06-14T19:28:25.9221952Z 	updating dependency infos of nanosaur-1.4.3
2025-06-14T19:28:25.9222248Z 	updating dependency infos of nanosvgtranslator-1.0.8
2025-06-14T19:28:25.9222666Z 	updating dependency infos of nanumfont-2.5
2025-06-14T19:28:25.9222921Z 	updating dependency infos of nasm-2.15.05
2025-06-14T19:28:25.9223180Z 	updating dependency infos of naspro-0.5.1
2025-06-14T19:28:25.9223434Z 	updating dependency infos of nbdkit-1.36.1
2025-06-14T19:28:25.9223702Z 	updating dependency infos of ncdu-1.16
2025-06-14T19:28:25.9223952Z 	updating dependency infos of ncmpcpp-0.9.2
2025-06-14T19:28:25.9224229Z 	updating dependency infos of ncompress-4.2.4.4
2025-06-14T19:28:25.9224499Z 	recipe for ncurses5-6.2 is still broken:
2025-06-14T19:28:25.9224887Z 	Error: package ncurses5-6.2 cannot be built for architecture x86_64
2025-06-14T19:28:25.9225470Z 	updating dependency infos of ncurses6-6.5
2025-06-14T19:28:25.9225721Z 	updating dependency infos of ne-3.3.2
2025-06-14T19:28:25.9226015Z 	updating dependency infos of nekop2_libretro-0.86_20241021
2025-06-14T19:28:25.9226312Z 	updating dependency infos of neo-0.6.1
2025-06-14T19:28:25.9226602Z 	updating dependency infos of neocd_libretro-0.5_20241021
2025-06-14T19:28:25.9226911Z 	updating dependency infos of neochat-25.04.0
2025-06-14T19:28:25.9227186Z 	updating dependency infos of neofetch-7.1.0
2025-06-14T19:28:25.9227444Z 	updating dependency infos of neon-0.34.0
2025-06-14T19:28:25.9227701Z 	updating dependency infos of neonlights-0.2
2025-06-14T19:28:25.9227980Z 	updating dependency infos of nesalizer-1.0~git
2025-06-14T19:28:25.9228297Z 	updating dependency infos of nestopia_libretro-1.49_20250323
2025-06-14T19:28:25.9228610Z 	updating dependency infos of net_http-6.23
2025-06-14T19:28:25.9228869Z 	updating dependency infos of net_ssleay-1.94
2025-06-14T19:28:25.9229138Z 	updating dependency infos of netbeans_bin-23
2025-06-14T19:28:25.9229402Z 	updating dependency infos of netcat-1.10
2025-06-14T19:28:25.9229652Z 	updating dependency infos of netcdf-4.8.1
2025-06-14T19:28:25.9229916Z 	updating dependency infos of netcdf4.7-4.7.2
2025-06-14T19:28:25.9230181Z 	updating dependency infos of netcdf_cxx-4.3.1
2025-06-14T19:28:25.9230470Z 	updating dependency infos of netcdf_fortran-4.5.4
2025-06-14T19:28:25.9230746Z 	updating dependency infos of nethack-3.6.2
2025-06-14T19:28:25.9231310Z 	recipe for netpanzer-0.8.6 is still broken:
2025-06-14T19:28:25.9231913Z 	Error: package netpanzer-0.8.6 cannot be built for architecture x86_64
2025-06-14T19:28:25.9232276Z 	updating dependency infos of netpbm-10.86.42
2025-06-14T19:28:25.9232548Z 	updating dependency infos of netperf-2.7.0
2025-06-14T19:28:25.9232805Z 	updating dependency infos of netpulse-0.2.3
2025-06-14T19:28:25.9233075Z 	updating dependency infos of netsurf-3.11
2025-06-14T19:28:25.9233361Z 	updating dependency infos of netsurf_buildsystem-1.10
2025-06-14T19:28:27.2333093Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:27.2346698Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:27.2360193Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:27.2373708Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:27.2387124Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:27.2400312Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2092478Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2106689Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2120726Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2134631Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2148278Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2162439Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2176147Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2189745Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2203631Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2217168Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2230689Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2244431Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2257858Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2620379Z 	updating dependency infos of nettle-3.7.3
2025-06-14T19:28:28.2621012Z 	updating dependency infos of neverball-1.6.1~20190808
2025-06-14T19:28:28.2621931Z 	updating dependency infos of newlisp-10.7.5
2025-06-14T19:28:28.2622480Z 	updating dependency infos of nextcloud_client-3.11.1
2025-06-14T19:28:28.2623005Z 	updating dependency infos of nfd-1.0
2025-06-14T19:28:28.2623513Z 	updating dependency infos of nghttp2-1.63.0
2025-06-14T19:28:28.2624008Z 	updating dependency infos of nghttp3-1.2.0
2025-06-14T19:28:28.2624503Z 	updating dependency infos of nginx-1.23.2
2025-06-14T19:28:28.2624971Z 	updating dependency infos of ngspice-43
2025-06-14T19:28:28.2625529Z 	nhc98-1.22 is still marked as broken on target architecture
2025-06-14T19:28:28.2626106Z 	updating dependency infos of nheko-0.12.0
2025-06-14T19:28:28.2633975Z 	updating dependency infos of nifskope-2.0.dev9
2025-06-14T19:28:28.2634599Z 	updating dependency infos of nightandday-0.1.2
2025-06-14T19:28:28.2635125Z 	updating dependency infos of nim-2.2.4
2025-06-14T19:28:28.2635605Z 	updating dependency infos of ninja-1.12.1
2025-06-14T19:28:28.2636099Z 	updating dependency infos of nitroshare-0.3.4
2025-06-14T19:28:28.2636718Z 	niue-20140701 is still marked as untested on target architecture
2025-06-14T19:28:28.2637347Z 	updating dependency infos of nlohmann_json-3.11.2
2025-06-14T19:28:28.2637855Z 	updating dependency infos of nlopt-2.7.1
2025-06-14T19:28:28.2638422Z 	nmap-7.94 is still marked as untested on target architecture
2025-06-14T19:28:28.2639230Z 	updating dependency infos of nmap-3.81
2025-06-14T19:28:28.2639717Z 	updating dependency infos of nnn-5.1
2025-06-14T19:28:28.2640192Z 	updating dependency infos of nodejs20-20.15.1
2025-06-14T19:28:28.2640803Z 	nogravity-2.0 is still marked as untested on target architecture
2025-06-14T19:28:28.2641591Z 	updating dependency infos of nomacs-3.17
2025-06-14T19:28:28.2642072Z 	updating dependency infos of nose-1.3.7
2025-06-14T19:28:28.2642585Z 	updating dependency infos of notepadqq-1.4.8.ote
2025-06-14T19:28:28.2643086Z 	updating dependency infos of notes-2.1.0
2025-06-14T19:28:28.2643577Z 	updating dependency infos of noteshrink-0.1.1
2025-06-14T19:28:28.2644065Z 	updating dependency infos of noto-20250201
2025-06-14T19:28:28.2644569Z 	updating dependency infos of noto_emoji-20230311
2025-06-14T19:28:28.2645112Z 	updating dependency infos of noto_emoji_color-2.042
2025-06-14T19:28:28.2645675Z 	updating dependency infos of noto_sans_cjk-2.004
2025-06-14T19:28:28.2646219Z 	updating dependency infos of noto_serif_cjk-2.003
2025-06-14T19:28:28.2646742Z 	updating dependency infos of novprog-3.2.3
2025-06-14T19:28:28.2647215Z 	updating dependency infos of npm-10.9.2
2025-06-14T19:28:28.2647659Z 	updating dependency infos of npth-1.6
2025-06-14T19:28:28.2648122Z 	updating dependency infos of nsgenbind-0.9
2025-06-14T19:28:28.2648579Z 	updating dependency infos of nspr-4.36
2025-06-14T19:28:28.2649021Z 	updating dependency infos of nss-3.110
2025-06-14T19:28:28.2649494Z 	updating dependency infos of number_compare-0.03
2025-06-14T19:28:28.2650041Z 	updating dependency infos of numptyphysics-0.3.5
2025-06-14T19:28:28.2650537Z 	updating dependency infos of numpy-2.2.3
2025-06-14T19:28:28.2650995Z 	updating dependency infos of nuspell-4.2.0
2025-06-14T19:28:28.2651658Z 	updating dependency infos of nxengine-1.0.0.4~git
2025-06-14T19:28:28.2652155Z 	updating dependency infos of nyancat-1.5.2
2025-06-14T19:28:28.2652934Z 	updating dependency infos of o2em_libretro-1.18_20241021
2025-06-14T19:28:28.2653482Z 	updating dependency infos of objfw-1.3.2
2025-06-14T19:28:28.2653955Z 	updating dependency infos of ocaml-4.07.0
2025-06-14T19:28:28.2654400Z 	updating dependency infos of ocl_icd-2.3.1
2025-06-14T19:28:28.2654803Z 	updating dependency infos of ocp-3.0.1
2025-06-14T19:28:28.2655205Z 	updating dependency infos of ocr-0.2
2025-06-14T19:28:28.2655607Z 	updating dependency infos of octave-9.4.0
2025-06-14T19:28:28.2656032Z 	updating dependency infos of ode-0.12
2025-06-14T19:28:28.2656434Z 	updating dependency infos of odin-2025.4.0
2025-06-14T19:28:28.2656850Z 	updating dependency infos of odt2txt-0.5
2025-06-14T19:28:28.2657257Z 	updating dependency infos of okteta-0.26.15
2025-06-14T19:28:28.2657676Z 	updating dependency infos of okular-25.04.0
2025-06-14T19:28:28.2658113Z 	updating dependency infos of okular_kf5-23.08.5
2025-06-14T19:28:28.2658539Z 	updating dependency infos of olm-3.2.16
2025-06-14T19:28:28.2658982Z 	updating dependency infos of omnispeak-1.2~git
2025-06-14T19:28:28.2659456Z 	updating dependency infos of omnispeak_keen4-1.4
2025-06-14T19:28:28.2659924Z 	updating dependency infos of oniguruma-6.9.8
2025-06-14T19:28:28.2660338Z 	updating dependency infos of onnx-1.17.0
2025-06-14T19:28:28.2660757Z 	updating dependency infos of open_sans-1.101
2025-06-14T19:28:28.2661539Z 	updating dependency infos of open_supaplex-7.1.2
2025-06-14T19:28:28.2661998Z 	updating dependency infos of openal-1.21.1
2025-06-14T19:28:28.2662445Z 	updating dependency infos of openarena-0.8.9~git
2025-06-14T19:28:28.2662916Z 	updating dependency infos of openarena_data-0.8.8
2025-06-14T19:28:28.2663376Z 	updating dependency infos of openblas-0.3.23
2025-06-14T19:28:28.2663821Z 	updating dependency infos of openboardview-8.95.1
2025-06-14T19:28:28.2664312Z 	updating dependency infos of opencascade-7.8.1
2025-06-14T19:28:28.2664768Z 	updating dependency infos of opencc-1.1.4
2025-06-14T19:28:28.2665213Z 	recipe for opencity-0.0.6.3 is still broken:
2025-06-14T19:28:28.2665953Z 	Error: package opencity-0.0.6.3 cannot be built for architecture x86_64
2025-06-14T19:28:28.2666593Z 	updating dependency infos of opencl_headers-2024_10_24
2025-06-14T19:28:28.2667113Z 	updating dependency infos of openclaw-1.0.3_20210607
2025-06-14T19:28:28.2667584Z 	updating dependency infos of openclonk-9.0~git
2025-06-14T19:28:28.2668057Z 	updating dependency infos of opencollada-1.6.68
2025-06-14T19:28:28.2668533Z 	updating dependency infos of opencolorio-2.0.1
2025-06-14T19:28:28.2669029Z 	updating dependency infos of opencolorio2.3-2.3.2
2025-06-14T19:28:28.2669502Z 	updating dependency infos of opencsg-1.8.1
2025-06-14T19:28:28.2669944Z 	updating dependency infos of opencv-4.8.0
2025-06-14T19:28:28.2670376Z 	updating dependency infos of opencv3-3.4.3
2025-06-14T19:28:28.2670819Z 	updating dependency infos of opendetex-2.8.11
2025-06-14T19:28:28.2671491Z 	updating dependency infos of opendune-0.9
2025-06-14T19:28:28.2671990Z 	updating dependency infos of opendyslexic-0.91.12
2025-06-14T19:28:28.2672492Z 	updating dependency infos of openexr-2.4.1
2025-06-14T19:28:28.2672952Z 	updating dependency infos of openexr25-2.5.4
2025-06-14T19:28:28.2673435Z 	updating dependency infos of openexr3.2-3.2.4
2025-06-14T19:28:28.2673917Z 	updating dependency infos of openexr30-3.0.5
2025-06-14T19:28:28.2674265Z 	updating dependency infos of openh264-2.4.1
2025-06-14T19:28:28.2674554Z 	updating dependency infos of openimageio2.2-2.2.16.0
2025-06-14T19:28:28.2674867Z 	updating dependency infos of openimageio2.3-2.3.10.0
2025-06-14T19:28:28.2675170Z 	updating dependency infos of openimageio2.5-2.5.12.0
2025-06-14T19:28:28.2675456Z 	updating dependency infos of openjazz-20240919
2025-06-14T19:28:28.2675738Z 	recipe for openjdk-1.7_u80_b02 is still broken:
2025-06-14T19:28:28.2676085Z 	Error: package openjdk-1.7_u80_b02 cannot be built for architecture x86_64
2025-06-14T19:28:28.2676447Z 	recipe for openjdk-1.7.u80_b32 is still broken:
2025-06-14T19:28:28.2676944Z 	Error: package openjdk-1.7.u80_b32 cannot be built for architecture x86_64
2025-06-14T19:28:28.2677294Z 	recipe for openjdk10-10.0.2.13 is still broken:
2025-06-14T19:28:28.2677642Z 	Error: package openjdk10-10.0.2.13 cannot be built for architecture x86_64
2025-06-14T19:28:28.2678003Z 	updating dependency infos of openjdk10_bin-10.0.2.13
2025-06-14T19:28:28.2678301Z 	updating dependency infos of openjdk11-11.0.27.5
2025-06-14T19:28:28.2678584Z 	updating dependency infos of openjdk12-12.0.2.10
2025-06-14T19:28:28.2678865Z 	updating dependency infos of openjdk13-13.0.2.8
2025-06-14T19:28:28.2679146Z 	updating dependency infos of openjdk14-14.0.2.12
2025-06-14T19:28:28.2679419Z 	updating dependency infos of openjdk15-15.0.1.9
2025-06-14T19:28:28.2679701Z 	updating dependency infos of openjdk16-16.0.2.7
2025-06-14T19:28:28.2679974Z 	updating dependency infos of openjdk17-17.0.14.7
2025-06-14T19:28:28.2680255Z 	updating dependency infos of openjdk18-18.0.2.1
2025-06-14T19:28:28.2680526Z 	updating dependency infos of openjdk19-19.0.2.1
2025-06-14T19:28:28.2680804Z 	updating dependency infos of openjdk20-20.0.2.1
2025-06-14T19:28:28.2681436Z 	updating dependency infos of openjdk21-21.0.7.1
2025-06-14T19:28:28.2681803Z 	updating dependency infos of openjdk22-22.0.2.1
2025-06-14T19:28:28.2682095Z 	updating dependency infos of openjdk23-23.0.2.1
2025-06-14T19:28:28.2682371Z 	updating dependency infos of openjdk24-24.0.0.1
2025-06-14T19:28:28.2682670Z 	updating dependency infos of openjdk7_bin-1.7.u80_b32
2025-06-14T19:28:28.2682980Z 	updating dependency infos of openjdk8-1.8.u442_b00
2025-06-14T19:28:28.2683272Z 	recipe for openjdk9-9.0.4.11 is still broken:
2025-06-14T19:28:28.2683632Z 	Error: package openjdk9-9.0.4.11 cannot be built for architecture x86_64
2025-06-14T19:28:28.2684028Z 	updating dependency infos of openjk_academy-2025.03.10
2025-06-14T19:28:28.2684355Z 	updating dependency infos of openjk_outcast-2025.03.10
2025-06-14T19:28:28.2684644Z 	updating dependency infos of openjpeg-2.5.3
2025-06-14T19:28:28.2684967Z 	updating dependency infos of openlara_libretro-0.a3_20200525
2025-06-14T19:28:28.2685424Z 	updating dependency infos of openldap-2.6.6
2025-06-14T19:28:28.2685713Z 	updating dependency infos of openldap2.4-2.4.48
2025-06-14T19:28:28.2685990Z 	updating dependency infos of openlibm-0.7.5
2025-06-14T19:28:28.2686253Z 	updating dependency infos of openmortal-0.7
2025-06-14T19:28:28.2686575Z 	openmpi-4.1.0 is still marked as untested on target architecture
2025-06-14T19:28:28.2686900Z 	updating dependency infos of openmw-0.47.0
2025-06-14T19:28:28.2687199Z 	updating dependency infos of openoriginpackage-1.1.3
2025-06-14T19:28:28.2687503Z 	updating dependency infos of openpam-20170430
2025-06-14T19:28:28.2687786Z 	updating dependency infos of openscad-2021.01
2025-06-14T19:28:28.2688068Z 	updating dependency infos of openscenegraph-3.6.5
2025-06-14T19:28:28.2688357Z 	updating dependency infos of openshot-3.1.0
2025-06-14T19:28:28.2688613Z 	updating dependency infos of opensound-4.2
2025-06-14T19:28:28.2688882Z 	updating dependency infos of opensp-1.5.2
2025-06-14T19:28:28.2689145Z 	updating dependency infos of openssh-9.8p1
2025-06-14T19:28:28.2689399Z 	updating dependency infos of openssl-1.1.1w
2025-06-14T19:28:28.2689661Z 	updating dependency infos of openssl3-3.5.0
2025-06-14T19:28:28.2689929Z 	updating dependency infos of opensubdiv-3.5.0
2025-06-14T19:28:28.2690215Z 	updating dependency infos of opensubdiv3.4-3.4.3
2025-06-14T19:28:28.2690508Z 	updating dependency infos of opensyobonaction-rc3
2025-06-14T19:28:28.2690813Z 	updating dependency infos of opentimelineio-0.17.0
2025-06-14T19:28:28.2691299Z 	updating dependency infos of opentoonz-1.7.1
2025-06-14T19:28:28.2691612Z 	updating dependency infos of openttd-14.1
2025-06-14T19:28:28.2691885Z 	updating dependency infos of openttd_gfx-7.1
2025-06-14T19:28:28.2692161Z 	updating dependency infos of openttd_msx-0.4.2
2025-06-14T19:28:28.2692444Z 	updating dependency infos of openttd_sfx-1.0.3
2025-06-14T19:28:28.2692736Z 	updating dependency infos of opentyrian-2.1.20130907
2025-06-14T19:28:28.2693162Z 	updating dependency infos of opentyrian_data-21
2025-06-14T19:28:28.2693441Z 	updating dependency infos of openvdb-7.1.0
2025-06-14T19:28:28.2693704Z 	updating dependency infos of openvpn-2.6.13
2025-06-14T19:28:28.2693967Z 	recipe for openwatcom-2.0.0 is still broken:
2025-06-14T19:28:28.2694310Z 	Error: package openwatcom-2.0.0 cannot be built for architecture x86_64
2025-06-14T19:28:28.2694674Z 	recipe for openwatcom-1.9.0 is still broken:
2025-06-14T19:28:28.2695013Z 	Error: package openwatcom-1.9.0 cannot be built for architecture x86_64
2025-06-14T19:28:28.2695362Z 	updating dependency infos of openxcom-1.0
2025-06-14T19:28:28.2695664Z 	updating dependency infos of opera_libretro-1.0.0_20241017
2025-06-14T19:28:28.2695980Z 	updating dependency infos of optiimage-1.0.0
2025-06-14T19:28:28.2696240Z 	updating dependency infos of optipng-0.7.8
2025-06-14T19:28:28.2696532Z 	updating dependency infos of optipngtranslator-0.1.0
2025-06-14T19:28:28.2696827Z 	updating dependency infos of opus-1.3.1
2025-06-14T19:28:28.2697077Z 	updating dependency infos of opus_tools-0.2
2025-06-14T19:28:28.2697342Z 	updating dependency infos of opusfile-0.12
2025-06-14T19:28:28.2697589Z 	updating dependency infos of orc-0.4.32
2025-06-14T19:28:28.2697855Z 	updating dependency infos of orcaslicer-2.3.0
2025-06-14T19:28:28.2723838Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2737758Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2751665Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2765350Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2778965Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2792692Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2806305Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2821487Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2835105Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2848933Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2863178Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2876515Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:28.2889824Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8090209Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8103670Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8117021Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8130155Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8144223Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8157426Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8170670Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8184259Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8197521Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8210686Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8224083Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8237600Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8251275Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8264542Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8278047Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8291571Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8305583Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8319388Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.8333283Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9827651Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9841445Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9855076Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9868297Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9881924Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9895229Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9909564Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9923218Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9936771Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9950066Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9963677Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9977089Z packageEntries: warning: "glib" doesn't seem to be a valid package suffix.
2025-06-14T19:28:29.9990315Z packageEntries: warning: "qt5" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0003766Z packageEntries: warning: "qt6" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0465922Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0479597Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0493633Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0507352Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0521054Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0535044Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0548722Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0562427Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0576201Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0589612Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0603090Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0616537Z packageEntries: warning: "glib" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0630008Z packageEntries: warning: "qt5" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.0643486Z packageEntries: warning: "qt6" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1115522Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1129752Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1143933Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1157916Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1171888Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1185966Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1199629Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1213533Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1227252Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1240986Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1254793Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1268521Z packageEntries: warning: "glib" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1282564Z packageEntries: warning: "qt5" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.1296287Z packageEntries: warning: "qt6" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.4835665Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.4848713Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.4862328Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.4875925Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.4889169Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.4902582Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.4915680Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:30.6490388Z 	updating dependency infos of orcus-0.17.2
2025-06-14T19:28:30.6490927Z 	updating dependency infos of orcus0.18-0.19.2
2025-06-14T19:28:30.6491667Z 	organizer-0.1 is still marked as untested on target architecture
2025-06-14T19:28:30.6492360Z 	oricutron-1.2.1 is still marked as untested on target architecture
2025-06-14T19:28:30.6493028Z 	oricutron-1.1_svn is still marked as untested on target architecture
2025-06-14T19:28:30.6493905Z 	updating dependency infos of osl1.11-1.11.17.0
2025-06-14T19:28:30.6494360Z 	updating dependency infos of osl1.13-1.13.10.0
2025-06-14T19:28:30.6494824Z 	updating dependency infos of osmctools-0.9
2025-06-14T19:28:30.6495305Z 	updating dependency infos of otter_browser-1.0.03
2025-06-14T19:28:30.6495613Z 	updating dependency infos of ottomatic-4.0.0
2025-06-14T19:28:30.6495904Z 	updating dependency infos of overpass-3.0.3
2025-06-14T19:28:30.6496182Z 	recipe for owncloud_client-2.6.1 is still broken:
2025-06-14T19:28:30.6496563Z 	Error: package owncloud_client-2.6.1 cannot be built for architecture x86_64
2025-06-14T19:28:30.6496938Z 	updating dependency infos of oxipng-9.0.0
2025-06-14T19:28:30.6497222Z 	updating dependency infos of p11_kit-0.23.18.1
2025-06-14T19:28:30.6497510Z 	updating dependency infos of p7zip-17.05
2025-06-14T19:28:30.6497769Z 	updating dependency infos of pachi-1.0
2025-06-14T19:28:30.6498043Z 	updating dependency infos of package_stash-0.40
2025-06-14T19:28:30.6498339Z 	updating dependency infos of package_stash_xs-0.30
2025-06-14T19:28:30.6498634Z 	updating dependency infos of packaging-24.1
2025-06-14T19:28:30.6498987Z 	packetdrill-20160707 is still marked as broken on target architecture
2025-06-14T19:28:30.6499331Z 	updating dependency infos of pad-0~20181029
2025-06-14T19:28:30.6499608Z 	updating dependency infos of paladin-2.9
2025-06-14T19:28:30.6499880Z 	updating dependency infos of palapeli-25.04.0
2025-06-14T19:28:30.6500163Z 	updating dependency infos of pam_yubico-2.27
2025-06-14T19:28:30.6500489Z 	pandas-1.3.2 is still marked as untested on target architecture
2025-06-14T19:28:30.6500813Z 	updating dependency infos of pango-1.54.0
2025-06-14T19:28:30.6501069Z 	updating dependency infos of pangomm-2.46.2
2025-06-14T19:28:30.6501576Z 	updating dependency infos of paperkey-1.6
2025-06-14T19:28:30.6501855Z 	updating dependency infos of parallel-2023.10.22
2025-06-14T19:28:30.6502203Z 	updating dependency infos of parallel_n64_libretro-2.0rc2_20250302
2025-06-14T19:28:30.6502758Z 	updating dependency infos of parameterized-0.9.0
2025-06-14T19:28:30.6503074Z 	updating dependency infos of params_validate-1.31
2025-06-14T19:28:30.6503410Z 	updating dependency infos of params_validationcompiler-0.31
2025-06-14T19:28:30.6503735Z 	updating dependency infos of paratype-1.0
2025-06-14T19:28:30.6503995Z 	updating dependency infos of pari-2.17.0
2025-06-14T19:28:30.6504285Z 	updating dependency infos of parse_recdescent-1.967015
2025-06-14T19:28:30.6504595Z 	updating dependency infos of parse_yapp-1.21
2025-06-14T19:28:30.6504911Z 	parted-3.2 is still marked as untested on target architecture
2025-06-14T19:28:30.6505229Z 	updating dependency infos of partio-1.14.6
2025-06-14T19:28:30.6505586Z 	partitionmanager-3.3.1~git is still marked as untested on target architecture
2025-06-14T19:28:30.6505963Z 	updating dependency infos of pass-1.7.4
2025-06-14T19:28:30.6506222Z 	updating dependency infos of patch-2.7.6
2025-06-14T19:28:30.6506493Z 	updating dependency infos of patchelf-0.18.0
2025-06-14T19:28:30.6506781Z 	updating dependency infos of patchutils-0.4.2
2025-06-14T19:28:30.6507058Z 	updating dependency infos of path_tiny-0.146
2025-06-14T19:28:30.6507341Z 	updating dependency infos of pathological-1.1.3_17
2025-06-14T19:28:30.6507628Z 	updating dependency infos of pathspec-0.11.1
2025-06-14T19:28:30.6507898Z 	updating dependency infos of pathtools-3.75
2025-06-14T19:28:30.6508157Z 	updating dependency infos of pax_utils-1.2.6
2025-06-14T19:28:30.6508415Z 	updating dependency infos of pbr-5.5.1
2025-06-14T19:28:30.6508710Z 	pcem-10.1 is still marked as untested on target architecture
2025-06-14T19:28:30.6509018Z 	updating dependency infos of pciutils-3.11.1
2025-06-14T19:28:30.6509290Z 	updating dependency infos of pcmanfm_qt-1.3.0
2025-06-14T19:28:30.6509610Z 	pcsc_lite-1.8.25 is still marked as untested on target architecture
2025-06-14T19:28:30.6509989Z 	updating dependency infos of pcsx_rearmed_libretro-r22_20250412
2025-06-14T19:28:30.6510315Z 	updating dependency infos of pdflib-5.0.3
2025-06-14T19:28:30.6510710Z 	updating dependency infos of pdftranslator-1.0.4
2025-06-14T19:28:30.6510990Z 	updating dependency infos of pdfwriter-1.0
2025-06-14T19:28:30.6511620Z 	updating dependency infos of pe-2.5.0
2025-06-14T19:28:30.6511879Z 	updating dependency infos of pe_bear-0.6.5.2
2025-06-14T19:28:30.6512140Z 	updating dependency infos of peaclock-0.1.7
2025-06-14T19:28:30.6512453Z 	pecobeat-1.0 is still marked as untested on target architecture
2025-06-14T19:28:30.6512771Z 	updating dependency infos of pecorename-2.1
2025-06-14T19:28:30.6513028Z 	recipe for peek-20140206 is still broken:
2025-06-14T19:28:30.6513345Z 	Error: package peek-20140206 cannot be built for architecture x86_64
2025-06-14T19:28:30.6513676Z 	updating dependency infos of peg_e-1.3.3
2025-06-14T19:28:30.6513928Z 	updating dependency infos of peggy-0.7.5
2025-06-14T19:28:30.6514170Z 	updating dependency infos of pegtl-2.3.3
2025-06-14T19:28:30.6514434Z 	updating dependency infos of pencil-0.6.5
2025-06-14T19:28:30.6514716Z 	updating dependency infos of penguin_command-1.6.11
2025-06-14T19:28:30.6515009Z 	updating dependency infos of pep8-1.7.1
2025-06-14T19:28:30.6515253Z 	updating dependency infos of perl-5.40.2
2025-06-14T19:28:30.6515537Z 	updating dependency infos of perlio_utf8_strict-0.010
2025-06-14T19:28:30.6515819Z 	updating dependency infos of pfetch-0.6
2025-06-14T19:28:30.6516074Z 	updating dependency infos of phantomlimb-1
2025-06-14T19:28:30.6516333Z 	updating dependency infos of phonon-4.12.0
2025-06-14T19:28:30.6516586Z 	updating dependency infos of phonon6-4.12.0
2025-06-14T19:28:30.6516875Z 	updating dependency infos of phonon_gstreamer-4.10.0
2025-06-14T19:28:30.6517171Z 	updating dependency infos of phonon_vlc-0.12.0
2025-06-14T19:28:30.6517462Z 	updating dependency infos of photivo-0~pre20201120
2025-06-14T19:28:30.6517753Z 	updating dependency infos of photograbber-2.3.4
2025-06-14T19:28:30.6518034Z 	updating dependency infos of phototonic-2.1
2025-06-14T19:28:30.6518428Z 	updating dependency infos of php8-8.4.4
2025-06-14T19:28:30.6518679Z 	updating dependency infos of physfs-3.0.2
2025-06-14T19:28:30.6518952Z 	updating dependency infos of pianobar-2024.12.21
2025-06-14T19:28:30.6519223Z 	updating dependency infos of picard-2.13.2
2025-06-14T19:28:30.6519476Z 	updating dependency infos of pick-4.0.0
2025-06-14T19:28:30.6519797Z 	updating dependency infos of picodrive_libretro-1.92_20230811
2025-06-14T19:28:30.6520360Z 	updating dependency infos of pigz-2.8
2025-06-14T19:28:30.6520802Z 	updating dependency infos of pillow-9.2.0
2025-06-14T19:28:30.6521422Z 	updating dependency infos of pimcommon-23.08.5
2025-06-14T19:28:30.6521853Z 	pin8-1.0 is still marked as untested on target architecture
2025-06-14T19:28:30.6522206Z 	updating dependency infos of pinentry-1.2.1
2025-06-14T19:28:30.6522471Z 	updating dependency infos of pingus-0.7.6
2025-06-14T19:28:30.6522726Z 	updating dependency infos of piozone-1.0
2025-06-14T19:28:30.6522989Z 	updating dependency infos of pip-23.2.1
2025-06-14T19:28:30.6523247Z 	updating dependency infos of pipepanic-0.1.3
2025-06-14T19:28:30.6523519Z 	updating dependency infos of pixman-0.42.2
2025-06-14T19:28:30.6523776Z 	updating dependency infos of pjdfstest-0.1
2025-06-14T19:28:30.6524051Z 	updating dependency infos of pkcs11_helper-1.30.0
2025-06-14T19:28:30.6524333Z 	updating dependency infos of pkgconf-1.5.3
2025-06-14T19:28:30.6524595Z 	updating dependency infos of pkgconfig-0.29.2
2025-06-14T19:28:30.6524866Z 	updating dependency infos of pkgdiff-1.7.2
2025-06-14T19:28:30.6525119Z 	updating dependency infos of plasma-5.115.0
2025-06-14T19:28:30.6525407Z 	updating dependency infos of plasma_activities6-6.3.4
2025-06-14T19:28:30.6525743Z 	updating dependency infos of plasma_activities_stats6-6.3.4
2025-06-14T19:28:30.6526120Z 	plee_the_bear-0.7.1 is still marked as untested on target architecture
2025-06-14T19:28:30.6526510Z 	plee_the_bear-0.7.0 is still marked as untested on target architecture
2025-06-14T19:28:30.6526826Z 	updating dependency infos of plib-1.8.5
2025-06-14T19:28:30.6527224Z 	updating dependency infos of plotutils-2.6
2025-06-14T19:28:30.6527493Z 	updating dependency infos of pluggy-1.0.0
2025-06-14T19:28:30.6527751Z 	updating dependency infos of ply-3.11
2025-06-14T19:28:30.6527996Z 	updating dependency infos of pmx-3.0.0
2025-06-14T19:28:30.6528293Z 	pnet-0.8.0 is still marked as untested on target architecture
2025-06-14T19:28:30.6528616Z 	updating dependency infos of png2ico-2002.12.08
2025-06-14T19:28:30.6528906Z 	updating dependency infos of pngcrush-1.8.13
2025-06-14T19:28:30.6529181Z 	updating dependency infos of pnglite-0.1.17
2025-06-14T19:28:30.6529442Z 	updating dependency infos of pngquant-2.7.2
2025-06-14T19:28:30.6529701Z 	updating dependency infos of poco-1.12.4
2025-06-14T19:28:30.6529954Z 	updating dependency infos of podofo-0.10.3
2025-06-14T19:28:30.6530212Z 	updating dependency infos of poezio-0.14
2025-06-14T19:28:30.6530473Z 	updating dependency infos of pogger-0.0.1~git
2025-06-14T19:28:30.6530797Z 	updating dependency infos of pokemini_libretro-0.60_20241021
2025-06-14T19:28:30.6531269Z 	updating dependency infos of polyclipping-6.4.2
2025-06-14T19:28:30.6531557Z 	updating dependency infos of ponpokodiff-0.5.1
2025-06-14T19:28:30.6531853Z 	updating dependency infos of ponscripter-20111009
2025-06-14T19:28:30.6532137Z 	updating dependency infos of ponyexpress-0.2
2025-06-14T19:28:30.6532416Z 	updating dependency infos of poppler22-22.01.0
2025-06-14T19:28:30.6532687Z 	updating dependency infos of poppler23-23.12.0
2025-06-14T19:28:30.6532964Z 	updating dependency infos of poppler24-24.12.0
2025-06-14T19:28:30.6533232Z 	updating dependency infos of poppler25-25.04.0
2025-06-14T19:28:30.6533513Z 	updating dependency infos of poppler_data-0.4.12
2025-06-14T19:28:30.6533791Z 	updating dependency infos of popt-1.16
2025-06-14T19:28:30.6534052Z 	updating dependency infos of portaudio-19.07.00
2025-06-14T19:28:30.6534330Z 	updating dependency infos of portmidi-2.0.4
2025-06-14T19:28:30.6534757Z 	updating dependency infos of portsmf-239
2025-06-14T19:28:30.6535034Z 	recipe for posixtestsuite-1.5.2 is still broken:
2025-06-14T19:28:30.6535402Z 	Error: package posixtestsuite-1.5.2 cannot be built for architecture x86_64
2025-06-14T19:28:30.6535774Z 	updating dependency infos of postal-1.0.0
2025-06-14T19:28:30.6536086Z 	postfix-3.9.1 is still marked as untested on target architecture
2025-06-14T19:28:30.6536420Z 	updating dependency infos of postgresql-9.6.10
2025-06-14T19:28:30.6536704Z 	updating dependency infos of postgresql11-11.1
2025-06-14T19:28:30.6536977Z 	updating dependency infos of postgresql12-12.0
2025-06-14T19:28:30.6537240Z 	updating dependency infos of potrace-1.16
2025-06-14T19:28:30.6537524Z 	updating dependency infos of povray-3.7.0.10
2025-06-14T19:28:30.6537794Z 	updating dependency infos of powermanga-0.93.1
2025-06-14T19:28:30.6538073Z 	updating dependency infos of ppsspp-1.18.1
2025-06-14T19:28:30.6538339Z 	updating dependency infos of ppviewer-1.0.0
2025-06-14T19:28:30.6538614Z 	updating dependency infos of prboom_plus-2.6.66
2025-06-14T19:28:30.6538902Z 	updating dependency infos of premake4-4.4.beta5
2025-06-14T19:28:30.6539189Z 	updating dependency infos of premake5-5.0.0~beta2
2025-06-14T19:28:30.6539535Z 	previous-3.1~svn is still marked as untested on target architecture
2025-06-14T19:28:30.6539860Z 	updating dependency infos of primegen-0.97
2025-06-14T19:28:30.6540124Z 	updating dependency infos of primesieve-7.4
2025-06-14T19:28:30.6540390Z 	updating dependency infos of prison-5.115.0
2025-06-14T19:28:30.6540648Z 	updating dependency infos of prison6-6.13.0
2025-06-14T19:28:30.6540908Z 	updating dependency infos of privoxy-3.0.34
2025-06-14T19:28:30.6541388Z 	updating dependency infos of proj-9.3.0
2025-06-14T19:28:30.6541684Z 	updating dependency infos of projectconceptor-0.1.1
2025-06-14T19:28:30.6541991Z 	updating dependency infos of prompt_toolkit-3.0.39
2025-06-14T19:28:30.6542287Z 	updating dependency infos of protobuf-3.20.1
2025-06-14T19:28:30.6542564Z 	updating dependency infos of protobuf21-3.10.1
2025-06-14T19:28:30.6542845Z 	updating dependency infos of protobuf24-3.13.0
2025-06-14T19:28:30.6543242Z 	updating dependency infos of protobuf28-3.17.2
2025-06-14T19:28:30.6543575Z 	protrekkr-2.5.4 is still marked as untested on target architecture
2025-06-14T19:28:32.1619316Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2450324Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2464088Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2477912Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2491937Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2505717Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2519498Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2533725Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2547353Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2560965Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2574954Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2588624Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2602439Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2616688Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2630357Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2645111Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2659213Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2673411Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2687383Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2701520Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2715408Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2729143Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2743912Z packageEntries: warning: "tools" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2758244Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2772361Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2786452Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2800598Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2814672Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2828497Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2842544Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2856599Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2871274Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2886039Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2899948Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2914216Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2928093Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2942345Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2956413Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2970213Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2984257Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.2998300Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.3012279Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.3026347Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.3039677Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.3053244Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.3067007Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.3080733Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.3094450Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.3107836Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.3121604Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.3135132Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:32.3148594Z packageEntries: warning: "devel" doesn't seem to be a valid package suffix.
2025-06-14T19:28:33.1210466Z 	updating dependency infos of proxychains_ng-4.14~git
2025-06-14T19:28:33.1211314Z 	updating dependency infos of ps2eps-1.70
2025-06-14T19:28:33.1211835Z 	updating dependency infos of psi_plus-1.5.1646
2025-06-14T19:28:33.1212358Z 	updating dependency infos of psiconv-0.9.9
2025-06-14T19:28:33.1212901Z 	updating dependency infos of psqlodbc-09.03.0400
2025-06-14T19:28:33.1213755Z 	updating dependency infos of psutil-6.0.0
2025-06-14T19:28:33.1214266Z 	updating dependency infos of psutils-3.3.9
2025-06-14T19:28:33.1214757Z 	updating dependency infos of ptex-2.1.28
2025-06-14T19:28:33.1215319Z 	updating dependency infos of puae_libretro-2.6.1_20250415
2025-06-14T19:28:33.1215897Z 	updating dependency infos of puckman-1.0~git
2025-06-14T19:28:33.1216403Z 	updating dependency infos of pugixml-1.11.4
2025-06-14T19:28:33.1216907Z 	updating dependency infos of pulseview-0.4.2
2025-06-14T19:28:33.1217399Z 	updating dependency infos of puremagic-1.27
2025-06-14T19:28:33.1217890Z 	updating dependency infos of puri-0.3.9.1
2025-06-14T19:28:33.1218411Z 	updating dependency infos of purple_discord-20240930
2025-06-14T19:28:33.1218976Z 	updating dependency infos of purple_matrix-0.1.0
2025-06-14T19:28:33.1219496Z 	updating dependency infos of purpose-5.115.0
2025-06-14T19:28:33.1220002Z 	updating dependency infos of purpose6-6.13.0
2025-06-14T19:28:33.1220483Z 	updating dependency infos of putty-0.80
2025-06-14T19:28:33.1220953Z 	updating dependency infos of pv-1.6.6
2025-06-14T19:28:33.1221596Z 	updating dependency infos of pwgen-2.08
2025-06-14T19:28:33.1222049Z 	updating dependency infos of py-1.11.0
2025-06-14T19:28:33.1222507Z 	updating dependency infos of pyasn1-0.4.8
2025-06-14T19:28:33.1223007Z 	updating dependency infos of pyasn1_modules-0.2.8
2025-06-14T19:28:33.1223531Z 	updating dependency infos of pybind11-2.13.6
2025-06-14T19:28:33.1224009Z 	updating dependency infos of pycairo-1.27.0
2025-06-14T19:28:33.1224484Z 	updating dependency infos of pycares-3.1.1
2025-06-14T19:28:33.1225036Z 	updating dependency infos of pycharm_community_bin-2023.3.5
2025-06-14T19:28:33.1225621Z 	updating dependency infos of pycparser-2.21
2025-06-14T19:28:33.1226112Z 	updating dependency infos of pycrypto-2.6.1
2025-06-14T19:28:33.1226618Z 	updating dependency infos of pycryptodome-3.17
2025-06-14T19:28:33.1227152Z 	updating dependency infos of pycryptodomex-3.17
2025-06-14T19:28:33.1227643Z 	updating dependency infos of pycurl-7.45.2
2025-06-14T19:28:33.1228320Z 	updating dependency infos of pyenchant-3.2.2
2025-06-14T19:28:33.1228797Z 	updating dependency infos of pyenet-20221216
2025-06-14T19:28:33.1229250Z 	updating dependency infos of pygame-2.0.0
2025-06-14T19:28:33.1229675Z 	updating dependency infos of pygments-2.14.0
2025-06-14T19:28:33.1230121Z 	updating dependency infos of pygobject-3.44.1
2025-06-14T19:28:33.1230568Z 	updating dependency infos of pyjwt-2.4.0
2025-06-14T19:28:33.1230990Z 	updating dependency infos of pylzma-0.5.0
2025-06-14T19:28:33.1231602Z 	updating dependency infos of pymupdf-1.20.2
2025-06-14T19:28:33.1232042Z 	updating dependency infos of pynacl-1.5.0
2025-06-14T19:28:33.1232490Z 	updating dependency infos of pyparsing-3.1.2
2025-06-14T19:28:33.1232924Z 	updating dependency infos of pypdf-4.3.1
2025-06-14T19:28:33.1233391Z 	updating dependency infos of pyproject_hooks-1.1.0
2025-06-14T19:28:33.1233923Z 	updating dependency infos of pyproject_metadata-0.7.1
2025-06-14T19:28:33.1234408Z 	updating dependency infos of pyqt5-5.15.11
2025-06-14T19:28:33.1234858Z 	updating dependency infos of pyqt5_sip-12.15.0
2025-06-14T19:28:33.1235305Z 	updating dependency infos of pyqt6-6.8.0
2025-06-14T19:28:33.1235739Z 	updating dependency infos of pyqt6_sip-13.8.0
2025-06-14T19:28:33.1236193Z 	updating dependency infos of pyqt_builder-1.17.2
2025-06-14T19:28:33.1236701Z 	updating dependency infos of pyqtwebengine5-5.15.6
2025-06-14T19:28:33.1237202Z 	updating dependency infos of pyrsistent-0.17.3
2025-06-14T19:28:33.1237692Z 	updating dependency infos of pyserial-3.5~20211205
2025-06-14T19:28:33.1238169Z 	updating dependency infos of pystring-1.1.4
2025-06-14T19:28:33.1238633Z 	updating dependency infos of pystring0-1.1.3_git
2025-06-14T19:28:33.1239101Z 	updating dependency infos of pytest-7.3.1
2025-06-14T19:28:33.1239622Z 	updating dependency infos of pytest_datafiles-3.0.0
2025-06-14T19:28:33.1240137Z 	updating dependency infos of pytest_mock-3.10.0
2025-06-14T19:28:33.1240785Z 	updating dependency infos of pytest_relaxed-1.1.5
2025-06-14T19:28:33.1241450Z 	updating dependency infos of python3.10-3.10.18
2025-06-14T19:28:33.1241938Z 	updating dependency infos of python3.11-3.11.12
2025-06-14T19:28:33.1242412Z 	updating dependency infos of python3.12-3.12.10
2025-06-14T19:28:33.1242887Z 	updating dependency infos of python3.13-3.13.3
2025-06-14T19:28:33.1243367Z 	updating dependency infos of python3.14-3.14.0~b2
2025-06-14T19:28:33.1243873Z 	updating dependency infos of python3.9-3.9.22
2025-06-14T19:28:33.1244378Z 	updating dependency infos of python_graphviz-0.20.1
2025-06-14T19:28:33.1244891Z 	updating dependency infos of python_ly-0.9.7
2025-06-14T19:28:33.1245403Z 	updating dependency infos of python_markdown_math-0.8
2025-06-14T19:28:33.1245948Z 	updating dependency infos of python_pkgconfig-1.5.5
2025-06-14T19:28:33.1246451Z 	updating dependency infos of python_poppler_qt5-21.3.0
2025-06-14T19:28:33.1246769Z 	updating dependency infos of pythonzeroconf-0.29.0
2025-06-14T19:28:33.1247071Z 	updating dependency infos of pytz-2023.3
2025-06-14T19:28:33.1247327Z 	updating dependency infos of pyyaml-6.0
2025-06-14T19:28:33.1247582Z 	updating dependency infos of pyzmq-25.1.2
2025-06-14T19:28:33.1247866Z 	q-1.1 is still marked as broken on target architecture
2025-06-14T19:28:33.1248163Z 	updating dependency infos of qalculate_qt-5.5.1
2025-06-14T19:28:33.1248430Z 	updating dependency infos of qbe-1.2
2025-06-14T19:28:33.1248685Z 	updating dependency infos of qbittorrent-4.3.1
2025-06-14T19:28:33.1248951Z 	updating dependency infos of qbs-1.13.0
2025-06-14T19:28:33.1249200Z 	updating dependency infos of qca_qt5-2.3.10
2025-06-14T19:28:33.1249457Z 	updating dependency infos of qca_qt6-2.3.10
2025-06-14T19:28:33.1249724Z 	updating dependency infos of qcachegrind-21.08.2
2025-06-14T19:28:33.1249999Z 	updating dependency infos of qcad-3.26.4.12
2025-06-14T19:28:33.1250256Z 	updating dependency infos of qcoro_qt5-0.11.0
2025-06-14T19:28:33.1250529Z 	updating dependency infos of qcoro_qt6-0.11.0
2025-06-14T19:28:33.1250797Z 	updating dependency infos of qdirstat-1.4
2025-06-14T19:28:33.1251414Z 	updating dependency infos of qelectrotech-0.7.0
2025-06-14T19:28:33.1251888Z 	qemacs-0.4.1~pre20170225 is still marked as untested on target architecture
2025-06-14T19:28:33.1252237Z 	updating dependency infos of qemu-8.2.2
2025-06-14T19:28:33.1252498Z 	updating dependency infos of qgis-3.24.3
2025-06-14T19:28:33.1252745Z 	updating dependency infos of qgit-2.9
2025-06-14T19:28:33.1253012Z 	updating dependency infos of qhttpengine-1.0.1
2025-06-14T19:28:33.1253280Z 	updating dependency infos of qhull-8.0.2
2025-06-14T19:28:33.1253546Z 	updating dependency infos of qmdnsengine-0.1.0
2025-06-14T19:28:33.1253840Z 	updating dependency infos of qml_box2d_qt5-20240415
2025-06-14T19:28:33.1254136Z 	updating dependency infos of qml_box2d_qt6-20240415
2025-06-14T19:28:33.1254417Z 	updating dependency infos of qmmp-2.2.6
2025-06-14T19:28:33.1254690Z 	updating dependency infos of qmmp_plugin_pack-2.2.1
2025-06-14T19:28:33.1254987Z 	updating dependency infos of qmodmaster-0.5.2
2025-06-14T19:28:33.1255261Z 	updating dependency infos of qmplay2-25.01.19
2025-06-14T19:28:33.1255535Z 	updating dependency infos of qpageview-0.6.2
2025-06-14T19:28:33.1255811Z 	updating dependency infos of qpdfview-0.4.18
2025-06-14T19:28:33.1256073Z 	updating dependency infos of qputty-506
2025-06-14T19:28:33.1256369Z 	updating dependency infos of qqc2_desktop_style-5.115.0
2025-06-14T19:28:33.1256691Z 	updating dependency infos of qqc2_desktop_style6-6.13.0
2025-06-14T19:28:33.1257011Z 	updating dependency infos of qr_code_generator-1.8.0
2025-06-14T19:28:33.1257291Z 	updating dependency infos of qrcode-7.2
2025-06-14T19:28:33.1257546Z 	updating dependency infos of qrencode-4.1.1
2025-06-14T19:28:33.1257814Z 	updating dependency infos of qrencode_kdl-3.4.4
2025-06-14T19:28:33.1258101Z 	updating dependency infos of qscintilla-2.11.6
2025-06-14T19:28:33.1258412Z 	qscope-2.0 is still marked as broken on target architecture
2025-06-14T19:28:33.1258846Z 	updating dependency infos of qsolocards-0.99.1
2025-06-14T19:28:33.1259129Z 	updating dependency infos of qsystray-5.15.2.14
2025-06-14T19:28:33.1259390Z 	updating dependency infos of qt5-5.15.16
2025-06-14T19:28:33.1259706Z 	qt6_3d-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1260005Z 	updating dependency infos of qt6_3d-6.7.2
2025-06-14T19:28:33.1260319Z 	qt6_5compat-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1260645Z 	updating dependency infos of qt6_5compat-6.7.2
2025-06-14T19:28:33.1260961Z 	qt6_base-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1261695Z 	updating dependency infos of qt6_base-6.7.2
2025-06-14T19:28:33.1262020Z 	qt6_charts-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1262342Z 	updating dependency infos of qt6_charts-6.7.2
2025-06-14T19:28:33.1262688Z 	qt6_connectivity-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1263065Z 	updating dependency infos of qt6_connectivity-6.7.2
2025-06-14T19:28:33.1263418Z 	qt6_datavis3d-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1263766Z 	updating dependency infos of qt6_datavis3d-6.7.2
2025-06-14T19:28:33.1264108Z 	qt6_declarative-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1264469Z 	updating dependency infos of qt6_declarative-6.7.2
2025-06-14T19:28:33.1264792Z 	qt6_doc-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1265101Z 	updating dependency infos of qt6_doc-6.7.2
2025-06-14T19:28:33.1265420Z 	qt6_examples-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1265751Z 	updating dependency infos of qt6_examples-6.7.2
2025-06-14T19:28:33.1266094Z 	qt6_imageformats-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1266450Z 	updating dependency infos of qt6_imageformats-6.7.2
2025-06-14T19:28:33.1266744Z 	updating dependency infos of qt6_jdenticon-0.3.1
2025-06-14T19:28:33.1267076Z 	qt6_location-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1267538Z 	updating dependency infos of qt6_location-6.7.2
2025-06-14T19:28:33.1267869Z 	qt6_lottie-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1268355Z 	updating dependency infos of qt6_lottie-6.7.2
2025-06-14T19:28:33.1268867Z 	qt6_multimedia-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1269223Z 	updating dependency infos of qt6_multimedia-6.7.2
2025-06-14T19:28:33.1269576Z 	qt6_networkauth-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1269929Z 	updating dependency infos of qt6_networkauth-6.7.2
2025-06-14T19:28:33.1270284Z 	qt6_positioning-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1270640Z 	updating dependency infos of qt6_positioning-6.7.2
2025-06-14T19:28:33.1270974Z 	qt6_quick3d-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1271507Z 	updating dependency infos of qt6_quick3d-6.7.2
2025-06-14T19:28:33.1271870Z 	qt6_quick3dphysics-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1272257Z 	updating dependency infos of qt6_quick3dphysics-6.7.2
2025-06-14T19:28:33.1272628Z 	qt6_quicktimeline-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1273003Z 	updating dependency infos of qt6_quicktimeline-6.7.2
2025-06-14T19:28:33.1273344Z 	qt6_scxml-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1273667Z 	updating dependency infos of qt6_scxml-6.7.2
2025-06-14T19:28:33.1273993Z 	qt6_sensors-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1274322Z 	updating dependency infos of qt6_sensors-6.7.2
2025-06-14T19:28:33.1274662Z 	qt6_serialport-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1275012Z 	updating dependency infos of qt6_serialport-6.7.2
2025-06-14T19:28:33.1275367Z 	qt6_shadertools-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:33.1275869Z 	updating dependency infos of qt6_shadertools-6.7.2
2025-06-14T19:28:33.6932200Z packageEntries: warning: "qt6" doesn't seem to be a valid package suffix.
2025-06-14T19:28:34.8466402Z 	qt6_speech-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:34.8467141Z 	updating dependency infos of qt6_speech-6.7.2
2025-06-14T19:28:34.8467742Z 	qt6_svg-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:34.8468323Z 	updating dependency infos of qt6_svg-6.7.2
2025-06-14T19:28:34.8468917Z 	qt6_tools-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:34.8469513Z 	updating dependency infos of qt6_tools-6.7.2
2025-06-14T19:28:34.8470154Z 	qt6_translations-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:34.8470837Z 	updating dependency infos of qt6_translations-6.7.2
2025-06-14T19:28:34.8471672Z 	qt6_webchannel-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:34.8472372Z 	updating dependency infos of qt6_webchannel-6.7.2
2025-06-14T19:28:34.8473042Z 	qt6_websockets-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:34.8473732Z 	updating dependency infos of qt6_websockets-6.7.2
2025-06-14T19:28:34.8474374Z 	qt6_webview-6.9.0 is still marked as untested on target architecture
2025-06-14T19:28:34.8475011Z 	updating dependency infos of qt6_webview-6.7.2
2025-06-14T19:28:34.8475540Z 	updating dependency infos of qt_creator-16.0.2
2025-06-14T19:28:34.8476043Z 	updating dependency infos of qtav-1.13.0
2025-06-14T19:28:34.8476560Z 	updating dependency infos of qtdropbox-20151109
2025-06-14T19:28:34.8477130Z 	updating dependency infos of qthaikuplugins-5.15.2.38
2025-06-14T19:28:34.8477713Z 	updating dependency infos of qtkeychain-0.15.0
2025-06-14T19:28:34.8478256Z 	updating dependency infos of qtkeychain_qt6-0.15.0
2025-06-14T19:28:34.8478782Z 	updating dependency infos of qtox-1.17.6
2025-06-14T19:28:34.8479319Z 	updating dependency infos of qtpbfimageplugin-2.3
2025-06-14T19:28:34.8480142Z 	recipe for qtquickcontrols2-5.15.2 is still broken:
2025-06-14T19:28:34.8480661Z 	Error: No match found for license FDL
2025-06-14T19:28:34.8481345Z 	Error: Valid license filenames included with Haiku are:
2025-06-14T19:28:34.8484270Z 	Error: Anti-Grain Geometry, Apache v2, Artistic, Artistic v2.0, BSD (2-clause), BSD (3-clause), BSD (4-clause), Be Sample Code License, Bullet, CDDL v1, CQuantizer, DEC, GLUT (Mark Kilgard), GNU GPL font exception, GNU GPL v1, GNU GPL v2, GNU GPL v3, GNU LGPL v2, GNU LGPL v2.1, GNU LGPL v3, GPC, Intel (2xxx firmware), Intel (ACPICA), Intel (firmware), LibHTTPd, LibJPEG, LibPNG, MAPM, MIT, MIT (no promotion), MPL v1.1, MPL v2.0, Marvell (firmware), OpenGroup, PDFlib Lite, Public Domain, Ralink (firmware), SGI Free B, SIL Open Font License v1.1, Zlib
2025-06-14T19:28:34.8487491Z 	Error: (in /runner/work/haikuports/haikuports/dev-qt/qtquickcontrols2/qtquickcontrols2-5.15.2.recipe)
2025-06-14T19:28:34.8488405Z 	updating dependency infos of qtstyleplugins-5.0.0~git
2025-06-14T19:28:34.8489056Z 	qtwebengine-5.15.18 is still marked as untested on target architecture
2025-06-14T19:28:34.8489681Z 	updating dependency infos of qtwebengine_bin-5.15.18
2025-06-14T19:28:34.8490252Z 	updating dependency infos of qtwebkit-5.212.0~pre20200924
2025-06-14T19:28:34.8490768Z 	recipe for quake3-0.6.1 is still broken:
2025-06-14T19:28:34.8491691Z 	Error: package quake3-0.6.1 cannot be built for architecture x86_64
2025-06-14T19:28:34.8492290Z 	updating dependency infos of quakespasm-0.96.3
2025-06-14T19:28:34.8492780Z 	updating dependency infos of quassel-0.15~pre
2025-06-14T19:28:34.8493276Z 	updating dependency infos of quaternion-0.0.97.1
2025-06-14T19:28:34.8493755Z 	updating dependency infos of quazip-0.8.1
2025-06-14T19:28:34.8494215Z 	updating dependency infos of quazip1_qt5-1.4
2025-06-14T19:28:34.8494685Z 	updating dependency infos of quazip1_qt6-1.4
2025-06-14T19:28:34.8495148Z 	updating dependency infos of querywatcher-1.4
2025-06-14T19:28:34.8495832Z 	updating dependency infos of quicklaunch-1.8
2025-06-14T19:28:34.8496297Z 	recipe for quickres-20011026 is still broken:
2025-06-14T19:28:34.8496931Z 	Error: package quickres-20011026 cannot be built for architecture x86_64
2025-06-14T19:28:34.8497629Z 	quicktour-0.2 is still marked as broken on target architecture
2025-06-14T19:28:34.8498165Z 	updating dependency infos of quilt-0.65
2025-06-14T19:28:34.8498606Z 	updating dependency infos of quimup-1.4.3
2025-06-14T19:28:34.8499059Z 	updating dependency infos of quiterss-0.19.4
2025-06-14T19:28:34.8499542Z 	updating dependency infos of qutebrowser-2.5.4
2025-06-14T19:28:34.8500001Z 	updating dependency infos of qview-6.0
2025-06-14T19:28:34.8500432Z 	updating dependency infos of qvim-8.0.197
2025-06-14T19:28:34.8500872Z 	updating dependency infos of qwinff-0.2.1
2025-06-14T19:28:34.8501492Z 	updating dependency infos of qwt-6.2.0
2025-06-14T19:28:34.8501924Z 	updating dependency infos of qxlsx-1.5.0
2025-06-14T19:28:34.8502377Z 	updating dependency infos of r-4.5.0
2025-06-14T19:28:34.8502820Z 	updating dependency infos of r2dec_js-5.9.8
2025-06-14T19:28:34.8503287Z 	updating dependency infos of r2ghidra-5.9.4
2025-06-14T19:28:34.8503809Z 	updating dependency infos of raceintospace-v2.0~git
2025-06-14T19:28:34.8504320Z 	updating dependency infos of radare2-5.9.8
2025-06-14T19:28:34.8504748Z 	updating dependency infos of ragel-7.0.0.10
2025-06-14T19:28:34.8505088Z 	updating dependency infos of ralink_wifi_firmwares-2023_08_04
2025-06-14T19:28:34.8505427Z 	updating dependency infos of randomizer-1.2.2
2025-06-14T19:28:34.8505712Z 	updating dependency infos of range_v3-0.11.0
2025-06-14T19:28:34.8505976Z 	updating dependency infos of ranger-1.9.3
2025-06-14T19:28:34.8506264Z 	updating dependency infos of rapidjson-1.1.1~20250205
2025-06-14T19:28:34.8506551Z 	updating dependency infos of raptor-2.0.15
2025-06-14T19:28:34.8506808Z 	updating dependency infos of rasm-2.0
2025-06-14T19:28:34.8507056Z 	updating dependency infos of rasqal-0.9.33
2025-06-14T19:28:34.8507308Z 	updating dependency infos of rav1e-0.7.1
2025-06-14T19:28:34.8507701Z 	updating dependency infos of rawaes-1.1
2025-06-14T19:28:34.8507972Z 	updating dependency infos of rawtherapee-5.9
2025-06-14T19:28:34.8508236Z 	updating dependency infos of raylib-5.0
2025-06-14T19:28:34.8508526Z 	rcs-5.9.4 is still marked as untested on target architecture
2025-06-14T19:28:34.8508890Z 	rdesktop-1.8.0 is still marked as untested on target architecture
2025-06-14T19:28:34.8509206Z 	updating dependency infos of re2-2022.06.01
2025-06-14T19:28:34.8509463Z 	updating dependency infos of re2c-2.0.3
2025-06-14T19:28:34.8509729Z 	updating dependency infos of readline-8.2.013
2025-06-14T19:28:34.8510052Z 	readline6-6.3.8 is still marked as untested on target architecture
2025-06-14T19:28:34.8510382Z 	updating dependency infos of readline7-7.0.5
2025-06-14T19:28:34.8510698Z 	updating dependency infos of realtek_wifi_firmwares-2019_01_02
2025-06-14T19:28:34.8511010Z 	recipe for rebar-2.5.1 is still broken:
2025-06-14T19:28:34.8511745Z 	Error: package rebar-2.5.1 cannot be built for architecture x86_64
2025-06-14T19:28:34.8512233Z 	rebol-git_25033f897b is still marked as broken on target architecture
2025-06-14T19:28:34.8512597Z 	updating dependency infos of recastnavigation-1.6.0
2025-06-14T19:28:34.8512933Z 	recibe-1.0b1 is still marked as untested on target architecture
2025-06-14T19:28:34.8513266Z 	updating dependency infos of recursive-1.027~beta
2025-06-14T19:28:34.8513540Z 	updating dependency infos of redasm-2.1.1
2025-06-14T19:28:34.8513792Z 	updating dependency infos of redis-5.0.6
2025-06-14T19:28:34.8514045Z 	updating dependency infos of redland-1.0.17
2025-06-14T19:28:34.8514322Z 	updating dependency infos of redoflacs-0.31~pre
2025-06-14T19:28:34.8514595Z 	updating dependency infos of ref_util-0.204
2025-06-14T19:28:34.8514866Z 	updating dependency infos of ref_util_xs-0.117
2025-06-14T19:28:34.8515135Z 	updating dependency infos of regex-2020.1.8
2025-06-14T19:28:34.8515550Z 	updating dependency infos of regexp_common-2024080801
2025-06-14T19:28:34.8515841Z 	updating dependency infos of rehex-0.62.1
2025-06-14T19:28:34.8516099Z 	updating dependency infos of remember-1.0.0
2025-06-14T19:28:34.8516421Z 	updating dependency infos of reminiscence_libretro-0.3.6_20241021
2025-06-14T19:28:34.8516745Z 	updating dependency infos of remmina-1.4.29
2025-06-14T19:28:34.8517016Z 	updating dependency infos of remotecontrol-1.1
2025-06-14T19:28:34.8517387Z 	updating dependency infos of rename-3.9.0
2025-06-14T19:28:34.8517637Z 	updating dependency infos of renga-1.27
2025-06-14T19:28:34.8517885Z 	recipe for replicat-1.06 is still broken:
2025-06-14T19:28:34.8518129Z 	Error: No match found for license unknown
2025-06-14T19:28:34.8518413Z 	Error: Valid license filenames included with Haiku are:
2025-06-14T19:28:34.8520007Z 	Error: Anti-Grain Geometry, Apache v2, Artistic, Artistic v2.0, BSD (2-clause), BSD (3-clause), BSD (4-clause), Be Sample Code License, Bullet, CDDL v1, CQuantizer, DEC, GLUT (Mark Kilgard), GNU GPL font exception, GNU GPL v1, GNU GPL v2, GNU GPL v3, GNU LGPL v2, GNU LGPL v2.1, GNU LGPL v3, GPC, Intel (2xxx firmware), Intel (ACPICA), Intel (firmware), LibHTTPd, LibJPEG, LibPNG, MAPM, MIT, MIT (no promotion), MPL v1.1, MPL v2.0, Marvell (firmware), OpenGroup, PDFlib Lite, Public Domain, Ralink (firmware), SGI Free B, SIL Open Font License v1.1, Zlib
2025-06-14T19:28:34.8521900Z 	Error: (in /runner/work/haikuports/haikuports/haiku-misc/replicat/replicat-1.06.recipe)
2025-06-14T19:28:34.8522341Z 	updating dependency infos of reportlab-3.6.9
2025-06-14T19:28:34.8522609Z 	updating dependency infos of requests-2.27.1
2025-06-14T19:28:34.8522899Z 	updating dependency infos of requests_futures-1.0.0
2025-06-14T19:28:34.8523260Z 	resourceedit-1.0_git is still marked as untested on target architecture
2025-06-14T19:28:34.8523603Z 	updating dependency infos of resourcer-3.0
2025-06-14T19:28:34.8523866Z 	updating dependency infos of retawq-0.2.6c
2025-06-14T19:28:34.8524123Z 	updating dependency infos of retext-8.0.2
2025-06-14T19:28:34.8524390Z 	updating dependency infos of retro-2021.4
2025-06-14T19:28:34.8524800Z 	updating dependency infos of retroarch-1.20.0
2025-06-14T19:28:34.8525117Z 	updating dependency infos of retroarch_assets-0_20250321
2025-06-14T19:28:34.8525425Z 	updating dependency infos of retroshare-0.6.6
2025-06-14T19:28:34.8525686Z 	updating dependency infos of rez-108
2025-06-14T19:28:34.8525930Z 	recipe for rezerwar-0.4.2 is still broken:
2025-06-14T19:28:34.8526255Z 	Error: package rezerwar-0.4.2 cannot be built for architecture x86_64
2025-06-14T19:28:34.8526604Z 	updating dependency infos of rhapsody_irc-0.28b
2025-06-14T19:28:34.8526873Z 	updating dependency infos of rhash-1.4.4
2025-06-14T19:28:34.8527294Z 	updating dependency infos of rhash0-1.4.2
2025-06-14T19:28:34.8527685Z 	updating dependency infos of ri_li-2.0.1
2025-06-14T19:28:34.8527951Z 	updating dependency infos of ripgrep-14.0.1
2025-06-14T19:28:34.8528210Z 	updating dependency infos of rizin-0.7.4
2025-06-14T19:28:34.8528569Z 	updating dependency infos of rkward-0.7.5
2025-06-14T19:28:34.8528833Z 	updating dependency infos of rlwrap-0.46.1
2025-06-14T19:28:34.8529079Z 	updating dependency infos of rman-3.2
2025-06-14T19:28:34.8529338Z 	updating dependency infos of rnnoise-0.4.1~git
2025-06-14T19:28:34.8529624Z 	updating dependency infos of roadfighter-1.0.1269
2025-06-14T19:28:34.8529991Z 	roaraudio-1.0beta12 is still marked as untested on target architecture
2025-06-14T19:28:34.8530332Z 	updating dependency infos of robin_map-0.6.3
2025-06-14T19:28:34.8530612Z 	updating dependency infos of robinhood-1.3~git
2025-06-14T19:28:34.8530878Z 	updating dependency infos of roboto-2.136
2025-06-14T19:28:34.8531307Z 	updating dependency infos of rocksdb-9.10.0
2025-06-14T19:28:34.8531600Z 	updating dependency infos of rocksndiamonds-4.2.0.3
2025-06-14T19:28:34.8531891Z 	updating dependency infos of role_tiny-2.002004
2025-06-14T19:28:34.8532177Z 	updating dependency infos of romannumbers-1.0~git
2025-06-14T19:28:34.8532594Z 	updating dependency infos of routino-3.3.2
2025-06-14T19:28:34.8532870Z 	updating dependency infos of rpcsvc_proto-1.4.3
2025-06-14T19:28:34.8533188Z 	rssavers-0.2 is still marked as broken on target architecture
2025-06-14T19:28:37.1572002Z 	updating dependency infos of rssguard-4.2.1
2025-06-14T19:28:37.1578136Z 	updating dependency infos of rst2pdf-0.102
2025-06-14T19:28:37.1578618Z 	updating dependency infos of rsync-3.2.7
2025-06-14T19:28:37.1579149Z 	rtaudio-5.2.0 is still marked as untested on target architecture
2025-06-14T19:28:37.1579600Z 	updating dependency infos of rtl_sdr-2023.8.25
2025-06-14T19:28:37.1579895Z 	updating dependency infos of rtmidi-5.0.0
2025-06-14T19:28:37.1580189Z 	updating dependency infos of rtmpdump-2.4_20161210
2025-06-14T19:28:37.1580479Z 	updating dependency infos of rtorrent-0.9.8
2025-06-14T19:28:37.1580760Z 	updating dependency infos of rubberband-1.8.2
2025-06-14T19:28:37.1581031Z 	updating dependency infos of ruby-3.2.7
2025-06-14T19:28:37.1581609Z 	updating dependency infos of run_parts-5.17
2025-06-14T19:28:37.1581927Z 	updating dependency infos of runescape_launcher-0.9.0
2025-06-14T19:28:37.1582252Z 	updating dependency infos of runprogram-1.0rc1
2025-06-14T19:28:37.1582568Z 	rust-1.79.0 is still marked as broken on target architecture
2025-06-14T19:28:37.1582873Z 	updating dependency infos of rust_bin-1.83.0
2025-06-14T19:28:37.1583155Z 	updating dependency infos of rust_wasm_bin-1.83.0
2025-06-14T19:28:37.1583432Z 	updating dependency infos of rvvm-0.7~git
2025-06-14T19:28:37.1583693Z 	updating dependency infos of rxtx-2.2_pre2
2025-06-14T19:28:37.1583943Z 	updating dependency infos of s25rttr-0.9.5
2025-06-14T19:28:37.1584202Z 	updating dependency infos of sablotron-1.0.3
2025-06-14T19:28:37.1584534Z 	sagebrush-0~git is still marked as broken on target architecture
2025-06-14T19:28:37.1584900Z 	updating dependency infos of sais-1.6.3~git
2025-06-14T19:28:37.1585161Z 	updating dependency infos of samba-3.6.25
2025-06-14T19:28:37.1585467Z 	samba4-4.20.4 is still marked as untested on target architecture
2025-06-14T19:28:37.1585782Z 	updating dependency infos of samba4-4.20.2
2025-06-14T19:28:37.1586308Z 	updating dependency infos of sameboy_libretro-0.9.0_20240628
2025-06-14T19:28:37.1586618Z 	updating dependency infos of samedi-1.0
2025-06-14T19:28:37.1586892Z 	updating dependency infos of sane_backends-1.3.1
2025-06-14T19:28:37.1587163Z 	updating dependency infos of sanity-0.6
2025-06-14T19:28:37.1587415Z 	updating dependency infos of saptools-2.0.94
2025-06-14T19:28:37.1587680Z 	updating dependency infos of sassc-3.6.2
2025-06-14T19:28:37.1587952Z 	updating dependency infos of sauerbraten-2020.12.29
2025-06-14T19:28:37.1588235Z 	updating dependency infos of savvycan-213
2025-06-14T19:28:37.1588489Z 	updating dependency infos of sawteeth-1.4.1
2025-06-14T19:28:37.1588740Z 	updating dependency infos of sbc-2.0
2025-06-14T19:28:37.1588974Z 	updating dependency infos of sbcl-2.5.5
2025-06-14T19:28:37.1589220Z 	updating dependency infos of sc-7.16_1.1.2
2025-06-14T19:28:37.1589476Z 	updating dependency infos of sc_im-0.8.3
2025-06-14T19:28:37.1589786Z 	scalapack-2.1.0 is still marked as untested on target architecture
2025-06-14T19:28:37.1590108Z 	updating dependency infos of scdoc-1.11.3
2025-06-14T19:28:37.1590381Z 	updating dependency infos of scheherazade_font-1.005
2025-06-14T19:28:37.1590694Z 	updating dependency infos of schismtracker-20240529
2025-06-14T19:28:37.1590985Z 	updating dependency infos of schroedinger-1.0.11
2025-06-14T19:28:37.1591565Z 	updating dependency infos of scintilla-5.3.4
2025-06-14T19:28:37.1591831Z 	updating dependency infos of scipy-1.15.1
2025-06-14T19:28:37.1592088Z 	updating dependency infos of scons-4.6.0
2025-06-14T19:28:37.1592387Z 	scooby-0.9.9 is still marked as broken on target architecture
2025-06-14T19:28:37.1592704Z 	updating dependency infos of scope_guard-0.21
2025-06-14T19:28:37.1592978Z 	updating dependency infos of scotch-6.0.9
2025-06-14T19:28:37.1593220Z 	updating dependency infos of scour-0.38.2
2025-06-14T19:28:37.1593677Z 	scourge-0.21.1 is still marked as untested on target architecture
2025-06-14T19:28:37.1594008Z 	updating dependency infos of scourge_data-0.21.1
2025-06-14T19:28:37.1594350Z 	screen-4.99.0~git is still marked as untested on target architecture
2025-06-14T19:28:37.1594722Z 	screen-4.6.1 is still marked as untested on target architecture
2025-06-14T19:28:37.1595043Z 	updating dependency infos of screenfetch-3.9.1
2025-06-14T19:28:37.1595330Z 	updating dependency infos of screenkeyboard-1.0
2025-06-14T19:28:37.1595613Z 	updating dependency infos of screensavers_ai-1.1
2025-06-14T19:28:37.1595895Z 	updating dependency infos of scribus-1.6.1
2025-06-14T19:28:37.1596174Z 	updating dependency infos of scriptureguide-0.9.1.1
2025-06-14T19:28:37.1596455Z 	updating dependency infos of scummvm-2.9.1
2025-06-14T19:28:37.1596758Z 	updating dependency infos of scummvm_libretro-2.0.0_20220406
2025-06-14T19:28:37.1597073Z 	updating dependency infos of scummvm_tools-2.9.0
2025-06-14T19:28:37.1597338Z 	updating dependency infos of sdcc-4.5.0
2025-06-14T19:28:37.1597591Z 	updating dependency infos of sdl2_gfx-1.0.4
2025-06-14T19:28:37.1597856Z 	updating dependency infos of sdl2_image-2.0.5
2025-06-14T19:28:37.1598122Z 	updating dependency infos of sdl2_mixer-2.8.0
2025-06-14T19:28:37.1598386Z 	updating dependency infos of sdl2_net-2.0.1
2025-06-14T19:28:37.1598640Z 	updating dependency infos of sdl2_pango-0.1.2
2025-06-14T19:28:37.1598931Z 	updating dependency infos of sdl2_sound-2.0.1~06112022
2025-06-14T19:28:37.1599221Z 	updating dependency infos of sdl2_ttf-2.20.2
2025-06-14T19:28:37.1599476Z 	updating dependency infos of sdl_bomber-1.0.4
2025-06-14T19:28:37.1599736Z 	updating dependency infos of sdl_gfx-2.0.26
2025-06-14T19:28:37.1599987Z 	updating dependency infos of sdl_image-1.2.12
2025-06-14T19:28:37.1600265Z 	updating dependency infos of sdl_kitchensink-1.0.9
2025-06-14T19:28:37.1600539Z 	updating dependency infos of sdl_mixer-1.2.12
2025-06-14T19:28:37.1600796Z 	updating dependency infos of sdl_net-1.2.8
2025-06-14T19:28:37.1601049Z 	updating dependency infos of sdl_pango-0.1.2
2025-06-14T19:28:37.1601846Z 	updating dependency infos of sdl_perl-2.548
2025-06-14T19:28:37.1602186Z 	sdl_rtf-0.1.0 is still marked as untested on target architecture
2025-06-14T19:28:37.1602508Z 	updating dependency infos of sdl_sopwith-2.3.0
2025-06-14T19:28:37.1602795Z 	updating dependency infos of sdl_sound-1.0.3
2025-06-14T19:28:37.1603271Z 	updating dependency infos of sdl_ttf-2.0.11
2025-06-14T19:28:37.1603764Z 	updating dependency infos of sdlinvaders-0.7.6
2025-06-14T19:28:37.1604258Z 	sdljoytest-11102003 is still marked as untested on target architecture
2025-06-14T19:28:37.1604609Z 	updating dependency infos of sdllopan-10
2025-06-14T19:28:37.1604962Z 	updating dependency infos of sdlpop-1.22
2025-06-14T19:28:37.1605229Z 	updating dependency infos of sdlscavenger-145.4
2025-06-14T19:28:37.1605503Z 	updating dependency infos of se-3.0.1
2025-06-14T19:28:37.1605739Z 	updating dependency infos of sed-4.9
2025-06-14T19:28:37.1605992Z 	updating dependency infos of seeker-1.0
2025-06-14T19:28:37.1606232Z 	updating dependency infos of seer-2.4
2025-06-14T19:28:37.1606482Z 	updating dependency infos of sequitur-2.2.0
2025-06-14T19:28:37.1606735Z 	updating dependency infos of serd-0.30.16
2025-06-14T19:28:37.1606986Z 	updating dependency infos of serf-1.3.10
2025-06-14T19:28:37.1607253Z 	updating dependency infos of serious_sam-1.10~git
2025-06-14T19:28:37.1607542Z 	recipe for serviceswatcher-1.0.1 is still broken:
2025-06-14T19:28:37.1607924Z 	Error: package serviceswatcher-1.0.1 cannot be built for architecture x86_64
2025-06-14T19:28:37.1608312Z 	recipe for serviceswatcher-1.0 is still broken:
2025-06-14T19:28:37.1608681Z 	Error: package serviceswatcher-1.0 cannot be built for architecture x86_64
2025-06-14T19:28:37.1609049Z 	updating dependency infos of setuptools-68.2.2
2025-06-14T19:28:37.1609341Z 	updating dependency infos of setuptools_rust-1.8.1
2025-06-14T19:28:37.1609638Z 	updating dependency infos of setuptools_scm-7.1.0
2025-06-14T19:28:37.1610067Z 	updating dependency infos of sfxr-1.2.1
2025-06-14T19:28:37.1610327Z 	updating dependency infos of sg3_utils-1.42
2025-06-14T19:28:37.1610573Z 	updating dependency infos of sge-030809
2025-06-14T19:28:37.1610828Z 	updating dependency infos of sgmllib3k-1.0.0
2025-06-14T19:28:37.1611251Z 	updating dependency infos of shaderc-2024.2
2025-06-14T19:28:37.1611618Z 	updating dependency infos of shanty-0.4
2025-06-14T19:28:37.1611886Z 	updating dependency infos of shared_mime_info-1.15
2025-06-14T19:28:37.1612183Z 	updating dependency infos of sharutils-4.15.2
2025-06-14T19:28:37.1612444Z 	updating dependency infos of shc-3.9.6
2025-06-14T19:28:37.1612697Z 	updating dependency infos of shine-3.1.1~20230101
2025-06-14T19:28:37.1613032Z 	shockolate-0.7.7 is still marked as broken on target architecture
2025-06-14T19:28:37.1613411Z 	shotcut-24.11.17 is still marked as untested on target architecture
2025-06-14T19:28:37.1613733Z 	updating dependency infos of shredder-1.0.0
2025-06-14T19:28:37.1614048Z 	sidplayer-4.4 is still marked as broken on target architecture
2025-06-14T19:28:37.1614367Z 	updating dependency infos of sidreloc-1.0
2025-06-14T19:28:37.1614623Z 	updating dependency infos of sigil-0.9.14.2
2025-06-14T19:28:37.1614915Z 	signify-23 is still marked as broken on target architecture
2025-06-14T19:28:37.1615226Z 	updating dependency infos of signond_qt5-8.61
2025-06-14T19:28:37.1615489Z 	updating dependency infos of signond_qt6-8.61
2025-06-14T19:28:37.1615755Z 	updating dependency infos of sigrok_cli-0.7.2
2025-06-14T19:28:37.1616016Z 	updating dependency infos of simdjson-3.11.5
2025-06-14T19:28:37.1616333Z 	simgear-2018.2.2 is still marked as broken on target architecture
2025-06-14T19:28:37.1616690Z 	simh-4.0.0_git is still marked as untested on target architecture
2025-06-14T19:28:37.1617008Z 	recipe for simplebackup-2.0.1 is still broken:
2025-06-14T19:28:37.1617368Z 	Error: package simplebackup-2.0.1 cannot be built for architecture x86_64
2025-06-14T19:28:37.1617720Z 	recipe for simplyvorbis-0.1 is still broken:
2025-06-14T19:28:37.1618183Z 	Error: package simplyvorbis-0.1 cannot be built for architecture x86_64
2025-06-14T19:28:37.1618533Z 	updating dependency infos of simsu-1.4.3
2025-06-14T19:28:37.1618792Z 	updating dependency infos of simulide-0.4.14
2025-06-14T19:28:37.1619058Z 	updating dependency infos of simutrans-123.0.1
2025-06-14T19:28:37.1619349Z 	updating dependency infos of simutrans_pak128-2.8.2
2025-06-14T19:28:37.1619648Z 	updating dependency infos of simutrans_pak64-123.0
2025-06-14T19:28:37.1619928Z 	updating dependency infos of singularity-1.00
2025-06-14T19:28:37.1620232Z 	sinus-0.1.3 is still marked as broken on target architecture
2025-06-14T19:28:37.1620521Z 	updating dependency infos of sip-6.9.0
2025-06-14T19:28:37.1620764Z 	updating dependency infos of six-1.15.0
2025-06-14T19:28:37.1621007Z 	updating dependency infos of skrooge-2.33.0
2025-06-14T19:28:37.1621448Z 	updating dependency infos of skympc-1.6.5
2025-06-14T19:28:37.1621698Z 	updating dependency infos of sl-5.02
2025-06-14T19:28:37.1621942Z 	updating dependency infos of slack++-0
2025-06-14T19:28:37.1622187Z 	updating dependency infos of slang-2.3.3
2025-06-14T19:28:37.1622427Z 	updating dependency infos of slayer-1.0
2025-06-14T19:28:37.1622691Z 	updating dependency infos of slimevolley-2.4.2
2025-06-14T19:28:37.1622957Z 	updating dependency infos of slixmpp-1.8.4
2025-06-14T19:28:37.1623233Z 	updating dependency infos of slunkcrypt-2024_06_08
2025-06-14T19:28:37.1623503Z 	updating dependency infos of smake-1.2.5
2025-06-14T19:28:37.1623805Z 	smjpeg-0.2.1 is still marked as untested on target architecture
2025-06-14T19:28:37.1624115Z 	updating dependency infos of smmap-5.0.1
2025-06-14T19:28:37.1624380Z 	updating dependency infos of smolcloudtools-0.1.1
2025-06-14T19:28:37.1624666Z 	updating dependency infos of smooth-0.9.10
2025-06-14T19:28:37.1624917Z 	updating dependency infos of smpeg-0.4.5
2025-06-14T19:28:37.1625164Z 	updating dependency infos of smpeg2-2.0.0
2025-06-14T19:28:37.1625418Z 	updating dependency infos of smplayer-22.7.0
2025-06-14T19:28:37.1625798Z 	updating dependency infos of smpq-1.6
2025-06-14T19:28:37.1626046Z 	updating dependency infos of smtube-18.11.0
2025-06-14T19:28:37.1626306Z 	updating dependency infos of snappy-1.1.10
2025-06-14T19:28:37.1626558Z 	recipe for snapshot-1.0 is still broken:
2025-06-14T19:28:37.1626873Z 	Error: package snapshot-1.0 cannot be built for architecture x86_64
2025-06-14T19:28:37.1627261Z 	updating dependency infos of snes9x_libretro-1.60_20241021
2025-06-14T19:28:37.1627588Z 	updating dependency infos of snowball_stemmer-2.2.0
2025-06-14T19:28:37.1627889Z 	updating dependency infos of snowballstemmer-2.2.0
2025-06-14T19:28:37.1628163Z 	updating dependency infos of snowman-0.1.3
2025-06-14T19:28:37.1628412Z 	updating dependency infos of sock-0.3.2
2025-06-14T19:28:37.1628709Z 	sockhop-1.13 is still marked as untested on target architecture
2025-06-14T19:28:39.3977480Z 	updating dependency infos of softhsm2-2.5.0
2025-06-14T19:28:39.3978040Z 	updating dependency infos of solarus-1.6.5
2025-06-14T19:28:39.3978455Z 	updating dependency infos of solid-5.115.0
2025-06-14T19:28:39.3978751Z 	updating dependency infos of solid6-6.13.0
2025-06-14T19:28:39.3979038Z 	updating dependency infos of solitaire_mahjong-2.2.4
2025-06-14T19:28:39.3979351Z 	updating dependency infos of sombok-2.4.0
2025-06-14T19:28:39.3979609Z 	updating dependency infos of sonnet-5.115.0
2025-06-14T19:28:39.3979870Z 	updating dependency infos of sonnet6-6.13.0
2025-06-14T19:28:39.3980117Z 	updating dependency infos of sord-0.16.14
2025-06-14T19:28:39.3980368Z 	updating dependency infos of sort_key-1.33
2025-06-14T19:28:39.3980623Z 	updating dependency infos of sortsave-1.1
2025-06-14T19:28:39.3980888Z 	updating dependency infos of sounds_community-0.1
2025-06-14T19:28:39.3981487Z 	updating dependency infos of soupsieve-1.9.5
2025-06-14T19:28:39.3981778Z 	updating dependency infos of source_pro-20191013
2025-06-14T19:28:39.3982087Z 	updating dependency infos of sourcetrail-2019.4.102
2025-06-14T19:28:39.3982370Z 	updating dependency infos of sox-14.4.2
2025-06-14T19:28:39.3982844Z 	updating dependency infos of sox_ng-14.5.0.3
2025-06-14T19:28:39.3983104Z 	updating dependency infos of soxr-0.1.3
2025-06-14T19:28:39.3983354Z 	updating dependency infos of space-1.2
2025-06-14T19:28:39.3983621Z 	updating dependency infos of sparsehash-2.0.4
2025-06-14T19:28:39.3983888Z 	updating dependency infos of spdlog-1.15.0
2025-06-14T19:28:39.3984146Z 	updating dependency infos of specio-0.48
2025-06-14T19:28:39.3984401Z 	updating dependency infos of speech_tools-2.4
2025-06-14T19:28:39.3984681Z 	updating dependency infos of speed_dreams-2.2.3
2025-06-14T19:28:39.3984957Z 	updating dependency infos of speedcrunch-0.12.0
2025-06-14T19:28:39.3985257Z 	updating dependency infos of speedtest_cli-2.1.3
2025-06-14T19:28:39.3985532Z 	updating dependency infos of speex-1.2.1
2025-06-14T19:28:39.3985795Z 	updating dependency infos of speexdsp-1.2.1
2025-06-14T19:28:39.3986054Z 	updating dependency infos of speg-0.3
2025-06-14T19:28:39.3986301Z 	updating dependency infos of sphinx-7.2.6
2025-06-14T19:28:39.3986584Z 	updating dependency infos of sphinx_argparse-0.4.0
2025-06-14T19:28:39.3986884Z 	updating dependency infos of sphinx_rtd_theme-1.2.1
2025-06-14T19:28:39.3987216Z 	updating dependency infos of sphinxcontrib_applehelp-1.0.4
2025-06-14T19:28:39.3987568Z 	updating dependency infos of sphinxcontrib_devhelp-1.0.2
2025-06-14T19:28:39.3987907Z 	updating dependency infos of sphinxcontrib_htmlhelp-2.0.1
2025-06-14T19:28:39.3988238Z 	updating dependency infos of sphinxcontrib_jquery-4.1
2025-06-14T19:28:39.3988555Z 	updating dependency infos of sphinxcontrib_jsmath-1.0.1
2025-06-14T19:28:39.3988879Z 	updating dependency infos of sphinxcontrib_qthelp-1.0.3
2025-06-14T19:28:39.3989236Z 	updating dependency infos of sphinxcontrib_serializinghtml-2.0.0
2025-06-14T19:28:39.3989565Z 	updating dependency infos of spice-0.15.2
2025-06-14T19:28:39.3989840Z 	updating dependency infos of spice_protocol-0.14.4
2025-06-14T19:28:39.3990317Z 	spidermonkey-1.8.5 is still marked as untested on target architecture
2025-06-14T19:28:39.3990688Z 	spiff-1 is still marked as broken on target architecture
2025-06-14T19:28:39.3990980Z 	updating dependency infos of spotify_qt-3.12
2025-06-14T19:28:39.3991635Z 	updating dependency infos of sqlalchemy-1.3.24
2025-06-14T19:28:39.3991981Z 	updating dependency infos of sqlcipher-4.4.2
2025-06-14T19:28:39.3992256Z 	updating dependency infos of sqlite-3.47.2.0
2025-06-14T19:28:39.3992535Z 	updating dependency infos of sqlitebrowser-3.12.1
2025-06-14T19:28:39.3992818Z 	updating dependency infos of sqlitecpp-3.3.2
2025-06-14T19:28:39.3993097Z 	updating dependency infos of squashfs_tools-4.6.1
2025-06-14T19:28:39.3993367Z 	updating dependency infos of squirrel-3.2
2025-06-14T19:28:39.3993623Z 	updating dependency infos of sratom-0.6.14
2025-06-14T19:28:39.3993901Z 	updating dependency infos of srb2-2.2.9
2025-06-14T19:28:39.3994155Z 	updating dependency infos of srb2_data-2.2.9
2025-06-14T19:28:39.3994409Z 	updating dependency infos of srm-1.2.15
2025-06-14T19:28:39.3994663Z 	updating dependency infos of ssh_askpass-0.3
2025-06-14T19:28:39.3994929Z 	updating dependency infos of sshfs_fuse-2.10
2025-06-14T19:28:39.3995178Z 	updating dependency infos of stagit-1.2
2025-06-14T19:28:39.3995443Z 	updating dependency infos of starfighter-2.0.0.3
2025-06-14T19:28:39.3995728Z 	updating dependency infos of steghide-0.5.1.1
2025-06-14T19:28:39.3995999Z 	updating dependency infos of stegsnow-20130616
2025-06-14T19:28:39.3996323Z 	updating dependency infos of stella2014_libretro-3.9.3_20241021
2025-06-14T19:28:39.3996689Z 	updating dependency infos of stella_libretro-6.5.3_20250419
2025-06-14T19:28:39.3997002Z 	updating dependency infos of stellarium-25.1
2025-06-14T19:28:39.3997257Z 	updating dependency infos of step-25.04.0
2025-06-14T19:28:39.3997505Z 	updating dependency infos of stfl-0.24
2025-06-14T19:28:39.3997749Z 	updating dependency infos of stlink-1.6.1
2025-06-14T19:28:39.3998002Z 	updating dependency infos of stlover-1.0.1
2025-06-14T19:28:39.3998259Z 	recipe for stm32flash-0.3 is still broken:
2025-06-14T19:28:39.3998704Z 	Error: package stm32flash-0.3 cannot be built for architecture x86_64
2025-06-14T19:28:39.3999055Z 	updating dependency infos of stockfish-9
2025-06-14T19:28:39.3999305Z 	updating dependency infos of stormlib-9.30
2025-06-14T19:28:39.3999571Z 	updating dependency infos of strawberry-1.2.11
2025-06-14T19:28:39.3999846Z 	updating dependency infos of streamradio-1.0.0
2025-06-14T19:28:39.4000121Z 	updating dependency infos of stress_ng-0.18.06
2025-06-14T19:28:39.4000375Z 	updating dependency infos of strigi-0.7.8
2025-06-14T19:28:39.4000704Z 	stylededitplus-1.0 is still marked as untested on target architecture
2025-06-14T19:28:39.4001281Z 	updating dependency infos of sub_exporter_progressive-0.001013
2025-06-14T19:28:39.4001633Z 	updating dependency infos of sub_quote-2.006008
2025-06-14T19:28:39.4001918Z 	updating dependency infos of sub_uplevel-0.2800
2025-06-14T19:28:39.4002185Z 	updating dependency infos of substrate-1.0b
2025-06-14T19:28:39.4002475Z 	updating dependency infos of subtitlecomposer-0.8.0
2025-06-14T19:28:39.4002812Z 	updating dependency infos of subversion-1.14.3
2025-06-14T19:28:39.4003346Z 	updating dependency infos of suitesparse-5.7.1
2025-06-14T19:28:39.4003836Z 	updating dependency infos of sum_it-0.2beta
2025-06-14T19:28:39.4004218Z 	updating dependency infos of sundials-6.5.1
2025-06-14T19:28:39.4004512Z 	updating dependency infos of super_transball-2.1.5
2025-06-14T19:28:39.4004812Z 	updating dependency infos of superfreecell-0.1.0
2025-06-14T19:28:39.4005092Z 	updating dependency infos of superlu-5.3.0
2025-06-14T19:28:39.4005363Z 	updating dependency infos of supermariowar-beta1.1
2025-06-14T19:28:39.4005650Z 	updating dependency infos of superprefs-1.0
2025-06-14T19:28:39.4005923Z 	updating dependency infos of superslicer-2.5.60.0
2025-06-14T19:28:39.4006209Z 	updating dependency infos of supertux-0.6.1
2025-06-14T19:28:39.4006478Z 	updating dependency infos of supertuxkart-1.3
2025-06-14T19:28:39.4006895Z 	updating dependency infos of surgescript-0.5.5
2025-06-14T19:28:39.4007179Z 	updating dependency infos of svgcleaner-0.9.5
2025-06-14T19:28:39.4007437Z 	updating dependency infos of svt_av1-1.0.0
2025-06-14T19:28:39.4007759Z 	swi_prolog-9.0.4 is still marked as untested on target architecture
2025-06-14T19:28:39.4008148Z 	swift_lang-4.1.0~git is still marked as untested on target architecture
2025-06-14T19:28:39.4008535Z 	swift_lang-3.1 is still marked as untested on target architecture
2025-06-14T19:28:39.4008850Z 	updating dependency infos of swig-4.0.2
2025-06-14T19:28:39.4009094Z 	updating dependency infos of sword-1.8.1
2025-06-14T19:28:39.4009350Z 	updating dependency infos of symbola-10.03
2025-06-14T19:28:39.4009616Z 	updating dependency infos of symetrie-0.0.1
2025-06-14T19:28:39.4009897Z 	recipe for sync_modular-2.2.1b is still broken:
2025-06-14T19:28:39.4010247Z 	Error: package sync_modular-2.2.1b cannot be built for architecture x86_64
2025-06-14T19:28:39.4010614Z 	updating dependency infos of syncterm-1.3
2025-06-14T19:28:39.4010886Z 	updating dependency infos of syndication-5.115.0
2025-06-14T19:28:39.4011440Z 	updating dependency infos of syndication6-6.13.0
2025-06-14T19:28:39.4011738Z 	recipe for synergy-1.5.0 is still broken:
2025-06-14T19:28:39.4012052Z 	Error: package synergy-1.5.0 cannot be built for architecture x86_64
2025-06-14T19:28:39.4012398Z 	updating dependency infos of synergy_haiku-0.3
2025-06-14T19:28:39.4012667Z 	updating dependency infos of systeminfo-2
2025-06-14T19:28:39.4012925Z 	updating dependency infos of szip-2.1.1
2025-06-14T19:28:39.4013171Z 	updating dependency infos of t1utils-1.42
2025-06-14T19:28:39.4013437Z 	updating dependency infos of t4k_common-0.1.1
2025-06-14T19:28:39.4013737Z 	updating dependency infos of tagainijisho-1.2~20180610
2025-06-14T19:28:39.4014022Z 	updating dependency infos of taglib-1.12
2025-06-14T19:28:39.4014284Z 	updating dependency infos of taglib2.0-2.0.2
2025-06-14T19:28:39.4014556Z 	updating dependency infos of takenotes-1.0.1~git
2025-06-14T19:28:39.4014835Z 	updating dependency infos of tanglet-1.6.5
2025-06-14T19:28:39.4015203Z 	updating dependency infos of tar-1.35
2025-06-14T19:28:39.4015464Z 	updating dependency infos of taresizer-3.4
2025-06-14T19:28:39.4015713Z 	updating dependency infos of task-2.6.0~git
2025-06-14T19:28:39.4015982Z 	updating dependency infos of taskmanager-0.1.7
2025-06-14T19:28:39.4016311Z 	tbb-2022.0.0 is still marked as untested on target architecture
2025-06-14T19:28:39.4016668Z 	tbb-2021.10.0 is still marked as untested on target architecture
2025-06-14T19:28:39.4016974Z 	updating dependency infos of tbb-2018.5
2025-06-14T19:28:39.4017215Z 	updating dependency infos of tbe-0.9.3.1
2025-06-14T19:28:39.4017504Z 	tcc-0.9.26 is still marked as untested on target architecture
2025-06-14T19:28:39.4017793Z 	updating dependency infos of tcl-8.6.14
2025-06-14T19:28:39.4018043Z 	updating dependency infos of tcllib-1.21
2025-06-14T19:28:39.4018303Z 	updating dependency infos of tcpdump-4.99.5
2025-06-14T19:28:39.4018560Z 	updating dependency infos of tcpslice-1.7
2025-06-14T19:28:39.4018827Z 	updating dependency infos of tdlib-0.0.20250511
2025-06-14T19:28:39.4019089Z 	updating dependency infos of teckit-2.5.9
2025-06-14T19:28:39.4019359Z 	updating dependency infos of tecnoballz-0.94.0~git
2025-06-14T19:28:39.4019723Z 	teensy_loader_cli-2.1.202108 is still marked as untested on target architecture
2025-06-14T19:28:39.4020089Z 	updating dependency infos of teeworlds-0.7.5
2025-06-14T19:28:39.4020380Z 	updating dependency infos of telegram_desktop-5.14.3
2025-06-14T19:28:39.4020670Z 	updating dependency infos of tellico-4.1.2
2025-06-14T19:28:39.4020928Z 	updating dependency infos of tenacity-1.3.3
2025-06-14T19:28:39.4021516Z 	updating dependency infos of terminal_theme_catppuccin-0.2.0
2025-06-14T19:28:39.4021855Z 	updating dependency infos of terminus_ttf-4.47.0
2025-06-14T19:28:39.4022136Z 	updating dependency infos of termreadkey-2.38
2025-06-14T19:28:39.4022460Z 	terrarium-0.1.9 is still marked as untested on target architecture
2025-06-14T19:28:39.4022916Z 	updating dependency infos of tesseract-3.05.02
2025-06-14T19:28:39.4023212Z 	updating dependency infos of tesseract_data-3.04.00
2025-06-14T19:28:39.4023531Z 	updating dependency infos of tesseracttranslator-1.0.2
2025-06-14T19:28:39.4023869Z 	updating dependency infos of test2_plugin_nowarnings-0.10
2025-06-14T19:28:39.4024182Z 	updating dependency infos of test_deep-1.204
2025-06-14T19:28:39.4024458Z 	updating dependency infos of test_differences-0.71
2025-06-14T19:28:39.4024750Z 	updating dependency infos of test_exception-0.43
2025-06-14T19:28:39.4025124Z 	updating dependency infos of test_fatal-0.017
2025-06-14T19:28:39.4025394Z 	updating dependency infos of test_file-1.993
2025-06-14T19:28:39.4025694Z 	updating dependency infos of test_file_sharedir-1.001002
2025-06-14T19:28:39.4025998Z 	updating dependency infos of test_leaktrace-0.17
2025-06-14T19:28:39.4026273Z 	updating dependency infos of test_most-0.38
2025-06-14T19:28:39.4026537Z 	updating dependency infos of test_needs-0.002010
2025-06-14T19:28:39.4026824Z 	updating dependency infos of test_requires-0.11
2025-06-14T19:28:39.4027126Z 	updating dependency infos of test_requiresinternet-0.05
2025-06-14T19:28:39.4027422Z 	updating dependency infos of test_warn-0.37
2025-06-14T19:28:39.4027683Z 	updating dependency infos of test_warnings-0.033
2025-06-14T19:28:39.4027988Z 	updating dependency infos of test_without_module-0.23
2025-06-14T19:28:39.4028279Z 	updating dependency infos of testdisk-7.2
2025-06-14T19:28:39.4028526Z 	updating dependency infos of tetzle-2.2.3
2025-06-14T19:28:41.8495045Z 	updating dependency infos of tex_gyre-2.501
2025-06-14T19:28:41.8495583Z 	updating dependency infos of texi2html-1.82
2025-06-14T19:28:41.8496047Z 	updating dependency infos of texinfo-7.1
2025-06-14T19:28:41.8496340Z 	updating dependency infos of texinfo4-4.13a
2025-06-14T19:28:41.8496603Z 	updating dependency infos of texlive-2025
2025-06-14T19:28:41.8496874Z 	updating dependency infos of texlive_core-2025
2025-06-14T19:28:41.8497184Z 	updating dependency infos of texmacs-1.99.12
2025-06-14T19:28:41.8497672Z 	updating dependency infos of texmaker-5.1.4
2025-06-14T19:28:41.8497943Z 	updating dependency infos of texstudio-4.8.7
2025-06-14T19:28:41.8498221Z 	updating dependency infos of text_bibtex-0.91
2025-06-14T19:28:41.8498487Z 	updating dependency infos of text_csv-2.04
2025-06-14T19:28:41.8498754Z 	updating dependency infos of text_csv_xs-1.57
2025-06-14T19:28:41.8499017Z 	updating dependency infos of text_diff-1.45
2025-06-14T19:28:41.8499265Z 	updating dependency infos of text_glob-0.11
2025-06-14T19:28:41.8499517Z 	updating dependency infos of text_patch-1.8
2025-06-14T19:28:41.8499764Z 	updating dependency infos of text_roman-3.5
2025-06-14T19:28:41.8500013Z 	updating dependency infos of textsaver-1.0
2025-06-14T19:28:41.8500282Z 	updating dependency infos of tg_owt-0.0.20250511
2025-06-14T19:28:41.8500594Z 	updating dependency infos of the_silver_searcher-2.2.0
2025-06-14T19:28:41.8500920Z 	updating dependency infos of thememanager-1.0~git
2025-06-14T19:28:41.8501542Z 	updating dependency infos of themes-1.0~git
2025-06-14T19:28:41.8501840Z 	updating dependency infos of thepowdertoy-97.0.352
2025-06-14T19:28:41.8502144Z 	updating dependency infos of threadweaver-5.115.0
2025-06-14T19:28:41.8502440Z 	updating dependency infos of threadweaver6-6.13.0
2025-06-14T19:28:41.8502709Z 	updating dependency infos of tidy-5.8.0
2025-06-14T19:28:41.8502974Z 	updating dependency infos of tie_cycle-1.229
2025-06-14T19:28:41.8503236Z 	updating dependency infos of tie_simple-1.04
2025-06-14T19:28:41.8503493Z 	updating dependency infos of tiff-4.7.0
2025-06-14T19:28:41.8503748Z 	updating dependency infos of tiff4.4-4.4.0
2025-06-14T19:28:41.8503999Z 	updating dependency infos of tig-2.5.12
2025-06-14T19:28:41.8504244Z 	updating dependency infos of time-1.9
2025-06-14T19:28:41.8504549Z 	timebomb-0.4.0 is still marked as untested on target architecture
2025-06-14T19:28:41.8504871Z 	updating dependency infos of timecop-0.61
2025-06-14T19:28:41.8505264Z 	updating dependency infos of timedate-2.33
2025-06-14T19:28:41.8505531Z 	updating dependency infos of timetracker-0.2
2025-06-14T19:28:41.8505802Z 	updating dependency infos of timezone_data-2023c
2025-06-14T19:28:41.8506092Z 	updating dependency infos of timgmsoundfont-fixed
2025-06-14T19:28:41.8506407Z 	updating dependency infos of timidity_freepats-20060219
2025-06-14T19:28:41.8506731Z 	tin-2.4.4 is still marked as untested on target architecture
2025-06-14T19:28:41.8507031Z 	updating dependency infos of tiny-0.1.01
2025-06-14T19:28:41.8507289Z 	updating dependency infos of tinyemu-2019.12.21
2025-06-14T19:28:41.8507550Z 	recipe for tinygl-0.4 is still broken:
2025-06-14T19:28:41.8507855Z 	Error: package tinygl-0.4 cannot be built for architecture x86_64
2025-06-14T19:28:41.8508184Z 	updating dependency infos of tinyxml-2.6.2
2025-06-14T19:28:41.8508443Z 	updating dependency infos of tinyxml2-11.0.0
2025-06-14T19:28:41.8508693Z 	updating dependency infos of tinyxxd-1.3.1
2025-06-14T19:28:41.8508945Z 	updating dependency infos of tio-2.5
2025-06-14T19:28:41.8509192Z 	updating dependency infos of tipster-1.1.3
2025-06-14T19:28:41.8509441Z 	updating dependency infos of tk-8.6.10
2025-06-14T19:28:41.8509673Z 	updating dependency infos of tklib-0.7
2025-06-14T19:28:41.8509937Z 	updating dependency infos of tldr-1.6.1
2025-06-14T19:28:41.8510204Z 	updating dependency infos of tmux-3.1c
2025-06-14T19:28:41.8510446Z 	updating dependency infos of tnftp-20151004
2025-06-14T19:28:41.8510769Z 	tnftpd-20190602 is still marked as untested on target architecture
2025-06-14T19:28:41.8511246Z 	updating dependency infos of tnt-3.0.12
2025-06-14T19:28:41.8511599Z 	todolistmanager-0.11 is still marked as untested on target architecture
2025-06-14T19:28:41.8511943Z 	updating dependency infos of toilet-0.3~git
2025-06-14T19:28:41.8512211Z 	updating dependency infos of tokodon-25.04.0
2025-06-14T19:28:41.8512527Z 	tolmach-1.1.0 is still marked as untested on target architecture
2025-06-14T19:28:41.8512836Z 	updating dependency infos of tolua-5.2.4
2025-06-14T19:28:41.8513204Z 	updating dependency infos of toluapp-1.0.93
2025-06-14T19:28:41.8513457Z 	updating dependency infos of tomli-2.0.1
2025-06-14T19:28:41.8513707Z 	updating dependency infos of tomlkit-0.12.4
2025-06-14T19:28:41.8513950Z 	updating dependency infos of toner-1.0.0
2025-06-14T19:28:41.8514189Z 	updating dependency infos of toot-0.42.0
2025-06-14T19:28:41.8514429Z 	updating dependency infos of tor-0.4.8.12
2025-06-14T19:28:41.8514695Z 	updating dependency infos of torrentor-0.0.5~git
2025-06-14T19:28:41.8515018Z 	torsocks-1.3 is still marked as untested on target architecture
2025-06-14T19:28:41.8515321Z 	updating dependency infos of tox-0.2.18
2025-06-14T19:28:41.8515574Z 	updating dependency infos of trackergrep-5.2
2025-06-14T19:28:41.8515839Z 	updating dependency infos of trackgit-1.0.0~git
2025-06-14T19:28:41.8516120Z 	updating dependency infos of trackrunner-0.2.2
2025-06-14T19:28:41.8516390Z 	recipe for transformers-0.5.6.2 is still broken:
2025-06-14T19:28:41.8516756Z 	Error: package transformers-0.5.6.2 cannot be built for architecture x86_64
2025-06-14T19:28:41.8517137Z 	updating dependency infos of transmission-3.00
2025-06-14T19:28:41.8517415Z 	updating dependency infos of transplus-0.6
2025-06-14T19:28:41.8517670Z 	updating dependency infos of trax-1.1.1
2025-06-14T19:28:41.8517910Z 	updating dependency infos of tree-1.8.0
2025-06-14T19:28:41.8518183Z 	updating dependency infos of tree_sitter-0.20.10~git
2025-06-14T19:28:41.8518464Z 	updating dependency infos of treecc-0.3.10
2025-06-14T19:28:41.8518733Z 	updating dependency infos of tremor-1.0.0~git
2025-06-14T19:28:41.8519043Z 	updating dependency infos of trenchbroom-2025.1
2025-06-14T19:28:41.8519542Z 	updating dependency infos of trojita-0.7.0
2025-06-14T19:28:41.8520112Z 	updating dependency infos of trove_classifiers-2024.10.21.16
2025-06-14T19:28:41.8520577Z 	updating dependency infos of try_tiny-0.32
2025-06-14T19:28:41.8520856Z 	updating dependency infos of turbo-2024.02.05~git
2025-06-14T19:28:41.8521463Z 	updating dependency infos of tuxcards-2.2.1~git
2025-06-14T19:28:41.8521747Z 	updating dependency infos of tuxmath-2.0.1
2025-06-14T19:28:41.8522005Z 	updating dependency infos of tuxpaint-0.9.35
2025-06-14T19:28:41.8522296Z 	updating dependency infos of tuxpaint_config-0.0.26
2025-06-14T19:28:41.8522610Z 	updating dependency infos of tuxpaint_stamps-2025.05.26
2025-06-14T19:28:41.8522903Z 	updating dependency infos of tuxpuck-0.8.2
2025-06-14T19:28:41.8523155Z 	updating dependency infos of tuxracer-0.61
2025-06-14T19:28:41.8523414Z 	updating dependency infos of tuxracer_data-0.61
2025-06-14T19:28:41.8523686Z 	updating dependency infos of tuxtype2-1.8.3
2025-06-14T19:28:41.8523955Z 	updating dependency infos of tvision-2024.02.04~git
2025-06-14T19:28:41.8524230Z 	updating dependency infos of tweeny-3.2.0
2025-06-14T19:28:41.8524479Z 	updating dependency infos of twolame-0.4.0
2025-06-14T19:28:41.8524729Z 	updating dependency infos of tworld-1.3.2
2025-06-14T19:28:41.8524987Z 	updating dependency infos of txt2man-1.7.1
2025-06-14T19:28:41.8525271Z 	updating dependency infos of typing_extensions-4.12.2
2025-06-14T19:28:41.8525563Z 	updating dependency infos of typst-0.13.1
2025-06-14T19:28:41.8525861Z 	updating dependency infos of tyrquake_libretro-0.62_20241227
2025-06-14T19:28:41.8526174Z 	updating dependency infos of u_boot-2024.04
2025-06-14T19:28:41.8526439Z 	updating dependency infos of u_boot_tools-2021.10
2025-06-14T19:28:41.8526709Z 	recipe for uade-2.13 is still broken:
2025-06-14T19:28:41.8527008Z 	Error: package uade-2.13 cannot be built for architecture x86_64
2025-06-14T19:28:41.8527344Z 	updating dependency infos of ubertuber-0.9.13
2025-06-14T19:28:41.8527639Z 	updating dependency infos of ubuntu_font_family-0.83
2025-06-14T19:28:41.8527923Z 	updating dependency infos of uchardet-0.0.7
2025-06-14T19:28:41.8528183Z 	updating dependency infos of ucommon-7.0.1
2025-06-14T19:28:41.8528428Z 	updating dependency infos of ucpp-1.3.5
2025-06-14T19:28:41.8528681Z 	updating dependency infos of udis86-1.7.2
2025-06-14T19:28:41.8528925Z 	updating dependency infos of ugrep-3.12.0
2025-06-14T19:28:41.8529288Z 	updating dependency infos of uhexen2-1.5.9
2025-06-14T19:28:41.8529544Z 	updating dependency infos of uif2iso-0.1.7c
2025-06-14T19:28:41.8529810Z 	updating dependency infos of ukijorgfonts-1.0
2025-06-14T19:28:41.8530092Z 	updating dependency infos of ultracopier-2.0.0.1
2025-06-14T19:28:41.8530358Z 	updating dependency infos of ultradv-0.0.1
2025-06-14T19:28:41.8530620Z 	updating dependency infos of umbrello-25.04.0
2025-06-14T19:28:41.8530874Z 	updating dependency infos of unarr-1.0.1
2025-06-14T19:28:41.8531349Z 	updating dependency infos of uncrustify-0.78.1
2025-06-14T19:28:41.8531660Z 	updating dependency infos of unibilium-2.0.0
2025-06-14T19:28:41.8531981Z 	updating dependency infos of unicode_character_database-15.0.0
2025-06-14T19:28:41.8532310Z 	updating dependency infos of unicode_cldr-43.0
2025-06-14T19:28:41.8532617Z 	updating dependency infos of unicode_input_method-20230929
2025-06-14T19:28:41.8532967Z 	updating dependency infos of unicode_linebreak-2019.001
2025-06-14T19:28:41.8533267Z 	updating dependency infos of unicode_utf8-0.62
2025-06-14T19:28:41.8533529Z 	updating dependency infos of unicorn-2.1.2
2025-06-14T19:28:41.8533776Z 	updating dependency infos of unifdef-2.12
2025-06-14T19:28:41.8534036Z 	updating dependency infos of unifont-15.0.01
2025-06-14T19:28:41.8534296Z 	updating dependency infos of unittest++-2.0.0
2025-06-14T19:28:41.8534615Z 	updating dependency infos of universalscroller-4.0.1~20171227
2025-06-14T19:28:41.8534936Z 	updating dependency infos of unixodbc-2.3.11
2025-06-14T19:28:41.8535212Z 	updating dependency infos of unknown_horizons-2014.1
2025-06-14T19:28:41.8535493Z 	recipe for unlzx-1.1 is still broken:
2025-06-14T19:28:41.8535794Z 	Error: package unlzx-1.1 cannot be built for architecture x86_64
2025-06-14T19:28:41.8536112Z 	updating dependency infos of unrar-6.2.10
2025-06-14T19:28:41.8536365Z 	updating dependency infos of unrardll-0.1.7
2025-06-14T19:28:41.8536797Z 	updating dependency infos of unreal_speccy_portable-0.0.86.21
2025-06-14T19:28:41.8537114Z 	updating dependency infos of unrtf-0.21.10
2025-06-14T19:28:41.8537365Z 	updating dependency infos of unshield-1.5.1
2025-06-14T19:28:41.8537619Z 	updating dependency infos of unzip-6.10c23
2025-06-14T19:28:41.8537868Z 	updating dependency infos of uploadit-1.3
2025-06-14T19:28:41.8538119Z 	updating dependency infos of upmendex-1.11
2025-06-14T19:28:41.8538401Z 	uqm-0.7.0 is still marked as broken on target architecture
2025-06-14T19:28:41.8538687Z 	updating dependency infos of uri-5.28
2025-06-14T19:28:41.8538932Z 	updating dependency infos of uriparser-0.9.7
2025-06-14T19:28:41.8539195Z 	updating dependency infos of urllib3-1.26.19
2025-06-14T19:28:41.8539485Z 	updating dependency infos of urw_base35_fonts-20200910
2025-06-14T19:28:41.8539766Z 	updating dependency infos of urwid-2.1.2
2025-06-14T19:28:41.8540026Z 	updating dependency infos of usbdeskbar-1.0.0
2025-06-14T19:28:41.8540288Z 	updating dependency infos of utfcpp-4.0.5
2025-06-14T19:28:41.8540543Z 	updating dependency infos of uthash-2.3.0
2025-06-14T19:28:41.8540793Z 	updating dependency infos of util_linux-2.34
2025-06-14T19:28:41.8541066Z 	updating dependency infos of util_macros-1.20.0
2025-06-14T19:28:41.8541526Z 	updating dependency infos of uxn-20230829
2025-06-14T19:28:41.8541772Z 	updating dependency infos of v8-7.4.288.28
2025-06-14T19:28:41.8542058Z 	updating dependency infos of vacuum-1.3.0.20191119
2025-06-14T19:28:41.8542332Z 	updating dependency infos of vala-0.56.14
2025-06-14T19:28:41.8542590Z 	updating dependency infos of valentina-0.6.1
2025-06-14T19:28:41.8542867Z 	updating dependency infos of vamp_plugin_sdk-2.10.0
2025-06-14T19:28:41.8543158Z 	updating dependency infos of vangers-1.46.0~git
2025-06-14T19:28:41.8543434Z 	updating dependency infos of variable_magic-0.64
2025-06-14T19:28:41.8543707Z 	updating dependency infos of vasm-1.9d
2025-06-14T19:28:41.8544004Z 	updating dependency infos of vba_next_libretro-1.0.2_20241021
2025-06-14T19:28:41.8544309Z 	updating dependency infos of vc-1.4.3
2025-06-14T19:28:41.8544675Z 	updating dependency infos of vcardpeople-1.0.1
2025-06-14T19:28:41.8544999Z 	vcdgear-1.1 is still marked as broken on target architecture
2025-06-14T19:28:41.8545313Z 	updating dependency infos of vcdimager-2.0.1
2025-06-14T19:28:41.8545564Z 	updating dependency infos of vcmi-1.3.1
2025-06-14T19:28:43.2538683Z packageEntries: warning: "bin" doesn't seem to be a valid package suffix.
2025-06-14T19:28:43.2723449Z packageEntries: warning: "bin" doesn't seem to be a valid package suffix.
2025-06-14T19:28:43.8810750Z 	updating dependency infos of vectoroids-1.1.0
2025-06-14T19:28:43.8811652Z 	updating dependency infos of vecx_libretro-1.2_20250412
2025-06-14T19:28:43.8812236Z 	updating dependency infos of verilator-4.222
2025-06-14T19:28:43.8812806Z 	vice-3.3 is still marked as untested on target architecture
2025-06-14T19:28:43.8813435Z 	vice-3.2 is still marked as untested on target architecture
2025-06-14T19:28:43.8814106Z 	vice-2.4.24 is still marked as untested on target architecture
2025-06-14T19:28:43.8814742Z 	updating dependency infos of vice_libretro-3.7_20240827
2025-06-14T19:28:43.8815285Z 	updating dependency infos of vifm-0.12
2025-06-14T19:28:43.8815854Z 	vigra-1.11.1 is still marked as untested on target architecture
2025-06-14T19:28:43.8816417Z 	updating dependency infos of vim-9.1.1153
2025-06-14T19:28:43.8816926Z 	recipe for virtualbelive-20140718 is still broken:
2025-06-14T19:28:43.8817625Z 	Error: package virtualbelive-20140718 cannot be built for architecture x86_64
2025-06-14T19:28:43.8818430Z 	updating dependency infos of virtualbox_guest_additions-6.1.26
2025-06-14T19:28:43.8819149Z 	updating dependency infos of virtualjaguar_libretro-2.1.2_20241021
2025-06-14T19:28:43.8819756Z 	updating dependency infos of vis-0.8
2025-06-14T19:28:43.8820217Z 	updating dependency infos of vision-0.10.6
2025-06-14T19:28:43.8820711Z 	updating dependency infos of vl_gothic-20141206
2025-06-14T19:28:43.8821954Z 	updating dependency infos of vlc-3.0.21
2025-06-14T19:28:43.8822416Z 	recipe for vlink-0.16a is still broken:
2025-06-14T19:28:43.8822984Z 	Error: package vlink-0.16a cannot be built for architecture x86_64
2025-06-14T19:28:43.8823557Z 	recipe for vlink-0.15 is still broken:
2025-06-14T19:28:43.8824126Z 	Error: package vlink-0.15 cannot be built for architecture x86_64
2025-06-14T19:28:43.8824707Z 	updating dependency infos of vlna-1.5
2025-06-14T19:28:43.8825154Z 	updating dependency infos of vmaf-1.5.1
2025-06-14T19:28:43.8825637Z 	updating dependency infos of vmware_addons-1.2.2
2025-06-14T19:28:43.8826119Z 	updating dependency infos of vncserver-1.34
2025-06-14T19:28:43.8826582Z 	recipe for vncviewer-3.3.1r6 is still broken:
2025-06-14T19:28:43.8827177Z 	Error: package vncviewer-3.3.1r6 cannot be built for architecture x86_64
2025-06-14T19:28:43.8827783Z 	updating dependency infos of vollkorn-4.105
2025-06-14T19:28:43.8828249Z 	updating dependency infos of voluptuous-0.12.1
2025-06-14T19:28:43.8828753Z 	updating dependency infos of vorbis_tools-1.4.2
2025-06-14T19:28:43.8829236Z 	updating dependency infos of voxophone-1.0
2025-06-14T19:28:43.8829693Z 	updating dependency infos of vttest-20230201
2025-06-14T19:28:43.8830151Z 	updating dependency infos of vulkan-1.4.311
2025-06-14T19:28:43.8830591Z 	updating dependency infos of vvvvvv-2.3.6
2025-06-14T19:28:43.8831042Z 	updating dependency infos of vvvvvv_data-2.0
2025-06-14T19:28:43.8831674Z 	updating dependency infos of vwget-20141229
2025-06-14T19:28:43.8832133Z 	updating dependency infos of w2c2-0.1~20221219
2025-06-14T19:28:43.8832611Z 	updating dependency infos of w3m-0.5.3~git20230121
2025-06-14T19:28:43.8833086Z 	updating dependency infos of w6-1.7
2025-06-14T19:28:43.8833595Z 	waave-3.01 is still marked as untested on target architecture
2025-06-14T19:28:43.8834128Z 	updating dependency infos of waitress-2.1.2
2025-06-14T19:28:43.8834570Z 	updating dependency infos of wakeup-1.0
2025-06-14T19:28:43.8835057Z 	updating dependency infos of wallpaper_community-0.1
2025-06-14T19:28:43.8835809Z 	updating dependency infos of wallpaper_unsplash-0.1
2025-06-14T19:28:43.8836303Z 	updating dependency infos of wand-0.6.13
2025-06-14T19:28:43.8836770Z 	updating dependency infos of warmux-11.0.4~git
2025-06-14T19:28:43.8837224Z 	updating dependency infos of wasm3-0.5.0
2025-06-14T19:28:43.8837670Z 	updating dependency infos of watchdog-3.0.0
2025-06-14T19:28:43.8838209Z 	waterfox-6.5.7 is still marked as broken on target architecture
2025-06-14T19:28:43.8838765Z 	updating dependency infos of waterfox_bin-6.5.7
2025-06-14T19:28:43.8839231Z 	updating dependency infos of waveedit-1.1
2025-06-14T19:28:43.8839661Z 	recipe for waveview-1.0 is still broken:
2025-06-14T19:28:43.8840210Z 	Error: package waveview-1.0 cannot be built for architecture x86_64
2025-06-14T19:28:43.8840777Z 	updating dependency infos of wavpack-5.5.0
2025-06-14T19:28:43.8841387Z 	updating dependency infos of wayland-1.21.0~git
2025-06-14T19:28:43.8841899Z 	updating dependency infos of wayland_protocols-1.36
2025-06-14T19:28:43.8842468Z 	updating dependency infos of wayland_server-0.1.20250303
2025-06-14T19:28:43.8843072Z 	wcalc-2.5 is still marked as untested on target architecture
2025-06-14T19:28:43.8843596Z 	updating dependency infos of wcslib-7.8
2025-06-14T19:28:43.8844054Z 	updating dependency infos of wcstools-3.9.7
2025-06-14T19:28:43.8844513Z 	updating dependency infos of wcwidth-0.2.6
2025-06-14T19:28:43.8844953Z 	updating dependency infos of wdiff-1.2.2
2025-06-14T19:28:43.8845215Z 	updating dependency infos of weather-1.1.0
2025-06-14T19:28:43.8845512Z 	updating dependency infos of webencodings-0.5.1
2025-06-14T19:28:43.8845813Z 	updating dependency infos of webkit_gtk-2.40.0
2025-06-14T19:28:43.8846092Z 	updating dependency infos of websocketpp-0.8.2
2025-06-14T19:28:43.8846376Z 	updating dependency infos of webwatch-1.0~git
2025-06-14T19:28:43.8846668Z 	updating dependency infos of weechat-4.5.1
2025-06-14T19:28:43.8846926Z 	updating dependency infos of wesnoth-1.18.4
2025-06-14T19:28:43.8847336Z 	updating dependency infos of wget-1.24.5
2025-06-14T19:28:43.8847594Z 	updating dependency infos of wget2-2.2.0
2025-06-14T19:28:43.8847842Z 	updating dependency infos of wheel-0.41.2
2025-06-14T19:28:43.8848112Z 	updating dependency infos of whereismymouse-1.0
2025-06-14T19:28:43.8848378Z 	updating dependency infos of which-2.21
2025-06-14T19:28:43.8848640Z 	updating dependency infos of whid-2.0.2~beta
2025-06-14T19:28:43.8848950Z 	whisper-1.2 is still marked as untested on target architecture
2025-06-14T19:28:43.8849275Z 	updating dependency infos of widelands-1.1
2025-06-14T19:28:43.8849532Z 	updating dependency infos of wildmidi-0.4.5
2025-06-14T19:28:43.8849807Z 	updating dependency infos of windowtailor-0.2.1
2025-06-14T19:28:43.8850115Z 	wine-7.1 is still marked as broken on target architecture
2025-06-14T19:28:43.8850401Z 	updating dependency infos of wine_bin-7.9
2025-06-14T19:28:43.8850650Z 	recipe for wings-1.5.3 is still broken:
2025-06-14T19:28:43.8850964Z 	Error: package wings-1.5.3 cannot be built for architecture x86_64
2025-06-14T19:28:43.8851554Z 	updating dependency infos of wireshark-4.2.6
2025-06-14T19:28:43.8851820Z 	updating dependency infos of wizznic-1.1
2025-06-14T19:28:43.8852079Z 	updating dependency infos of woff2-1.0.2
2025-06-14T19:28:43.8852394Z 	wolfssl-5.7.6 is still marked as untested on target architecture
2025-06-14T19:28:43.8852725Z 	updating dependency infos of wolle-2.0~git
2025-06-14T19:28:43.8853003Z 	updating dependency infos of wonderbrush-2.1.2
2025-06-14T19:28:43.8853345Z 	wonderbrush3-3.0.0~git is still marked as broken on target architecture
2025-06-14T19:28:43.8853696Z 	updating dependency infos of wordclock-0.1.1
2025-06-14T19:28:43.8853960Z 	updating dependency infos of wordgrinder-0.8
2025-06-14T19:28:43.8854234Z 	updating dependency infos of wordtsar-0.3.719
2025-06-14T19:28:43.8854515Z 	updating dependency infos of workspacenumber-0.2
2025-06-14T19:28:43.8854838Z 	updating dependency infos of wpa_supplicant-2.11.haiku.0
2025-06-14T19:28:43.8855141Z 	updating dependency infos of wput-0.6.2
2025-06-14T19:28:43.8855542Z 	updating dependency infos of wqy_microhei-0.2.0~beta
2025-06-14T19:28:43.8855844Z 	updating dependency infos of wqy_zenhei-0.9.45
2025-06-14T19:28:43.8856111Z 	updating dependency infos of wrapt-1.15.0
2025-06-14T19:28:43.8856364Z 	updating dependency infos of wv-1.2.9
2025-06-14T19:28:43.8856626Z 	updating dependency infos of www_robotrules-6.02
2025-06-14T19:28:43.8856899Z 	updating dependency infos of wxgtk-3.2.6
2025-06-14T19:28:43.8857147Z 	updating dependency infos of wxqt-3.2.4
2025-06-14T19:28:43.8857400Z 	updating dependency infos of x16_emulator-46
2025-06-14T19:28:43.8857659Z 	updating dependency infos of x264-20220222
2025-06-14T19:28:43.8857900Z 	updating dependency infos of x265-3.5
2025-06-14T19:28:43.8858159Z 	updating dependency infos of x_series_fonts-2.0
2025-06-14T19:28:43.8858420Z 	updating dependency infos of xa-2.3.14
2025-06-14T19:28:43.8858661Z 	recipe for xamos-0.29 is still broken:
2025-06-14T19:28:43.8858986Z 	Error: package xamos-0.29 cannot be built for architecture x86_64
2025-06-14T19:28:43.8859467Z 	xaos-4.2.1 is still marked as untested on target architecture
2025-06-14T19:28:43.8859770Z 	updating dependency infos of xaos-3.4
2025-06-14T19:28:43.8860014Z 	updating dependency infos of xapian-1.4.26
2025-06-14T19:28:43.8860278Z 	updating dependency infos of xar-1.8.0.0~498
2025-06-14T19:28:43.8860540Z 	updating dependency infos of xash3d-0.20~git
2025-06-14T19:28:43.8860799Z 	updating dependency infos of xcairo-1.16.0
2025-06-14T19:28:43.8861060Z 	updating dependency infos of xcairo1.18-1.18.0
2025-06-14T19:28:43.8861674Z 	updating dependency infos of xcb_proto-1.13
2025-06-14T19:28:43.8862063Z 	updating dependency infos of xcb_util_keysyms-0.4.1
2025-06-14T19:28:43.8862356Z 	updating dependency infos of xcftools-1.0.7
2025-06-14T19:28:43.8862616Z 	updating dependency infos of xdelta-3.1.0
2025-06-14T19:28:43.8862875Z 	updating dependency infos of xdg_utils-1.2.1
2025-06-14T19:28:43.8863340Z 	xemacs-21.5_hg is still marked as untested on target architecture
2025-06-14T19:28:43.8863659Z 	updating dependency infos of xerces_c-3.3.0
2025-06-14T19:28:43.8863920Z 	updating dependency infos of xindy-2.5.1
2025-06-14T19:28:43.8864235Z 	xinetd-2.3.15.4 is still marked as untested on target architecture
2025-06-14T19:28:43.8864574Z 	updating dependency infos of xkeyboard_config-2.41
2025-06-14T19:28:43.8864855Z 	updating dependency infos of xlibe-0.3.3
2025-06-14T19:28:43.8865107Z 	updating dependency infos of xlreader-0.9.0
2025-06-14T19:28:43.8865360Z 	updating dependency infos of xmake-2.9.9
2025-06-14T19:28:43.8865617Z 	updating dependency infos of xml2pmx-2021_02_07
2025-06-14T19:28:43.8865902Z 	updating dependency infos of xml_libxml-2.0210
2025-06-14T19:28:43.8866187Z 	updating dependency infos of xml_libxml_simple-1.01
2025-06-14T19:28:43.8866484Z 	updating dependency infos of xml_libxslt-2.003000
2025-06-14T19:28:43.8866793Z 	updating dependency infos of xml_namespacesupport-1.12
2025-06-14T19:28:43.8867100Z 	updating dependency infos of xml_parser-2.47
2025-06-14T19:28:43.8867367Z 	updating dependency infos of xml_sax-1.02
2025-06-14T19:28:43.8867625Z 	updating dependency infos of xml_sax_base-1.09
2025-06-14T19:28:43.8867903Z 	updating dependency infos of xml_writer-0.900
2025-06-14T19:28:43.8868170Z 	updating dependency infos of xmlbmessage-1.0
2025-06-14T19:28:43.8868430Z 	updating dependency infos of xmlroff-0.6.3
2025-06-14T19:28:43.8868682Z 	updating dependency infos of xmlsec-1.2.37
2025-06-14T19:28:43.8869007Z 	updating dependency infos of xmlto-0.0.29
2025-06-14T19:28:43.8869449Z 	updating dependency infos of xmoto-0.6.1
2025-06-14T19:28:43.8869765Z 	updating dependency infos of xonsh-0.14.1
2025-06-14T19:28:43.8870028Z 	updating dependency infos of xoreos-0.0.7~git
2025-06-14T19:28:43.8870314Z 	updating dependency infos of xorg_sgml_doctools-1.12
2025-06-14T19:28:43.8870618Z 	updating dependency infos of xorgproto-2022.2
2025-06-14T19:28:43.8870901Z 	updating dependency infos of xorriso-1.5.4~pl02
2025-06-14T19:28:43.8871370Z 	updating dependency infos of xournalpp-1.2.3
2025-06-14T19:28:43.8871767Z 	updating dependency infos of xpdf-4.05
2025-06-14T19:28:43.8872083Z 	recipe for xpmtranslator-1.1.1~git is still broken:
2025-06-14T19:28:44.9956972Z 	Error: No match found for license unknown
2025-06-14T19:28:44.9957546Z 	Error: Valid license filenames included with Haiku are:
2025-06-14T19:28:44.9959481Z 	Error: Anti-Grain Geometry, Apache v2, Artistic, Artistic v2.0, BSD (2-clause), BSD (3-clause), BSD (4-clause), Be Sample Code License, Bullet, CDDL v1, CQuantizer, DEC, GLUT (Mark Kilgard), GNU GPL font exception, GNU GPL v1, GNU GPL v2, GNU GPL v3, GNU LGPL v2, GNU LGPL v2.1, GNU LGPL v3, GPC, Intel (2xxx firmware), Intel (ACPICA), Intel (firmware), LibHTTPd, LibJPEG, LibPNG, MAPM, MIT, MIT (no promotion), MPL v1.1, MPL v2.0, Marvell (firmware), OpenGroup, PDFlib Lite, Public Domain, Ralink (firmware), SGI Free B, SIL Open Font License v1.1, Zlib
2025-06-14T19:28:44.9961709Z 	Error: (in /runner/work/haikuports/haikuports/haiku-apps/xpmtranslator/xpmtranslator-1.1.1~git.recipe)
2025-06-14T19:28:44.9962238Z 	updating dependency infos of xrick-021212
2025-06-14T19:28:44.9962575Z 	updating dependency infos of xrick_libretro-1.0.0.6_20250105
2025-06-14T19:28:44.9962900Z 	updating dependency infos of xrs-1.9.1
2025-06-14T19:28:44.9963168Z 	updating dependency infos of xsimd-13.2.0
2025-06-14T19:28:44.9963436Z 	updating dependency infos of xstring-0.005
2025-06-14T19:28:44.9963710Z 	updating dependency infos of xsv-0.13.0
2025-06-14T19:28:44.9963973Z 	updating dependency infos of xtrans-1.4.0
2025-06-14T19:28:44.9964241Z 	updating dependency infos of xxhash-0.8.3
2025-06-14T19:28:44.9964515Z 	updating dependency infos of xygrib-1.2.6.1
2025-06-14T19:28:44.9964790Z 	updating dependency infos of xz_utils-5.6.2
2025-06-14T19:28:44.9965058Z 	updating dependency infos of yab-1.8.2
2025-06-14T19:28:44.9965345Z 	updating dependency infos of yab_buildfactory-2.4.6
2025-06-14T19:28:44.9965991Z 	updating dependency infos of yab_documentation-1.8.2
2025-06-14T19:28:44.9966301Z 	updating dependency infos of yab_ide-2.3.4
2025-06-14T19:28:44.9966605Z 	updating dependency infos of yab_localizer-0.0.6
2025-06-14T19:28:44.9966953Z 	updating dependency infos of yabause_libretro-0.9.15_20241021
2025-06-14T19:28:44.9967302Z 	updating dependency infos of yacreader-9.15.0
2025-06-14T19:28:44.9967589Z 	updating dependency infos of yaddns-1.1.2
2025-06-14T19:28:44.9967867Z 	updating dependency infos of yamagi_quake2-8.50
2025-06-14T19:28:44.9968170Z 	updating dependency infos of yaml_cpp0.7-0.7.0
2025-06-14T19:28:44.9968445Z 	updating dependency infos of yaml_cpp0.8-0.8.0
2025-06-14T19:28:44.9968706Z 	updating dependency infos of yara-4.4.0
2025-06-14T19:28:44.9968947Z 	updating dependency infos of yarl-1.9.4
2025-06-14T19:28:44.9969192Z 	updating dependency infos of yasm-1.3.0
2025-06-14T19:28:44.9969497Z 	yate-6.4.0 is still marked as untested on target architecture
2025-06-14T19:28:44.9969794Z 	updating dependency infos of yaz-5.35.1
2025-06-14T19:28:44.9970047Z 	updating dependency infos of yazpp-1.9.0
2025-06-14T19:28:44.9970302Z 	updating dependency infos of ykclient-2.15
2025-06-14T19:28:44.9970561Z 	updating dependency infos of ykpers-1.20.0
2025-06-14T19:28:44.9970830Z 	updating dependency infos of yodownet-2014.03.09
2025-06-14T19:28:44.9971223Z 	updating dependency infos of yoshi-1.1
2025-06-14T19:28:44.9971501Z 	updating dependency infos of youcompleteme-20241216
2025-06-14T19:28:44.9971810Z 	updating dependency infos of youtube_dl-2021.12.17
2025-06-14T19:28:44.9972099Z 	updating dependency infos of yt_dlp-2025.06.09
2025-06-14T19:28:44.9972363Z 	updating dependency infos of ytdl_gui-3.0
2025-06-14T19:28:44.9972630Z 	recipe for z26-2.16.00s is still broken:
2025-06-14T19:28:44.9972942Z 	Error: package z26-2.16.00s cannot be built for architecture x86_64
2025-06-14T19:28:44.9973304Z 	zaz-1.0.0 is still marked as broken on target architecture
2025-06-14T19:28:44.9973596Z 	updating dependency infos of zbar-0.23.90
2025-06-14T19:28:44.9973852Z 	updating dependency infos of zeal-0.7.2
2025-06-14T19:28:44.9974247Z 	updating dependency infos of zeromq-4.3.5
2025-06-14T19:28:44.9974502Z 	updating dependency infos of zesarux-10.10
2025-06-14T19:28:44.9974755Z 	updating dependency infos of zimg-3.0.5
2025-06-14T19:28:44.9974995Z 	updating dependency infos of zip-3.0
2025-06-14T19:28:44.9975232Z 	updating dependency infos of zipp-3.7.0
2025-06-14T19:28:44.9975466Z 	updating dependency infos of zlib-1.3.1
2025-06-14T19:28:44.9975709Z 	updating dependency infos of zlib_ng-2.2.2
2025-06-14T19:28:44.9975974Z 	updating dependency infos of zmusic-1.1.4~git
2025-06-14T19:28:44.9976242Z 	updating dependency infos of zookeeper-2.1.1
2025-06-14T19:28:44.9976508Z 	updating dependency infos of zopfli-1.0.3
2025-06-14T19:28:44.9976752Z 	updating dependency infos of zpaq-7.15
2025-06-14T19:28:44.9976999Z 	updating dependency infos of zsdx-1.12.3
2025-06-14T19:28:44.9977241Z 	updating dependency infos of zsh-5.8.1
2025-06-14T19:28:44.9977527Z 	updating dependency infos of zsh_completions-0.35.0
2025-06-14T19:28:44.9977814Z 	updating dependency infos of zstd-1.5.6
2025-06-14T19:28:44.9978070Z 	updating dependency infos of zsxd-1.12.2
2025-06-14T19:28:44.9978324Z 	updating dependency infos of zug-0.1.1
2025-06-14T19:28:44.9978568Z 	updating dependency infos of zx0-2021.12.17
2025-06-14T19:28:44.9978874Z 	zx7-2013.02.25 is still marked as untested on target architecture
2025-06-14T19:28:44.9979191Z 	updating dependency infos of zxing_cpp-2.3.0
2025-06-14T19:28:44.9979451Z 	updating dependency infos of zxtune-r5040
2025-06-14T19:28:44.9979695Z 	updating dependency infos of zydis-4.1.0
2025-06-14T19:28:44.9979954Z 	updating dependency infos of zziplib-0.13.79
2025-06-14T19:28:44.9980208Z Looking for stale dependency-infos ...
2025-06-14T19:28:45.0126894Z Global 'haikuporter --repository-update' completed.
2025-06-14T19:28:45.0128021Z Listing contents of REPOSITORY_PATH (/home/runner/work/haikuports/haikuports/repository/) after global update:
2025-06-14T19:28:45.0210703Z /runner/work/haikuports/haikuports/repository/:
2025-06-14T19:28:45.0211539Z 0ad-0.0.23b~alpha.DependencyInfo
2025-06-14T19:28:45.0211932Z 0ad_data-0.0.23b~alpha.DependencyInfo
2025-06-14T19:28:45.0212342Z 1oom-1.0.DependencyInfo
2025-06-14T19:28:45.0212687Z 2048-1.1.1.DependencyInfo
2025-06-14T19:28:45.0213067Z 2048_libretro-1.0_20241227.DependencyInfo
2025-06-14T19:28:45.0213482Z 2pow-1.2.2.DependencyInfo
2025-06-14T19:28:45.0213853Z 3dengine_libretro-1.0_20250304.DependencyInfo
2025-06-14T19:28:45.0214284Z 3dmov-0.2.DependencyInfo
2025-06-14T19:28:45.0214618Z 54321-1.0.2001.11.16.DependencyInfo
2025-06-14T19:28:45.0214995Z 64tass-1.60.3243.DependencyInfo
2025-06-14T19:28:45.0215357Z 7kaa-2.15.6.DependencyInfo
2025-06-14T19:28:45.0215781Z 7kaa_music-2.15.DependencyInfo
2025-06-14T19:28:45.0216146Z 81_libretro-1.0a_20241021.DependencyInfo
2025-06-14T19:28:45.0216560Z 8dock-0.9.5~git.DependencyInfo
2025-06-14T19:28:45.0216919Z a2ps-4.15.6.DependencyInfo
2025-06-14T19:28:45.0217282Z a2ps_debuginfo-4.15.6.DependencyInfo
2025-06-14T19:28:45.0217674Z a52dec-0.8.0.DependencyInfo
2025-06-14T19:28:45.0218042Z a52dec_devel-0.8.0.DependencyInfo
2025-06-14T19:28:45.0218429Z a_book-1.1.DependencyInfo
2025-06-14T19:28:45.0218758Z aaaa-1.1.DependencyInfo
2025-06-14T19:28:45.0219089Z aalib-1.4~rc5.DependencyInfo
2025-06-14T19:28:45.0219448Z aalib_devel-1.4~rc5.DependencyInfo
2025-06-14T19:28:45.0219847Z aalibtranslator-0.0.1.DependencyInfo
2025-06-14T19:28:45.0220272Z abaddon-0.2.2~git.DependencyInfo
2025-06-14T19:28:45.0220636Z abcl-1.9.2.DependencyInfo
2025-06-14T19:28:45.0220996Z abe-1.1.DependencyInfo
2025-06-14T19:28:45.0221481Z abiword-3.0.5.DependencyInfo
2025-06-14T19:28:45.0221874Z abseil_cpp-20230125.3.DependencyInfo
2025-06-14T19:28:45.0229677Z abseil_cpp.2022-20220623.1.DependencyInfo
2025-06-14T19:28:45.0230252Z abseil_cpp.2022_debuginfo-20220623.1.DependencyInfo
2025-06-14T19:28:45.0230767Z abseil_cpp.2022_devel-20220623.1.DependencyInfo
2025-06-14T19:28:45.0231388Z abseil_cpp.2025-20250127.0.DependencyInfo
2025-06-14T19:28:45.0231875Z abseil_cpp.2025_debuginfo-20250127.0.DependencyInfo
2025-06-14T19:28:45.0232580Z abseil_cpp.2025_devel-20250127.0.DependencyInfo
2025-06-14T19:28:45.0233077Z abseil_cpp_debuginfo-20230125.3.DependencyInfo
2025-06-14T19:28:45.0233539Z abseil_cpp_devel-20230125.3.DependencyInfo
2025-06-14T19:28:45.0233972Z abstrakt-0.0.1~20180515.DependencyInfo
2025-06-14T19:28:45.0234408Z abstrakt_debuginfo-0.0.1~20180515.DependencyInfo
2025-06-14T19:28:45.0234865Z accounts_qml-0.7.DependencyInfo
2025-06-14T19:28:45.0235232Z ack-3.7.0.DependencyInfo
2025-06-14T19:28:45.0235562Z acme-0.96.5.DependencyInfo
2025-06-14T19:28:45.0235901Z acr-2.1.4.DependencyInfo
2025-06-14T19:28:45.0236218Z ada-2.9.2.DependencyInfo
2025-06-14T19:28:45.0236552Z ada_devel-2.9.2.DependencyInfo
2025-06-14T19:28:45.0236958Z admesh-0.98.5.DependencyInfo
2025-06-14T19:28:45.0237324Z admesh_devel-0.98.5.DependencyInfo
2025-06-14T19:28:45.0237710Z advancemame-3.10.DependencyInfo
2025-06-14T19:28:45.0238111Z adwaita_icon_theme-42.0.DependencyInfo
2025-06-14T19:28:45.0238506Z agar-1.7.0.DependencyInfo
2025-06-14T19:28:45.0238857Z agar_devel-1.7



2025-06-14T19:28:53.4687131Z Current runner version: '2.325.0'
2025-06-14T19:28:53.4714400Z ##[group]Operating System
2025-06-14T19:28:53.4715253Z Ubuntu
2025-06-14T19:28:53.4715703Z 24.04.2
2025-06-14T19:28:53.4716260Z LTS
2025-06-14T19:28:53.4716720Z ##[endgroup]
2025-06-14T19:28:53.4717230Z ##[group]Runner Image
2025-06-14T19:28:53.4717771Z Image: ubuntu-24.04
2025-06-14T19:28:53.4718361Z Version: 20250609.1.0
2025-06-14T19:28:53.4719381Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20250609.1/images/ubuntu/Ubuntu2404-Readme.md
2025-06-14T19:28:53.4720890Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20250609.1
2025-06-14T19:28:53.4721857Z ##[endgroup]
2025-06-14T19:28:53.4722341Z ##[group]Runner Image Provisioner
2025-06-14T19:28:53.4722936Z 2.0.437.1
2025-06-14T19:28:53.4723423Z ##[endgroup]
2025-06-14T19:28:53.4725777Z ##[group]GITHUB_TOKEN Permissions
2025-06-14T19:28:53.4728065Z Actions: write
2025-06-14T19:28:53.4728814Z Attestations: write
2025-06-14T19:28:53.4729438Z Checks: write
2025-06-14T19:28:53.4729943Z Contents: write
2025-06-14T19:28:53.4730776Z Deployments: write
2025-06-14T19:28:53.4731374Z Discussions: write
2025-06-14T19:28:53.4731851Z Issues: write
2025-06-14T19:28:53.4732327Z Metadata: read
2025-06-14T19:28:53.4732945Z Models: read
2025-06-14T19:28:53.4733522Z Packages: write
2025-06-14T19:28:53.4734008Z Pages: write
2025-06-14T19:28:53.4734603Z PullRequests: write
2025-06-14T19:28:53.4735158Z RepositoryProjects: write
2025-06-14T19:28:53.4735678Z SecurityEvents: write
2025-06-14T19:28:53.4736229Z Statuses: write
2025-06-14T19:28:53.4736699Z ##[endgroup]
2025-06-14T19:28:53.4738822Z Secret source: Actions
2025-06-14T19:28:53.4739955Z Prepare workflow directory
2025-06-14T19:28:53.5172384Z Prepare all required actions
2025-06-14T19:28:53.5211521Z Getting action download info
2025-06-14T19:28:53.8284975Z ##[group]Download immutable action package 'actions/checkout@v4'
2025-06-14T19:28:53.8286152Z Version: 4.2.2
2025-06-14T19:28:53.8287148Z Digest: sha256:ccb2698953eaebd21c7bf6268a94f9c26518a7e38e27e0b83c1fe1ad049819b1
2025-06-14T19:28:53.8288451Z Source commit SHA: 11bd71901bbe5b1630ceea73d27597364c9af683
2025-06-14T19:28:53.8289133Z ##[endgroup]
2025-06-14T19:28:53.9250490Z ##[group]Download immutable action package 'actions/cache@v4'
2025-06-14T19:28:53.9251353Z Version: 4.2.3
2025-06-14T19:28:53.9252084Z Digest: sha256:c8a3bb963e1f1826d8fcc8d1354f0dd29d8ac1db1d4f6f20247055ae11b81ed9
2025-06-14T19:28:53.9253186Z Source commit SHA: 5a3ec84eff668545956fd18022155c47e93e2684
2025-06-14T19:28:53.9253903Z ##[endgroup]
2025-06-14T19:28:54.0335581Z ##[group]Download immutable action package 'actions/upload-artifact@v4'
2025-06-14T19:28:54.0336439Z Version: 4.6.2
2025-06-14T19:28:54.0337166Z Digest: sha256:290722aa3281d5caf23d0acdc3dbeb3424786a1a01a9cc97e72f147225e37c38
2025-06-14T19:28:54.0338225Z Source commit SHA: ea165f8d65b6e75b540449e92b4886f43607fa02
2025-06-14T19:28:54.0338908Z ##[endgroup]
2025-06-14T19:28:54.2376445Z Complete job name: build-haikuports
2025-06-14T19:28:54.2925225Z ##[group]Checking docker version
2025-06-14T19:28:54.2938398Z ##[command]/usr/bin/docker version --format '{{.Server.APIVersion}}'
2025-06-14T19:28:54.3781303Z '1.48'
2025-06-14T19:28:54.3793951Z Docker daemon API version: '1.48'
2025-06-14T19:28:54.3794790Z ##[command]/usr/bin/docker version --format '{{.Client.APIVersion}}'
2025-06-14T19:28:54.3969489Z '1.48'
2025-06-14T19:28:54.3982834Z Docker client API version: '1.48'
2025-06-14T19:28:54.3988841Z ##[endgroup]
2025-06-14T19:28:54.3992385Z ##[group]Clean up resources from previous jobs
2025-06-14T19:28:54.3997750Z ##[command]/usr/bin/docker ps --all --quiet --no-trunc --filter "label=9c43b0"
2025-06-14T19:28:54.4146273Z ##[command]/usr/bin/docker network prune --force --filter "label=9c43b0"
2025-06-14T19:28:54.4279889Z ##[endgroup]
2025-06-14T19:28:54.4280758Z ##[group]Create local container network
2025-06-14T19:28:54.4291737Z ##[command]/usr/bin/docker network create --label 9c43b0 github_network_450eee868c4a45b0b3f1eb2abe5c2179
2025-06-14T19:28:54.4912532Z 3301fd16806ee7a964c52cc6b072cb4c404fd3dd5ee88323e2f0c87b511378dd
2025-06-14T19:28:54.4936519Z ##[endgroup]
2025-06-14T19:28:54.4974105Z ##[group]Starting job container
2025-06-14T19:28:54.5003839Z ##[command]/usr/bin/docker pull docker.io/hectorm/qemu-haiku:latest
2025-06-14T19:28:54.9513845Z latest: Pulling from hectorm/qemu-haiku
2025-06-14T19:28:55.0556784Z f557aa5ee224: Pulling fs layer
2025-06-14T19:28:55.0558225Z 542f7fa428a3: Pulling fs layer
2025-06-14T19:28:55.0559468Z 39ea4c135721: Pulling fs layer
2025-06-14T19:28:55.0560882Z 4f19a53ec18a: Pulling fs layer
2025-06-14T19:28:55.0561987Z 36ac4ff69dfa: Pulling fs layer
2025-06-14T19:28:55.0562747Z 474a15a65dbf: Pulling fs layer
2025-06-14T19:28:55.0563478Z 4f4fb700ef54: Pulling fs layer
2025-06-14T19:28:55.0564197Z 848239f4c9c9: Pulling fs layer
2025-06-14T19:28:55.0564940Z fd6fdfb194b8: Pulling fs layer
2025-06-14T19:28:55.0565697Z 28e929e3b252: Pulling fs layer
2025-06-14T19:28:55.0566477Z 474a15a65dbf: Waiting
2025-06-14T19:28:55.0567211Z 4f4fb700ef54: Waiting
2025-06-14T19:28:55.0567841Z 4f19a53ec18a: Waiting
2025-06-14T19:28:55.0568480Z 36ac4ff69dfa: Waiting
2025-06-14T19:28:55.0569158Z 848239f4c9c9: Waiting
2025-06-14T19:28:55.0569833Z fd6fdfb194b8: Waiting
2025-06-14T19:28:55.0570793Z 28e929e3b252: Waiting
2025-06-14T19:28:55.1849099Z 39ea4c135721: Verifying Checksum
2025-06-14T19:28:55.1855920Z 39ea4c135721: Download complete
2025-06-14T19:28:55.2849628Z 4f19a53ec18a: Verifying Checksum
2025-06-14T19:28:55.2854503Z 4f19a53ec18a: Download complete
2025-06-14T19:28:55.3048962Z f557aa5ee224: Verifying Checksum
2025-06-14T19:28:55.3052294Z f557aa5ee224: Download complete
2025-06-14T19:28:55.3664114Z 542f7fa428a3: Verifying Checksum
2025-06-14T19:28:55.3665663Z 542f7fa428a3: Download complete
2025-06-14T19:28:55.4203988Z 474a15a65dbf: Download complete
2025-06-14T19:28:55.4901335Z 4f4fb700ef54: Verifying Checksum
2025-06-14T19:28:55.4903558Z 4f4fb700ef54: Download complete
2025-06-14T19:28:55.5386604Z 848239f4c9c9: Verifying Checksum
2025-06-14T19:28:55.5391030Z 848239f4c9c9: Download complete
2025-06-14T19:28:55.5986091Z fd6fdfb194b8: Verifying Checksum
2025-06-14T19:28:55.5987935Z fd6fdfb194b8: Download complete
2025-06-14T19:28:55.6459853Z 28e929e3b252: Verifying Checksum
2025-06-14T19:28:55.6461832Z 28e929e3b252: Download complete
2025-06-14T19:28:56.5144881Z f557aa5ee224: Pull complete
2025-06-14T19:29:00.4318372Z 542f7fa428a3: Pull complete
2025-06-14T19:29:00.6817477Z 36ac4ff69dfa: Verifying Checksum
2025-06-14T19:29:00.6818105Z 36ac4ff69dfa: Download complete
2025-06-14T19:29:01.2799457Z 39ea4c135721: Pull complete
2025-06-14T19:29:01.3074417Z 4f19a53ec18a: Pull complete
2025-06-14T19:29:08.4831447Z 36ac4ff69dfa: Pull complete
2025-06-14T19:29:08.4971682Z 474a15a65dbf: Pull complete
2025-06-14T19:29:08.5114859Z 4f4fb700ef54: Pull complete
2025-06-14T19:29:08.5325134Z 848239f4c9c9: Pull complete
2025-06-14T19:29:08.5535119Z fd6fdfb194b8: Pull complete
2025-06-14T19:29:08.5797043Z 28e929e3b252: Pull complete
2025-06-14T19:29:08.6006785Z Digest: sha256:ff5cd760a7a820a5b00147371279d08e7a4f1e4fe5516f380846bd41d5910ac3
2025-06-14T19:29:08.6017451Z Status: Downloaded newer image for hectorm/qemu-haiku:latest
2025-06-14T19:29:08.6027700Z docker.io/hectorm/qemu-haiku:latest
2025-06-14T19:29:08.6110729Z ##[command]/usr/bin/docker create --name 7c3f467b05dd44f9870fcf4203ac21fc_dockeriohectormqemuhaikulatest_e9c54c --label 9c43b0 --workdir /haikuports/haikuports --network github_network_450eee868c4a45b0b3f1eb2abe5c2179  -e "HOME=/github/home" -e GITHUB_ACTIONS=true -e CI=true -v "/var/run/docker.sock":"/var/run/docker.sock" -v "/home/runner/work":"/__w" -v "/home/runner/runners/2.325.0/externals":"/__e":ro -v "/home/runner/work/_temp":"/__w/_temp" -v "/home/runner/work/_actions":"/__w/_actions" -v "/opt/hostedtoolcache":"/__t" -v "/home/runner/work/_temp/_github_home":"/github/home" -v "/home/runner/work/_temp/_github_workflow":"/github/workflow" --entrypoint "tail" docker.io/hectorm/qemu-haiku:latest "-f" "/dev/null"
2025-06-14T19:29:08.6383552Z 11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1
2025-06-14T19:29:08.6409197Z ##[command]/usr/bin/docker start 11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1
2025-06-14T19:29:08.8498200Z 11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1
2025-06-14T19:29:08.8520833Z ##[command]/usr/bin/docker ps --all --filter id=11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1 --filter status=running --no-trunc --format "{{.ID}} {{.Status}}"
2025-06-14T19:29:08.8641929Z 11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1 Up Less than a second
2025-06-14T19:29:08.8664304Z ##[command]/usr/bin/docker inspect --format "{{range .Config.Env}}{{println .}}{{end}}" 11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1
2025-06-14T19:29:08.8792328Z HOME=/github/home
2025-06-14T19:29:08.8792872Z GITHUB_ACTIONS=true
2025-06-14T19:29:08.8793195Z CI=true
2025-06-14T19:29:08.8793653Z PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
2025-06-14T19:29:08.8794205Z VM_CPU=2
2025-06-14T19:29:08.8794462Z VM_RAM=2048M
2025-06-14T19:29:08.8794733Z VM_KEYBOARD=en-us
2025-06-14T19:29:08.8795057Z VM_NET_EXTRA_OPTIONS=
2025-06-14T19:29:08.8795429Z VM_KVM=true
2025-06-14T19:29:08.8795687Z SVDIR=/etc/service/
2025-06-14T19:29:08.8795985Z SVWAIT=20
2025-06-14T19:29:08.8815107Z ##[endgroup]
2025-06-14T19:29:08.8824577Z ##[group]Waiting for all services to be ready
2025-06-14T19:29:08.8826245Z ##[endgroup]
2025-06-14T19:29:08.9085212Z ##[group]Run actions/checkout@v4
2025-06-14T19:29:08.9085796Z with:
2025-06-14T19:29:08.9085981Z   fetch-depth: 0
2025-06-14T19:29:08.9086182Z   repository: icarito/haikuports
2025-06-14T19:29:08.9086663Z   token: ***
2025-06-14T19:29:08.9086847Z   ssh-strict: true
2025-06-14T19:29:08.9087019Z   ssh-user: git
2025-06-14T19:29:08.9087204Z   persist-credentials: true
2025-06-14T19:29:08.9087417Z   clean: true
2025-06-14T19:29:08.9087605Z   sparse-checkout-cone-mode: true
2025-06-14T19:29:08.9087887Z   fetch-tags: false
2025-06-14T19:29:08.9088088Z   show-progress: true
2025-06-14T19:29:08.9088263Z   lfs: false
2025-06-14T19:29:08.9088422Z   submodules: false
2025-06-14T19:29:08.9088601Z   set-safe-directory: true
2025-06-14T19:29:08.9088992Z env:
2025-06-14T19:29:08.9089151Z   VM_CPU: 4
2025-06-14T19:29:08.9089301Z   VM_RAM: 15G
2025-06-14T19:29:08.9089464Z ##[endgroup]
2025-06-14T19:29:08.9147720Z ##[command]/usr/bin/docker exec  11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1 sh -c "cat /*release | grep ^ID"
2025-06-14T19:29:09.2624848Z Syncing repository: icarito/haikuports
2025-06-14T19:29:09.2626175Z ##[group]Getting Git version info
2025-06-14T19:29:09.2626513Z Working directory is '/__w/haikuports/haikuports'
2025-06-14T19:29:09.2627028Z ##[endgroup]
2025-06-14T19:29:09.2627269Z Deleting the contents of '/__w/haikuports/haikuports'
2025-06-14T19:29:09.2627627Z The repository will be downloaded using the GitHub REST API
2025-06-14T19:29:09.2628069Z To create a local Git repository instead, add Git 2.18 or higher to the PATH
2025-06-14T19:29:09.2628453Z Downloading the archive
2025-06-14T19:29:11.7728710Z Writing archive to disk
2025-06-14T19:29:11.8021127Z Extracting the archive
2025-06-14T19:29:11.8127596Z [command]/usr/bin/tar xz --warning=no-unknown-keyword --overwrite -C /haikuports/haikuports/dcc17b5e-04ee-4228-b875-aefc8224eac0 -f /haikuports/haikuports/dcc17b5e-04ee-4228-b875-aefc8224eac0.tar.gz
2025-06-14T19:29:12.6131396Z Resolved version icarito-haikuports-63b53c7
2025-06-14T19:29:12.6789982Z ##[group]Run apt-get update -y
2025-06-14T19:29:12.6790617Z [36;1mapt-get update -y[0m
2025-06-14T19:29:12.6790868Z [36;1mapt-get install -y jq[0m
2025-06-14T19:29:12.6794938Z shell: bash --noprofile --norc -e -o pipefail {0}
2025-06-14T19:29:12.6795224Z env:
2025-06-14T19:29:12.6795380Z   VM_CPU: 4
2025-06-14T19:29:12.6795533Z   VM_RAM: 15G
2025-06-14T19:29:12.6795707Z ##[endgroup]
2025-06-14T19:29:12.9403755Z Get:1 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
2025-06-14T19:29:13.0152926Z Get:2 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]
2025-06-14T19:29:13.1181516Z Get:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]
2025-06-14T19:29:13.1607797Z Get:4 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [127 kB]
2025-06-14T19:29:13.2137035Z Get:5 http://archive.ubuntu.com/ubuntu jammy/main amd64 Packages [1792 kB]
2025-06-14T19:29:13.3503369Z Get:6 http://archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages [266 kB]
2025-06-14T19:29:13.3534214Z Get:7 http://archive.ubuntu.com/ubuntu jammy/restricted amd64 Packages [164 kB]
2025-06-14T19:29:13.3546742Z Get:8 http://archive.ubuntu.com/ubuntu jammy/universe amd64 Packages [17.5 MB]
2025-06-14T19:29:13.5105115Z Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [3296 kB]
2025-06-14T19:29:13.5128318Z Get:10 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [2986 kB]
2025-06-14T19:29:13.5302966Z Get:11 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [4630 kB]
2025-06-14T19:29:13.5649085Z Get:12 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1556 kB]
2025-06-14T19:29:13.5807894Z Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [55.7 kB]
2025-06-14T19:29:13.5811687Z Get:14 http://archive.ubuntu.com/ubuntu jammy-backports/universe amd64 Packages [35.2 kB]
2025-06-14T19:29:13.5818779Z Get:15 http://archive.ubuntu.com/ubuntu jammy-backports/main amd64 Packages [83.2 kB]
2025-06-14T19:29:14.0533032Z Get:16 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1249 kB]
2025-06-14T19:29:14.0795975Z Get:17 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 Packages [47.7 kB]
2025-06-14T19:29:14.0803101Z Get:18 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [4476 kB]
2025-06-14T19:29:14.6971904Z Fetched 38.8 MB in 2s (20.2 MB/s)
2025-06-14T19:29:15.5183610Z Reading package lists...
2025-06-14T19:29:16.4034992Z Reading package lists...
2025-06-14T19:29:16.5989045Z Building dependency tree...
2025-06-14T19:29:16.5989594Z Reading state information...
2025-06-14T19:29:16.7447116Z The following additional packages will be installed:
2025-06-14T19:29:16.7451456Z   libjq1 libonig5
2025-06-14T19:29:16.7702792Z The following NEW packages will be installed:
2025-06-14T19:29:16.7708510Z   jq libjq1 libonig5
2025-06-14T19:29:16.9698410Z 0 upgraded, 3 newly installed, 0 to remove and 2 not upgraded.
2025-06-14T19:29:16.9698949Z Need to get 357 kB of archives.
2025-06-14T19:29:16.9699384Z After this operation, 1087 kB of additional disk space will be used.
2025-06-14T19:29:16.9700147Z Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 libonig5 amd64 6.9.7.1-2build1 [172 kB]
2025-06-14T19:29:17.4251499Z Get:2 http://archive.ubuntu.com/ubuntu jammy/main amd64 libjq1 amd64 1.6-2.1ubuntu3 [133 kB]
2025-06-14T19:29:17.4782321Z Get:3 http://archive.ubuntu.com/ubuntu jammy/main amd64 jq amd64 1.6-2.1ubuntu3 [52.5 kB]
2025-06-14T19:29:17.6001277Z debconf: delaying package configuration, since apt-utils is not installed
2025-06-14T19:29:17.6299097Z Fetched 357 kB in 1s (493 kB/s)
2025-06-14T19:29:17.6461177Z Selecting previously unselected package libonig5:amd64.
2025-06-14T19:29:17.6488139Z (Reading database ... 
2025-06-14T19:29:17.6488822Z (Reading database ... 5%
2025-06-14T19:29:17.6489416Z (Reading database ... 10%
2025-06-14T19:29:17.6489826Z (Reading database ... 15%
2025-06-14T19:29:17.6490856Z (Reading database ... 20%
2025-06-14T19:29:17.6491267Z (Reading database ... 25%
2025-06-14T19:29:17.6491663Z (Reading database ... 30%
2025-06-14T19:29:17.6492052Z (Reading database ... 35%
2025-06-14T19:29:17.6492449Z (Reading database ... 40%
2025-06-14T19:29:17.6492833Z (Reading database ... 45%
2025-06-14T19:29:17.6493224Z (Reading database ... 50%
2025-06-14T19:29:17.6493705Z (Reading database ... 55%
2025-06-14T19:29:17.6494114Z (Reading database ... 60%
2025-06-14T19:29:17.6500084Z (Reading database ... 65%
2025-06-14T19:29:17.6511284Z (Reading database ... 70%
2025-06-14T19:29:17.6522370Z (Reading database ... 75%
2025-06-14T19:29:17.6530680Z (Reading database ... 80%
2025-06-14T19:29:17.6540574Z (Reading database ... 85%
2025-06-14T19:29:17.6541513Z (Reading database ... 90%
2025-06-14T19:29:17.6548300Z (Reading database ... 95%
2025-06-14T19:29:17.6548710Z (Reading database ... 100%
2025-06-14T19:29:17.6549198Z (Reading database ... 7550 files and directories currently installed.)
2025-06-14T19:29:17.6556156Z Preparing to unpack .../libonig5_6.9.7.1-2build1_amd64.deb ...
2025-06-14T19:29:17.6576754Z Unpacking libonig5:amd64 (6.9.7.1-2build1) ...
2025-06-14T19:29:17.6816293Z Selecting previously unselected package libjq1:amd64.
2025-06-14T19:29:17.6827270Z Preparing to unpack .../libjq1_1.6-2.1ubuntu3_amd64.deb ...
2025-06-14T19:29:17.6838993Z Unpacking libjq1:amd64 (1.6-2.1ubuntu3) ...
2025-06-14T19:29:17.6988428Z Selecting previously unselected package jq.
2025-06-14T19:29:17.7000374Z Preparing to unpack .../jq_1.6-2.1ubuntu3_amd64.deb ...
2025-06-14T19:29:17.7012579Z Unpacking jq (1.6-2.1ubuntu3) ...
2025-06-14T19:29:17.7202094Z Setting up libonig5:amd64 (6.9.7.1-2build1) ...
2025-06-14T19:29:17.7232980Z Setting up libjq1:amd64 (1.6-2.1ubuntu3) ...
2025-06-14T19:29:17.7260951Z Setting up jq (1.6-2.1ubuntu3) ...
2025-06-14T19:29:17.7291249Z Processing triggers for libc-bin (2.35-0ubuntu3.10) ...
2025-06-14T19:29:17.7645214Z ##[group]Run container-init & timeout 600 vmshell exit 0
2025-06-14T19:29:17.7645625Z [36;1mcontainer-init & timeout 600 vmshell exit 0[0m
2025-06-14T19:29:17.7646070Z shell: sh -e {0}
2025-06-14T19:29:17.7646245Z env:
2025-06-14T19:29:17.7646397Z   VM_CPU: 4
2025-06-14T19:29:17.7646554Z   VM_RAM: 15G
2025-06-14T19:29:17.7646711Z ##[endgroup]
2025-06-14T19:29:17.8328559Z Created directory '/root/.ssh'.
2025-06-14T19:29:17.8788483Z /novnc/utils/websockify/websockify/websocket.py:31: UserWarning: no 'numpy' module, HyBi protocol will be slower
2025-06-14T19:29:17.8793629Z   warnings.warn("no 'numpy' module, HyBi protocol will be slower")
2025-06-14T19:29:17.9147078Z WebSocket server settings:
2025-06-14T19:29:17.9147666Z   - Listen on :6080
2025-06-14T19:29:17.9148017Z   - Web server. Web root: /novnc
2025-06-14T19:29:17.9148639Z   - No SSL/TLS support (no cert file)
2025-06-14T19:29:17.9152097Z   - proxying from :6080 to 127.0.0.1:5900
2025-06-14T19:29:57.6963020Z 127.0.0.1 - - [14/Jun/2025 19:29:57] "GET TP/1.1" 200 -
2025-06-14T19:29:57.7717052Z 127.0.0.1 - - [14/Jun/2025 19:29:57] code 404, message File not found
2025-06-14T19:29:57.7717772Z 127.0.0.1 - - [14/Jun/2025 19:29:57] "GET  HTTP/1.1" 404 -
2025-06-14T19:29:57.7887428Z 127.0.0.1 - - [14/Jun/2025 19:29:57] "GET  HTTP/1.1" 200 -
2025-06-14T19:29:57.8246443Z 127.0.0.1 - - [14/Jun/2025 19:29:57] "GET  HTTP/1.1" 200 -
2025-06-14T19:29:57.8562752Z 127.0.0.1 - - [14/Jun/2025 19:29:57] "GET  HTTP/1.1" 200 -
2025-06-14T19:30:10.9860669Z ##[group]Run actions/cache@v4
2025-06-14T19:30:10.9860925Z with:
2025-06-14T19:30:10.9861253Z   path: /runner/work/haikuports/haikuports
changed_recipes_list.json

2025-06-14T19:30:10.9861713Z   key: Linux-haiku-deps-v3-8ccc15b061e242ccc0e6f5e4bc1d2ed2f99239d2
2025-06-14T19:30:10.9862067Z   restore-keys: Linux-haiku-deps-v3-

2025-06-14T19:30:10.9862310Z   enableCrossOsArchive: false
2025-06-14T19:30:10.9862531Z   fail-on-cache-miss: false
2025-06-14T19:30:10.9862736Z   lookup-only: false
2025-06-14T19:30:10.9862913Z   save-always: false
2025-06-14T19:30:10.9863079Z env:
2025-06-14T19:30:10.9863216Z   VM_CPU: 4
2025-06-14T19:30:10.9863370Z   VM_RAM: 15G
2025-06-14T19:30:10.9863522Z ##[endgroup]
2025-06-14T19:30:10.9866445Z ##[command]/usr/bin/docker exec  11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1 sh -c "cat /*release | grep ^ID"
2025-06-14T19:30:11.3416578Z Cache not found for input keys: Linux-haiku-deps-v3-8ccc15b061e242ccc0e6f5e4bc1d2ed2f99239d2, Linux-haiku-deps-v3-
2025-06-14T19:30:11.3525888Z ##[group]Run vmshell pkgman install -y \
2025-06-14T19:30:11.3526623Z [36;1mvmshell pkgman install -y \[0m
2025-06-14T19:30:11.3527080Z [36;1m  gcc binutils make cmake autoconf automake \[0m
2025-06-14T19:30:11.3527404Z [36;1m  bison flex gawk gettext git gmp gperf grep \[0m
2025-06-14T19:30:11.3527701Z [36;1m  libtool m4 nasm ncurses6 patch pkgconf \[0m
2025-06-14T19:30:11.3528013Z [36;1m  python3.10 sed tar xz_utils zlib zlib_devel \[0m
2025-06-14T19:30:11.3528324Z [36;1m  curl curl_devel openssl3 openssl3_devel \[0m
2025-06-14T19:30:11.3528660Z [36;1m  glib2 glib2_devel gtk3 gtk3_devel cairo1.18 cairo1.18_devel \[0m
2025-06-14T19:30:11.3529058Z [36;1m  fontconfig fontconfig_devel freetype freetype_devel \[0m
2025-06-14T19:30:11.3529396Z [36;1m  harfbuzz harfbuzz_devel pango pango_devel \[0m
2025-06-14T19:30:11.3529716Z [36;1m  expat libffi libffi_devel libxml2 libxml2_devel \[0m
2025-06-14T19:30:11.3530114Z [36;1m  libxslt libpcre libpcre_devel libpng16 libpng16_devel \[0m
2025-06-14T19:30:11.3530765Z [36;1m  libjpeg_turbo libjpeg_turbo_devel tiff tiff_devel \[0m
2025-06-14T19:30:11.3531275Z [36;1m  libarchive libarchive_devel bzip2 bzip2_devel \[0m
2025-06-14T19:30:11.3531814Z [36;1m  libyaml libyaml_devel jsoncpp meson ninja \[0m
2025-06-14T19:30:11.3532333Z [36;1m  bash coreutils diffutils findutils gzip file \[0m
2025-06-14T19:30:11.3532974Z [36;1m  which unzip zip bc less vim nano pip_python310 jq haikuporter \[0m
2025-06-14T19:30:11.3533644Z [36;1m  json_glib_devel json_glib wayland_protocols gtk_doc \[0m
2025-06-14T19:30:11.3534166Z [36;1m  zstd_devel zstd[0m
2025-06-14T19:30:11.3534674Z shell: sh -e {0}
2025-06-14T19:30:11.3534956Z env:
2025-06-14T19:30:11.3535213Z   VM_CPU: 4
2025-06-14T19:30:11.3535473Z   VM_RAM: 15G
2025-06-14T19:30:11.3535754Z ##[endgroup]
2025-06-14T19:30:14.8974486Z   100% repochecksum-1 [65 bytes]
2025-06-14T19:30:20.8007128Z Validating checksum for Haiku...done.
2025-06-14T19:30:20.8007676Z   100% repochecksum-1 [64 bytes]
2025-06-14T19:30:22.2769229Z Validating checksum for HaikuPorts...done.
2025-06-14T19:30:22.2769808Z   100% repocache-2 [2.14 MiB]
2025-06-14T19:30:32.2545193Z Validating checksum for HaikuPorts...done.
2025-06-14T19:30:32.2545798Z The following changes will be made:
2025-06-14T19:30:32.2546173Z   in system:
2025-06-14T19:30:32.2546565Z     install package binutils-2.42-1 from repository HaikuPorts
2025-06-14T19:30:32.2547163Z     install package make-4.4.1-1 from repository HaikuPorts
2025-06-14T19:30:32.2547757Z     install package gettext-0.22.5-1 from repository HaikuPorts
2025-06-14T19:30:32.2548328Z     install package gperf-3.1-1 from repository HaikuPorts
2025-06-14T19:30:32.2548874Z     install package m4-1.4.19-1 from repository HaikuPorts
2025-06-14T19:30:32.2549426Z     install package nasm-2.15.05-2 from repository HaikuPorts
2025-06-14T19:30:32.2550008Z     install package patch-2.7.6-2 from repository HaikuPorts
2025-06-14T19:30:32.2550867Z     install package pkgconf-1.5.3-2 from repository HaikuPorts
2025-06-14T19:30:32.2551486Z     install package zlib_devel-1.3.1-4 from repository HaikuPorts
2025-06-14T19:30:32.2552131Z     install package curl_devel-8.13.0-2 from repository HaikuPorts
2025-06-14T19:30:32.2552773Z     install package openssl3_devel-3.5.0-2 from repository HaikuPorts
2025-06-14T19:30:32.2553398Z     install package glib2-2.78.0-2 from repository HaikuPorts
2025-06-14T19:30:32.2553998Z     install package libffi_devel-3.4.6-1 from repository HaikuPorts
2025-06-14T19:30:32.2554626Z     install package libpcre_devel-8.45-3 from repository HaikuPorts
2025-06-14T19:30:32.2555242Z     install package libpng16_devel-1.6.44-1 from repository HaikuPorts
2025-06-14T19:30:32.2555965Z     install package libjpeg_turbo_devel-2.1.5.1-1 from repository HaikuPorts
2025-06-14T19:30:32.2556677Z     install package tiff_devel-4.7.0-1 from repository HaikuPorts
2025-06-14T19:30:32.2557304Z     install package libarchive-3.7.9-1 from repository HaikuPorts
2025-06-14T19:30:32.2558439Z     install package bzip2_devel-1.0.8-3 from repository HaikuPorts
2025-06-14T19:30:32.2559256Z     install package libyaml-0.2.5-2 from repository HaikuPorts
2025-06-14T19:30:32.2559850Z     install package jsoncpp-1.9.5-3 from repository HaikuPorts
2025-06-14T19:30:32.2560610Z     install package ninja-1.12.1-1 from repository HaikuPorts
2025-06-14T19:30:32.2561187Z     install package vim-9.1.1153-1 from repository HaikuPorts
2025-06-14T19:30:32.2561802Z     install package haikuporter-1.3.1-1 from repository HaikuPorts
2025-06-14T19:30:32.2562448Z     install package wayland_protocols-1.36-1 from repository HaikuPorts
2025-06-14T19:30:32.2563113Z     install package zstd_devel-1.5.6-2 from repository HaikuPorts
2025-06-14T19:30:32.2563696Z     install package mpfr-4.2.0-3 from repository HaikuPorts
2025-06-14T19:30:32.2564262Z     install package rhash-1.4.4-3 from repository HaikuPorts
2025-06-14T19:30:32.2564866Z     install package libuv-1.48.0-1 from repository HaikuPorts
2025-06-14T19:30:32.2565504Z     install package libtool_libltdl-2.4.7-1 from repository HaikuPorts
2025-06-14T19:30:32.2566188Z     install package libpcre2_devel-10.45-1 from repository HaikuPorts
2025-06-14T19:30:32.2566838Z     install package libiconv_devel-1.17-4 from repository HaikuPorts
2025-06-14T19:30:32.2567545Z     install package gettext_libintl_devel-0.22.5-1 from repository HaikuPorts
2025-06-14T19:30:32.2568260Z     install package adwaita_icon_theme-42.0-2 from repository HaikuPorts
2025-06-14T19:30:32.2568983Z     install package haiku_svg_icon_theme-5.15.2.38-1 from repository HaikuPorts
2025-06-14T19:30:32.2569684Z     install package wayland-1.21.0~git-3 from repository HaikuPorts
2025-06-14T19:30:32.2570496Z     install package iso_codes-4.17.0-1 from repository HaikuPorts
2025-06-14T19:30:32.2571127Z     install package libepoxy-1.5.8-3 from repository HaikuPorts
2025-06-14T19:30:32.2571723Z     install package pixman-0.42.2-1 from repository HaikuPorts
2025-06-14T19:30:32.2572361Z     install package icu74_devel-74.1-6 from repository HaikuPorts
2025-06-14T19:30:32.2573035Z     install package graphite2_devel-1.3.14-2 from repository HaikuPorts
2025-06-14T19:30:32.2573753Z     install package fribidi_devel-1.0.16-1 from repository HaikuPorts
2025-06-14T19:30:32.2574485Z     install package setuptools_python310-68.2.2-1 from repository HaikuPorts
2025-06-14T19:30:32.2575208Z     install package oniguruma-6.9.8-1 from repository HaikuPorts
2025-06-14T19:30:32.2575853Z     install package libxslt_tools-1.1.43-1 from repository HaikuPorts
2025-06-14T19:30:32.2576540Z     install package pygments_python310-2.14.0-4 from repository HaikuPorts
2025-06-14T19:30:32.2577230Z     install package six_python310-1.15.0-5 from repository HaikuPorts
2025-06-14T19:30:32.2577854Z     install package libuuid-1.3.1-5 from repository HaikuPorts
2025-06-14T19:30:32.2578490Z     install package xkeyboard_config-2.41-1 from repository HaikuPorts
2025-06-14T19:30:32.2579152Z     install package docbook_xml_dtd-4.5-2 from repository HaikuPorts
2025-06-14T19:30:32.2579765Z     install package flex-2.6.4-4 from repository HaikuPorts
2025-06-14T19:30:32.2580530Z     install package bison-3.8.2-1 from repository HaikuPorts
2025-06-14T19:30:32.2581120Z     install package automake-1.16.5-3 from repository HaikuPorts
2025-06-14T19:30:32.2581716Z     install package autoconf-2.72-1 from repository HaikuPorts
2025-06-14T19:30:32.2582318Z     install package libcroco-0.6.13-2 from repository HaikuPorts
2025-06-14T19:30:32.2582965Z     install package shared_mime_info-1.15-2 from repository HaikuPorts
2025-06-14T19:30:32.2583669Z     install package gobject_introspection-1.78.1-1 from repository HaikuPorts
2025-06-14T19:30:32.2584356Z     install package harfbuzz_glib-8.3.0-2 from repository HaikuPorts
2025-06-14T19:30:32.2584950Z     install package libyaml_devel-0.2.5-2 from repository HaikuPorts
2025-06-14T19:30:32.2585573Z     install package mpc-1.2.1-2 from repository HaikuPorts
2025-06-14T19:30:32.2586449Z     install package cmake-3.31.5-1 from repository HaikuPorts
2025-06-14T19:30:32.2587147Z     install package libarchive_devel-3.7.9-1 from repository HaikuPorts
2025-06-14T19:30:32.2588173Z     install package libxml2_devel-2.12.10-1 from repository HaikuPorts
2025-06-14T19:30:32.2588907Z     install package glib2_devel-2.78.0-2 from repository HaikuPorts
2025-06-14T19:30:32.2589627Z     install package wayland_devel-1.21.0~git-3 from repository HaikuPorts
2025-06-14T19:30:32.2590589Z     install package wayland_server-0.1.20250303-1 from repository HaikuPorts
2025-06-14T19:30:32.2591341Z     install package libepoxy_devel-1.5.8-3 from repository HaikuPorts
2025-06-14T19:30:32.2592008Z     install package pixman_devel-0.42.2-1 from repository HaikuPorts
2025-06-14T19:30:32.2592692Z     install package cairo1.18-1.18.0-1 from repository HaikuPorts
2025-06-14T19:30:32.2593363Z     install package pip_python310-23.2.1-3 from repository HaikuPorts
2025-06-14T19:30:32.2593990Z     install package meson-1.6.0-1 from repository HaikuPorts
2025-06-14T19:30:32.2594563Z     install package jq-1.7-2 from repository HaikuPorts
2025-06-14T19:30:32.2595154Z     install package libxkbcommon-1.7.0-1 from repository HaikuPorts
2025-06-14T19:30:32.2595860Z     install package docbook_xsl_stylesheets-1.79.2-3 from repository HaikuPorts
2025-06-14T19:30:32.2596546Z     install package libtool-2.4.7-1 from repository HaikuPorts
2025-06-14T19:30:32.2597150Z     install package gdk_pixbuf-2.42.9-5 from repository HaikuPorts
2025-06-14T19:30:32.2597743Z     install package atk-2.38.0-3 from repository HaikuPorts
2025-06-14T19:30:32.2598535Z     install package gsettings_desktop_schemas-43.0-2 from repository HaikuPorts
2025-06-14T19:30:32.2599241Z     install package json_glib-1.6.6-2 from repository HaikuPorts
2025-06-14T19:30:32.2599879Z     install package gcc-13.3.0_2023_08_10-4 from repository HaikuPorts
2025-06-14T19:30:32.2600781Z     install package gobject_introspection_devel-1.78.1-1 from repository HaikuPorts
2025-06-14T19:30:32.2601551Z     install package harfbuzz_devel-8.3.0-2 from repository HaikuPorts
2025-06-14T19:30:32.2602170Z     install package pango-1.54.0-2 from repository HaikuPorts
2025-06-14T19:30:32.2602829Z     install package libxkbcommon_devel-1.7.0-1 from repository HaikuPorts
2025-06-14T19:30:32.2603491Z     install package gtk_doc-1.33.2-5 from repository HaikuPorts
2025-06-14T19:30:32.2604132Z     install package json_glib_devel-1.6.6-2 from repository HaikuPorts
2025-06-14T19:30:32.2604818Z     install package gdk_pixbuf_devel-2.42.9-5 from repository HaikuPorts
2025-06-14T19:30:32.2605467Z     install package atk_devel-2.38.0-3 from repository HaikuPorts
2025-06-14T19:30:32.2606114Z     install package freetype_devel-2.13.3-1 from repository HaikuPorts
2025-06-14T19:30:32.2606740Z     install package librsvg-2.50.7-4 from repository HaikuPorts
2025-06-14T19:30:32.2607387Z     install package fontconfig_devel-2.13.96-2 from repository HaikuPorts
2025-06-14T19:30:32.2608035Z     install package gtk3-3.24.36-2 from repository HaikuPorts
2025-06-14T19:30:32.2608665Z     install package cairo1.18_devel-1.18.0-1 from repository HaikuPorts
2025-06-14T19:30:32.2609336Z     install package pango_devel-1.54.0-2 from repository HaikuPorts
2025-06-14T19:30:32.2609973Z     install package gtk3_devel-3.24.36-2 from repository HaikuPorts
2025-06-14T19:30:32.2610678Z Continue? [yes/no] (yes) : yes
2025-06-14T19:30:32.2611057Z   100% binutils-2.42-1-x86_64.hpkg [11.92 MiB]
2025-06-14T19:30:33.8192140Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/binutils-2.42-1-x86_64.hpkg...done.
2025-06-14T19:30:33.8193156Z   100% make-4.4.1-1-x86_64.hpkg [314.00 KiB]
2025-06-14T19:30:36.8321042Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/make-4.4.1-1-x86_64.hpkg...done.
2025-06-14T19:30:36.8321882Z   100% gettext-0.22.5-1-x86_64.hpkg [10.71 MiB]
2025-06-14T19:30:38.2484155Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gettext-0.22.5-1-x86_64.hpkg...done.
2025-06-14T19:30:38.2485019Z   100% gperf-3.1-1-x86_64.hpkg [198.73 KiB]
2025-06-14T19:30:39.1104642Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gperf-3.1-1-x86_64.hpkg...done.
2025-06-14T19:30:39.1105628Z   100% m4-1.4.19-1-x86_64.hpkg [259.93 KiB]
2025-06-14T19:30:40.1119013Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/m4-1.4.19-1-x86_64.hpkg...done.
2025-06-14T19:30:40.1120064Z   100% nasm-2.15.05-2-x86_64.hpkg [589.81 KiB]
2025-06-14T19:30:41.0441181Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/nasm-2.15.05-2-x86_64.hpkg...done.
2025-06-14T19:30:41.0441811Z   100% patch-2.7.6-2-x86_64.hpkg [329.80 KiB]
2025-06-14T19:30:41.7032879Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/patch-2.7.6-2-x86_64.hpkg...done.
2025-06-14T19:30:41.7033790Z   100% pkgconf-1.5.3-2-x86_64.hpkg [56.73 KiB]
2025-06-14T19:30:42.2808462Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/pkgconf-1.5.3-2-x86_64.hpkg...done.
2025-06-14T19:30:42.2809612Z   100% zlib_devel-1.3.1-4-x86_64.hpkg [32.26 KiB]
2025-06-14T19:30:43.2026993Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/zlib_devel-1.3.1-4-x86_64.hpkg...done.
2025-06-14T19:30:43.2027800Z   100% curl_devel-8.13.0-2-x86_64.hpkg [349.00 KiB]
2025-06-14T19:30:44.4426118Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/curl_devel-8.13.0-2-x86_64.hpkg...done.
2025-06-14T19:30:44.4427190Z   100% openssl3_devel-3.5.0-2-x86_64.hpkg [2.03 MiB]
2025-06-14T19:30:45.8008998Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/openssl3_devel-3.5.0-2-x86_64.hpkg...done.
2025-06-14T19:30:45.8010067Z   100% glib2-2.78.0-2-x86_64.hpkg [1.74 MiB]
2025-06-14T19:30:46.2666364Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/glib2-2.78.0-2-x86_64.hpkg...done.
2025-06-14T19:30:46.2667636Z   100% libffi_devel-3.4.6-1-x86_64.hpkg [16.82 KiB]
2025-06-14T19:30:47.0768236Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libffi_devel-3.4.6-1-x86_64.hpkg...done.
2025-06-14T19:30:47.0769155Z   100% libpcre_devel-8.45-3-x86_64.hpkg [181.19 KiB]
2025-06-14T19:30:47.9067668Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libpcre_devel-8.45-3-x86_64.hpkg...done.
2025-06-14T19:30:47.9068473Z   100% libpng16_devel-1.6.44-1-x86_64.hpkg [179.15 KiB]
2025-06-14T19:30:48.5061212Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libpng16_devel-1.6.44-1-x86_64.hpkg...done.
2025-06-14T19:30:48.5062368Z   100% libjpeg_turbo_devel-2.1.5.1-1-x86_64.hpkg [45.75 KiB]
2025-06-14T19:30:49.5719051Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libjpeg_turbo_devel-2.1.5.1-1-x86_64.hpkg...done.
2025-06-14T19:30:49.5720396Z   100% tiff_devel-4.7.0-1-x86_64.hpkg [1.04 MiB]
2025-06-14T19:30:50.4750878Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/tiff_devel-4.7.0-1-x86_64.hpkg...done.
2025-06-14T19:30:50.4752012Z   100% libarchive-3.7.9-1-x86_64.hpkg [392.12 KiB]
2025-06-14T19:30:50.9254641Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libarchive-3.7.9-1-x86_64.hpkg...done.
2025-06-14T19:30:50.9255637Z   100% bzip2_devel-1.0.8-3-x86_64.hpkg [3.52 KiB]
2025-06-14T19:30:51.5759208Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/bzip2_devel-1.0.8-3-x86_64.hpkg...done.
2025-06-14T19:30:51.5760417Z   100% libyaml-0.2.5-2-x86_64.hpkg [54.47 KiB]
2025-06-14T19:30:52.3237902Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libyaml-0.2.5-2-x86_64.hpkg...done.
2025-06-14T19:30:52.3239244Z   100% jsoncpp-1.9.5-3-x86_64.hpkg [109.34 KiB]
2025-06-14T19:30:53.1007166Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/jsoncpp-1.9.5-3-x86_64.hpkg...done.
2025-06-14T19:30:53.1009021Z   100% ninja-1.12.1-1-x86_64.hpkg [158.78 KiB]
2025-06-14T19:30:57.1402056Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/ninja-1.12.1-1-x86_64.hpkg...done.
2025-06-14T19:30:57.1403193Z   100% vim-9.1.1153-1-x86_64.hpkg [15.24 MiB]
2025-06-14T19:30:58.7084441Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/vim-9.1.1153-1-x86_64.hpkg...done.
2025-06-14T19:30:58.7085253Z   100% haikuporter-1.3.1-1-any.hpkg [89.80 KiB]
2025-06-14T19:30:59.5012330Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/haikuporter-1.3.1-1-any.hpkg...done.
2025-06-14T19:30:59.5013215Z   100% wayland_protocols-1.36-1-any.hpkg [146.06 KiB]
2025-06-14T19:31:00.2109883Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/wayland_protocols-1.36-1-any.hpkg...done.
2025-06-14T19:31:00.2111216Z   100% zstd_devel-1.5.6-2-x86_64.hpkg [84.61 KiB]
2025-06-14T19:31:01.1278801Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/zstd_devel-1.5.6-2-x86_64.hpkg...done.
2025-06-14T19:31:01.1279819Z   100% mpfr-4.2.0-3-x86_64.hpkg [382.02 KiB]
2025-06-14T19:31:01.9732952Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/mpfr-4.2.0-3-x86_64.hpkg...done.
2025-06-14T19:31:01.9734181Z   100% rhash-1.4.4-3-x86_64.hpkg [188.76 KiB]
2025-06-14T19:31:02.6921897Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/rhash-1.4.4-3-x86_64.hpkg...done.
2025-06-14T19:31:02.6922744Z   100% libuv-1.48.0-1-x86_64.hpkg [85.74 KiB]
2025-06-14T19:31:03.3040797Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libuv-1.48.0-1-x86_64.hpkg...done.
2025-06-14T19:31:03.3041843Z   100% libtool_libltdl-2.4.7-1-x86_64.hpkg [49.62 KiB]
2025-06-14T19:31:04.1543205Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libtool_libltdl-2.4.7-1-x86_64.hpkg...done.
2025-06-14T19:31:04.1544087Z   100% libpcre2_devel-10.45-1-x86_64.hpkg [210.62 KiB]
2025-06-14T19:31:04.6368905Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libpcre2_devel-10.45-1-x86_64.hpkg...done.
2025-06-14T19:31:04.6369884Z   100% libiconv_devel-1.17-4-x86_64.hpkg [16.28 KiB]
2025-06-14T19:31:05.0004407Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libiconv_devel-1.17-4-x86_64.hpkg...done.
2025-06-14T19:31:05.0005489Z   100% gettext_libintl_devel-0.22.5-1-x86_64.hpkg [6.44 KiB]
2025-06-14T19:31:06.4406823Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gettext_libintl_devel-0.22.5-1-x86_64.hpkg...done.
2025-06-14T19:31:06.4407727Z   100% adwaita_icon_theme-42.0-2-any.hpkg [3.26 MiB]
2025-06-14T19:31:08.2185338Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/adwaita_icon_theme-42.0-2-any.hpkg...done.
2025-06-14T19:31:08.2186444Z   100% haiku_svg_icon_theme-5.15.2.38-1-any.hpkg [3.52 MiB]
2025-06-14T19:31:09.1696316Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/haiku_svg_icon_theme-5.15.2.38-1-any.hpkg...done.
2025-06-14T19:31:09.1697211Z   100% wayland-1.21.0~git-3-x86_64.hpkg [120.58 KiB]
2025-06-14T19:31:11.2578683Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/wayland-1.21.0~git-3-x86_64.hpkg...done.
2025-06-14T19:31:11.2579844Z   100% iso_codes-4.17.0-1-any.hpkg [6.19 MiB]
2025-06-14T19:31:12.4851515Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/iso_codes-4.17.0-1-any.hpkg...done.
2025-06-14T19:31:12.4852578Z   100% libepoxy-1.5.8-3-x86_64.hpkg [322.87 KiB]
2025-06-14T19:31:13.6049264Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libepoxy-1.5.8-3-x86_64.hpkg...done.
2025-06-14T19:31:13.6050525Z   100% pixman-0.42.2-1-x86_64.hpkg [1.63 MiB]
2025-06-14T19:31:14.7728859Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/pixman-0.42.2-1-x86_64.hpkg...done.
2025-06-14T19:31:14.7730759Z   100% icu74_devel-74.1-6-x86_64.hpkg [940.01 KiB]
2025-06-14T19:31:15.3773492Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/icu74_devel-74.1-6-x86_64.hpkg...done.
2025-06-14T19:31:15.3774564Z   100% graphite2_devel-1.3.14-2-x86_64.hpkg [25.11 KiB]
2025-06-14T19:31:15.9228404Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/graphite2_devel-1.3.14-2-x86_64.hpkg...done.
2025-06-14T19:31:15.9229652Z   100% fribidi_devel-1.0.16-1-x86_64.hpkg [23.42 KiB]
2025-06-14T19:31:17.1001457Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/fribidi_devel-1.0.16-1-x86_64.hpkg...done.
2025-06-14T19:31:17.1002445Z   100% setuptools_python310-68.2.2-1-any.hpkg [1.50 MiB]
2025-06-14T19:31:18.1409655Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/setuptools_python310-68.2.2-1-any.hpkg...done.
2025-06-14T19:31:18.1410974Z   100% oniguruma-6.9.8-1-x86_64.hpkg [507.51 KiB]
2025-06-14T19:31:18.7282287Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/oniguruma-6.9.8-1-x86_64.hpkg...done.
2025-06-14T19:31:18.7283379Z   100% libxslt_tools-1.1.43-1-x86_64.hpkg [32.79 KiB]
2025-06-14T19:31:20.0267006Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libxslt_tools-1.1.43-1-x86_64.hpkg...done.
2025-06-14T19:31:20.0267910Z   100% pygments_python310-2.14.0-4-any.hpkg [2.09 MiB]
2025-06-14T19:31:20.6990074Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/pygments_python310-2.14.0-4-any.hpkg...done.
2025-06-14T19:31:20.6991745Z   100% six_python310-1.15.0-5-any.hpkg [20.90 KiB]
2025-06-14T19:31:21.1538394Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/six_python310-1.15.0-5-any.hpkg...done.
2025-06-14T19:31:21.1539474Z   100% libuuid-1.3.1-5-x86_64.hpkg [15.93 KiB]
2025-06-14T19:31:22.1318184Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libuuid-1.3.1-5-x86_64.hpkg...done.
2025-06-14T19:31:22.1319038Z   100% xkeyboard_config-2.41-1-x86_64.hpkg [566.56 KiB]
2025-06-14T19:31:22.7552174Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/xkeyboard_config-2.41-1-x86_64.hpkg...done.
2025-06-14T19:31:22.7553318Z   100% docbook_xml_dtd-4.5-2-any.hpkg [79.65 KiB]
2025-06-14T19:31:23.6122914Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/docbook_xml_dtd-4.5-2-any.hpkg...done.
2025-06-14T19:31:23.6123777Z   100% flex-2.6.4-4-x86_64.hpkg [399.30 KiB]
2025-06-14T19:31:24.6094126Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/flex-2.6.4-4-x86_64.hpkg...done.
2025-06-14T19:31:24.6095139Z   100% bison-3.8.2-1-x86_64.hpkg [612.21 KiB]
2025-06-14T19:31:25.6676302Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/bison-3.8.2-1-x86_64.hpkg...done.
2025-06-14T19:31:25.6677642Z   100% automake-1.16.5-3-x86_64.hpkg [779.51 KiB]
2025-06-14T19:31:26.8397684Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/automake-1.16.5-3-x86_64.hpkg...done.
2025-06-14T19:31:26.8399160Z   100% autoconf-2.72-1-x86_64.hpkg [1.50 MiB]
2025-06-14T19:31:27.7405459Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/autoconf-2.72-1-x86_64.hpkg...done.
2025-06-14T19:31:27.7407284Z   100% libcroco-0.6.13-2-x86_64.hpkg [375.38 KiB]
2025-06-14T19:31:28.9649163Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libcroco-0.6.13-2-x86_64.hpkg...done.
2025-06-14T19:31:28.9650126Z   100% shared_mime_info-1.15-2-x86_64.hpkg [1.54 MiB]
2025-06-14T19:31:30.3892925Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/shared_mime_info-1.15-2-x86_64.hpkg...done.
2025-06-14T19:31:30.3894060Z   100% gobject_introspection-1.78.1-1-x86_64.hpkg [2.03 MiB]
2025-06-14T19:31:31.3345287Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gobject_introspection-1.78.1-1-x86_64.hpkg...done.
2025-06-14T19:31:31.3346667Z   100% harfbuzz_glib-8.3.0-2-x86_64.hpkg [203.72 KiB]
2025-06-14T19:31:31.7899769Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/harfbuzz_glib-8.3.0-2-x86_64.hpkg...done.
2025-06-14T19:31:31.7901150Z   100% libyaml_devel-0.2.5-2-x86_64.hpkg [9.84 KiB]
2025-06-14T19:31:32.4683270Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libyaml_devel-0.2.5-2-x86_64.hpkg...done.
2025-06-14T19:31:32.4684124Z   100% mpc-1.2.1-2-x86_64.hpkg [74.79 KiB]
2025-06-14T19:31:37.9492190Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/mpc-1.2.1-2-x86_64.hpkg...done.
2025-06-14T19:31:37.9493250Z   100% cmake-3.31.5-1-x86_64.hpkg [23.54 MiB]
2025-06-14T19:31:39.9673831Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/cmake-3.31.5-1-x86_64.hpkg...done.
2025-06-14T19:31:39.9674864Z   100% libarchive_devel-3.7.9-1-x86_64.hpkg [68.28 KiB]
2025-06-14T19:31:40.9193900Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libarchive_devel-3.7.9-1-x86_64.hpkg...done.
2025-06-14T19:31:40.9194904Z   100% libxml2_devel-2.12.10-1-x86_64.hpkg [430.92 KiB]
2025-06-14T19:31:41.8782406Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libxml2_devel-2.12.10-1-x86_64.hpkg...done.
2025-06-14T19:31:41.8783719Z   100% glib2_devel-2.78.0-2-x86_64.hpkg [440.16 KiB]
2025-06-14T19:31:42.5974940Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/glib2_devel-2.78.0-2-x86_64.hpkg...done.
2025-06-14T19:31:42.5976439Z   100% wayland_devel-1.21.0~git-3-x86_64.hpkg [83.12 KiB]
2025-06-14T19:31:43.2637342Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/wayland_devel-1.21.0~git-3-x86_64.hpkg...done.
2025-06-14T19:31:43.2638243Z   100% wayland_server-0.1.20250303-1-x86_64.hpkg [67.89 KiB]
2025-06-14T19:31:44.0576542Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/wayland_server-0.1.20250303-1-x86_64.hpkg...done.
2025-06-14T19:31:44.0577516Z   100% libepoxy_devel-1.5.8-3-x86_64.hpkg [161.96 KiB]
2025-06-14T19:31:44.5019946Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libepoxy_devel-1.5.8-3-x86_64.hpkg...done.
2025-06-14T19:31:44.5021274Z   100% pixman_devel-0.42.2-1-x86_64.hpkg [10.35 KiB]
2025-06-14T19:31:45.5048354Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/pixman_devel-0.42.2-1-x86_64.hpkg...done.
2025-06-14T19:31:45.5049250Z   100% cairo1.18-1.18.0-1-x86_64.hpkg [717.68 KiB]
2025-06-14T19:31:47.3128586Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/cairo1.18-1.18.0-1-x86_64.hpkg...done.
2025-06-14T19:31:47.3129660Z   100% pip_python310-23.2.1-3-any.hpkg [3.54 MiB]
2025-06-14T19:31:48.7121906Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/pip_python310-23.2.1-3-any.hpkg...done.
2025-06-14T19:31:48.7123146Z   100% meson-1.6.0-1-any.hpkg [1.87 MiB]
2025-06-14T19:31:49.8107621Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/meson-1.6.0-1-any.hpkg...done.
2025-06-14T19:31:49.8108382Z   100% jq-1.7-2-x86_64.hpkg [541.06 KiB]
2025-06-14T19:31:50.6713738Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/jq-1.7-2-x86_64.hpkg...done.
2025-06-14T19:31:50.6714966Z   100% libxkbcommon-1.7.0-1-x86_64.hpkg [212.40 KiB]
2025-06-14T19:31:56.5486453Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libxkbcommon-1.7.0-1-x86_64.hpkg...done.
2025-06-14T19:31:56.5487644Z   100% docbook_xsl_stylesheets-1.79.2-3-any.hpkg [22.62 MiB]
2025-06-14T19:31:58.7508104Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/docbook_xsl_stylesheets-1.79.2-3-any.hpkg...done.
2025-06-14T19:31:58.7509231Z   100% libtool-2.4.7-1-x86_64.hpkg [619.49 KiB]
2025-06-14T19:31:59.6171021Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libtool-2.4.7-1-x86_64.hpkg...done.
2025-06-14T19:31:59.6172051Z   100% gdk_pixbuf-2.42.9-5-x86_64.hpkg [224.71 KiB]
2025-06-14T19:32:00.5573831Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gdk_pixbuf-2.42.9-5-x86_64.hpkg...done.
2025-06-14T19:32:00.5574869Z   100% atk-2.38.0-3-x86_64.hpkg [434.38 KiB]
2025-06-14T19:32:01.6127288Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/atk-2.38.0-3-x86_64.hpkg...done.
2025-06-14T19:32:01.6128354Z   100% gsettings_desktop_schemas-43.0-2-x86_64.hpkg [1.50 MiB]
2025-06-14T19:32:02.6398823Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gsettings_desktop_schemas-43.0-2-x86_64.hpkg...done.
2025-06-14T19:32:02.6399589Z   100% json_glib-1.6.6-2-x86_64.hpkg [362.04 KiB]
2025-06-14T19:32:20.1232024Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/json_glib-1.6.6-2-x86_64.hpkg...done.
2025-06-14T19:32:20.1233379Z   100% gcc-13.3.0_2023_08_10-4-x86_64.hpkg [76.00 MiB]
2025-06-14T19:32:24.8122410Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gcc-13.3.0_2023_08_10-4-x86_64.hpkg...done.
2025-06-14T19:32:24.8123553Z   100% gobject_introspection_devel-1.78.1-1-x86_64.hpkg [14.34 KiB]
2025-06-14T19:32:25.7600951Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gobject_introspection_devel-1.78.1-1-x86_64.hpkg...done.
2025-06-14T19:32:25.7601818Z   100% harfbuzz_devel-8.3.0-2-x86_64.hpkg [417.01 KiB]
2025-06-14T19:32:26.8424590Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/harfbuzz_devel-8.3.0-2-x86_64.hpkg...done.
2025-06-14T19:32:26.8425461Z   100% pango-1.54.0-2-x86_64.hpkg [888.74 KiB]
2025-06-14T19:32:27.5707845Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/pango-1.54.0-2-x86_64.hpkg...done.
2025-06-14T19:32:27.5708774Z   100% libxkbcommon_devel-1.7.0-1-x86_64.hpkg [74.37 KiB]
2025-06-14T19:32:28.5106224Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/libxkbcommon_devel-1.7.0-1-x86_64.hpkg...done.
2025-06-14T19:32:28.5107096Z   100% gtk_doc-1.33.2-5-any.hpkg [640.94 KiB]
2025-06-14T19:32:28.9872825Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gtk_doc-1.33.2-5-any.hpkg...done.
2025-06-14T19:32:28.9874054Z   100% json_glib_devel-1.6.6-2-x86_64.hpkg [11.86 KiB]
2025-06-14T19:32:29.4547540Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/json_glib_devel-1.6.6-2-x86_64.hpkg...done.
2025-06-14T19:32:29.4548841Z   100% gdk_pixbuf_devel-2.42.9-5-x86_64.hpkg [18.22 KiB]
2025-06-14T19:32:30.0647336Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gdk_pixbuf_devel-2.42.9-5-x86_64.hpkg...done.
2025-06-14T19:32:30.0648916Z   100% atk_devel-2.38.0-3-x86_64.hpkg [43.21 KiB]
2025-06-14T19:32:30.8774290Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/atk_devel-2.38.0-3-x86_64.hpkg...done.
2025-06-14T19:32:30.8775312Z   100% freetype_devel-2.13.3-1-x86_64.hpkg [183.31 KiB]
2025-06-14T19:32:32.9744623Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/freetype_devel-2.13.3-1-x86_64.hpkg...done.
2025-06-14T19:32:32.9745414Z   100% librsvg-2.50.7-4-x86_64.hpkg [5.55 MiB]
2025-06-14T19:32:34.1747773Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/librsvg-2.50.7-4-x86_64.hpkg...done.
2025-06-14T19:32:34.1748618Z   100% fontconfig_devel-2.13.96-2-x86_64.hpkg [689.93 KiB]
2025-06-14T19:32:36.5679331Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/fontconfig_devel-2.13.96-2-x86_64.hpkg...done.
2025-06-14T19:32:36.5680147Z   100% gtk3-3.24.36-2-x86_64.hpkg [6.46 MiB]
2025-06-14T19:32:37.8071093Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gtk3-3.24.36-2-x86_64.hpkg...done.
2025-06-14T19:32:37.8072234Z   100% cairo1.18_devel-1.18.0-1-x86_64.hpkg [281.52 KiB]
2025-06-14T19:32:38.6384875Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/cairo1.18_devel-1.18.0-1-x86_64.hpkg...done.
2025-06-14T19:32:38.6385681Z   100% pango_devel-1.54.0-2-x86_64.hpkg [191.04 KiB]
2025-06-14T19:32:39.5378695Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/pango_devel-1.54.0-2-x86_64.hpkg...done.
2025-06-14T19:32:39.5379809Z   100% gtk3_devel-3.24.36-2-x86_64.hpkg [319.23 KiB]
2025-06-14T19:32:45.8074143Z Validating checksum for https://eu.hpkg.haiku-os.org/haikuports/r1beta5/x86_64/current/packages/gtk3_devel-3.24.36-2-x86_64.hpkg...done.
2025-06-14T19:32:45.8075222Z [system] Applying changes ...
2025-06-14T19:32:45.8075853Z [system] Changes applied. Old activation state backed up in "state_2025-06-09_05:07:31"
2025-06-14T19:32:45.8076525Z [system] Cleaning up ...
2025-06-14T19:32:45.8076870Z [system] Done.
2025-06-14T19:32:45.8169513Z ##[group]Run vmshell "mkdir -p /home/haikuports && \
2025-06-14T19:32:45.8170576Z [36;1mvmshell "mkdir -p /home/haikuports && \[0m
2025-06-14T19:32:45.8171373Z [36;1m  git clone https://github.com/${GITHUB_REPOSITORY}.git /home/haikuports && \[0m
2025-06-14T19:32:45.8172088Z [36;1m  cd /home/haikuports && \[0m
2025-06-14T19:32:45.8172556Z [36;1m  git checkout ${GITHUB_SHA}"[0m
2025-06-14T19:32:45.8173180Z shell: sh -e {0}
2025-06-14T19:32:45.8173484Z env:
2025-06-14T19:32:45.8173745Z   VM_CPU: 4
2025-06-14T19:32:45.8174017Z   VM_RAM: 15G
2025-06-14T19:32:45.8174296Z ##[endgroup]
2025-06-14T19:32:47.1447809Z Cloning into '/boot/home/haikuports'...
2025-06-14T19:34:45.1801644Z Updating files:   7% (496/6941)
2025-06-14T19:34:45.3945715Z Updating files:   8% (556/6941)
2025-06-14T19:34:45.5775225Z Updating files:   9% (625/6941)
2025-06-14T19:34:45.7267413Z Updating files:  10% (695/6941)
2025-06-14T19:34:45.8772872Z Updating files:  11% (764/6941)
2025-06-14T19:34:46.0176451Z Updating files:  12% (833/6941)
2025-06-14T19:34:46.0277541Z Updating files:  13% (903/6941)
2025-06-14T19:34:46.1539348Z Updating files:  13% (906/6941)
2025-06-14T19:34:46.3991808Z Updating files:  14% (972/6941)
2025-06-14T19:34:46.5573511Z Updating files:  15% (1042/6941)
2025-06-14T19:34:46.7080626Z Updating files:  16% (1111/6941)
2025-06-14T19:34:46.8575609Z Updating files:  17% (1180/6941)
2025-06-14T19:34:46.9789067Z Updating files:  18% (1250/6941)
2025-06-14T19:34:47.0258868Z Updating files:  19% (1319/6941)
2025-06-14T19:34:47.1352704Z Updating files:  19% (1337/6941)
2025-06-14T19:34:47.6966689Z Updating files:  20% (1389/6941)
2025-06-14T19:34:47.8387940Z Updating files:  21% (1458/6941)
2025-06-14T19:34:47.9783837Z Updating files:  22% (1528/6941)
2025-06-14T19:34:48.0234279Z Updating files:  23% (1597/6941)
2025-06-14T19:34:48.1292687Z Updating files:  23% (1614/6941)
2025-06-14T19:34:48.3884427Z Updating files:  24% (1666/6941)
2025-06-14T19:34:48.6781483Z Updating files:  25% (1736/6941)
2025-06-14T19:34:48.8204780Z Updating files:  26% (1805/6941)
2025-06-14T19:34:48.9861654Z Updating files:  27% (1875/6941)
2025-06-14T19:34:49.0259876Z Updating files:  28% (1944/6941)
2025-06-14T19:34:49.1509965Z Updating files:  28% (1960/6941)
2025-06-14T19:34:49.3146798Z Updating files:  29% (2013/6941)
2025-06-14T19:34:49.5066397Z Updating files:  30% (2083/6941)
2025-06-14T19:34:49.6966013Z Updating files:  31% (2152/6941)
2025-06-14T19:34:49.9474129Z Updating files:  32% (2222/6941)
2025-06-14T19:34:50.0297361Z Updating files:  33% (2291/6941)
2025-06-14T19:34:50.1599789Z Updating files:  33% (2315/6941)
2025-06-14T19:34:50.2927269Z Updating files:  34% (2360/6941)
2025-06-14T19:34:50.4917849Z Updating files:  35% (2430/6941)
2025-06-14T19:34:50.6525074Z Updating files:  36% (2499/6941)
2025-06-14T19:34:50.7982763Z Updating files:  37% (2569/6941)
2025-06-14T19:34:50.9486937Z Updating files:  38% (2638/6941)
2025-06-14T19:34:51.0270933Z Updating files:  39% (2707/6941)
2025-06-14T19:34:51.2041628Z Updating files:  39% (2742/6941)
2025-06-14T19:34:51.3826077Z Updating files:  40% (2777/6941)
2025-06-14T19:34:51.5302908Z Updating files:  41% (2846/6941)
2025-06-14T19:34:51.9303532Z Updating files:  42% (2916/6941)
2025-06-14T19:34:52.0258494Z Updating files:  43% (2985/6941)
2025-06-14T19:34:52.0668643Z Updating files:  43% (3031/6941)
2025-06-14T19:34:52.2785571Z Updating files:  44% (3055/6941)
2025-06-14T19:34:52.5094624Z Updating files:  45% (3124/6941)
2025-06-14T19:34:52.7388006Z Updating files:  46% (3193/6941)
2025-06-14T19:34:52.8717646Z Updating files:  47% (3263/6941)
2025-06-14T19:34:53.0243000Z Updating files:  48% (3332/6941)
2025-06-14T19:34:53.2219954Z Updating files:  49% (3402/6941)
2025-06-14T19:34:53.3707895Z Updating files:  50% (3471/6941)
2025-06-14T19:34:53.5477087Z Updating files:  51% (3540/6941)
2025-06-14T19:34:53.6955306Z Updating files:  52% (3610/6941)
2025-06-14T19:34:53.8463028Z Updating files:  53% (3679/6941)
2025-06-14T19:34:54.0203728Z Updating files:  54% (3749/6941)
2025-06-14T19:34:54.0242743Z Updating files:  55% (3818/6941)
2025-06-14T19:34:54.2024010Z Updating files:  55% (3819/6941)
2025-06-14T19:34:54.3810557Z Updating files:  56% (3887/6941)
2025-06-14T19:34:54.5506957Z Updating files:  57% (3957/6941)
2025-06-14T19:34:55.1942947Z Updating files:  58% (4026/6941)
2025-06-14T19:34:55.4420385Z Updating files:  58% (4040/6941)
2025-06-14T19:34:55.6007056Z Updating files:  59% (4096/6941)
2025-06-14T19:34:55.7626875Z Updating files:  60% (4165/6941)
2025-06-14T19:34:55.9139694Z Updating files:  61% (4235/6941)
2025-06-14T19:34:56.0245484Z Updating files:  62% (4304/6941)
2025-06-14T19:34:56.0787183Z Updating files:  62% (4352/6941)
2025-06-14T19:34:56.2371366Z Updating files:  63% (4373/6941)
2025-06-14T19:34:56.3974936Z Updating files:  64% (4443/6941)
2025-06-14T19:34:56.5544573Z Updating files:  65% (4512/6941)
2025-06-14T19:34:56.7097559Z Updating files:  66% (4582/6941)
2025-06-14T19:34:56.9587283Z Updating files:  67% (4651/6941)
2025-06-14T19:34:57.0257108Z Updating files:  68% (4720/6941)
2025-06-14T19:34:57.1181283Z Updating files:  68% (4748/6941)
2025-06-14T19:34:57.3777715Z Updating files:  69% (4790/6941)
2025-06-14T19:34:57.6116069Z Updating files:  70% (4859/6941)
2025-06-14T19:34:57.8185539Z Updating files:  71% (4929/6941)
2025-06-14T19:34:57.9754098Z Updating files:  72% (4998/6941)
2025-06-14T19:34:58.0245975Z Updating files:  73% (5067/6941)
2025-06-14T19:34:58.3239451Z Updating files:  73% (5086/6941)
2025-06-14T19:34:58.5300481Z Updating files:  74% (5137/6941)
2025-06-14T19:34:58.7114168Z Updating files:  75% (5206/6941)
2025-06-14T19:34:59.0771827Z Updating files:  76% (5276/6941)
2025-06-14T19:34:59.1140380Z Updating files:  76% (5330/6941)
2025-06-14T19:34:59.2806513Z Updating files:  77% (5345/6941)
2025-06-14T19:34:59.4516210Z Updating files:  78% (5414/6941)
2025-06-14T19:34:59.6187046Z Updating files:  79% (5484/6941)
2025-06-14T19:34:59.8003088Z Updating files:  80% (5553/6941)
2025-06-14T19:34:59.9693260Z Updating files:  81% (5623/6941)
2025-06-14T19:35:00.0292087Z Updating files:  82% (5692/6941)
2025-06-14T19:35:00.1566636Z Updating files:  82% (5714/6941)
2025-06-14T19:35:00.3424382Z Updating files:  83% (5762/6941)
2025-06-14T19:35:00.5336434Z Updating files:  84% (5831/6941)
2025-06-14T19:35:00.7515662Z Updating files:  85% (5900/6941)
2025-06-14T19:35:00.9170661Z Updating files:  86% (5970/6941)
2025-06-14T19:35:01.0270701Z Updating files:  87% (6039/6941)
2025-06-14T19:35:01.1107905Z Updating files:  87% (6079/6941)
2025-06-14T19:35:01.7100417Z Updating files:  88% (6109/6941)
2025-06-14T19:35:01.9777456Z Updating files:  89% (6178/6941)
2025-06-14T19:35:02.0294971Z Updating files:  90% (6247/6941)
2025-06-14T19:35:02.2300825Z Updating files:  90% (6261/6941)
2025-06-14T19:35:02.4605944Z Updating files:  91% (6317/6941)
2025-06-14T19:35:02.6813771Z Updating files:  92% (6386/6941)
2025-06-14T19:35:02.8573762Z Updating files:  93% (6456/6941)
2025-06-14T19:35:03.0283934Z Updating files:  94% (6525/6941)
2025-06-14T19:35:03.0874760Z Updating files:  94% (6569/6941)
2025-06-14T19:35:03.2405006Z Updating files:  95% (6594/6941)
2025-06-14T19:35:03.4038855Z Updating files:  96% (6664/6941)
2025-06-14T19:35:03.6011886Z Updating files:  97% (6733/6941)
2025-06-14T19:35:03.7745067Z Updating files:  98% (6803/6941)
2025-06-14T19:35:03.9573630Z Updating files:  99% (6872/6941)
2025-06-14T19:35:03.9573999Z Updating files: 100% (6941/6941)
2025-06-14T19:35:03.9574298Z Updating files: 100% (6941/6941), done.
2025-06-14T19:35:37.1144186Z Note: switching to '63b53c782f0409298c5b9fc44661b627ea21230d'.
2025-06-14T19:35:37.1145938Z 
2025-06-14T19:35:37.1146500Z You are in 'detached HEAD' state. You can look around, make experimental
2025-06-14T19:35:37.1147338Z changes and commit them, and you can discard any commits you make in this
2025-06-14T19:35:37.1148068Z state without impacting any branches by switching back to a branch.
2025-06-14T19:35:37.1148385Z 
2025-06-14T19:35:37.1148939Z If you want to create a new branch to retain commits you create, you may
2025-06-14T19:35:37.1149419Z do so (now or later) by using -c with the switch command. Example:
2025-06-14T19:35:37.1149698Z 
2025-06-14T19:35:37.1149824Z   git switch -c <new-branch-name>
2025-06-14T19:35:37.1150008Z 
2025-06-14T19:35:37.1150101Z Or undo this operation with:
2025-06-14T19:35:37.1150569Z 
2025-06-14T19:35:37.1150692Z   git switch -
2025-06-14T19:35:37.1150888Z 
2025-06-14T19:35:37.1151140Z Turn off this advice by setting config variable advice.detachedHead to false
2025-06-14T19:35:37.1151471Z 
2025-06-14T19:35:37.1151573Z HEAD is now at 63b53c782 Fix paths again
2025-06-14T19:35:37.1435434Z ##[group]Run # Standard HaikuPorter setup in VM
2025-06-14T19:35:37.1436048Z [36;1m# Standard HaikuPorter setup in VM[0m
2025-06-14T19:35:37.1436591Z [36;1mvmshell "mkdir -p /home/config/settings"[0m
2025-06-14T19:35:37.1437474Z [36;1mvmshell "echo 'TREE_PATH="/boot/home/haikuports"' > /home/config/settings/haikuports.conf"[0m
2025-06-14T19:35:37.1438693Z [36;1mvmshell "echo 'PACKAGER=\"GitHub Actions Builder \<actions@github.com\>\"' >> /home/config/settings/haikuports.conf"[0m
2025-06-14T19:35:37.1439625Z [36;1mecho "VM's haikuports.conf:"[0m
2025-06-14T19:35:37.1440399Z [36;1mvmshell "cat /home/config/settings/haikuports.conf"[0m
2025-06-14T19:35:37.1440928Z [36;1m[0m
2025-06-14T19:35:37.1441660Z [36;1mif [ -d "/home/runner/work/haikuports/haikuports/repository" ] && [ -f "changed_recipes_list.json" ]; then[0m
2025-06-14T19:35:37.1442510Z [36;1m  [0m
2025-06-14T19:35:37.1443155Z [36;1m  echo "Creating tarball from /runner/work/haikuports/haikuports/repository ..."[0m
2025-06-14T19:35:37.1444191Z [36;1m  tar -czf output_repository.tar.gz -C "/home/runner/work/haikuports/haikuports/repository" .[0m
2025-06-14T19:35:37.1445265Z [36;1m  [0m
2025-06-14T19:35:37.1445602Z [36;1m  # Transfer the tarball into the VM[0m
2025-06-14T19:35:37.1446208Z [36;1m  echo "Transferring output_repository.tar.gz to VM / ..."[0m
2025-06-14T19:35:37.1447040Z [36;1m  cat output_repository.tar.gz | vmshell "cat > /output_repository.tar.gz"[0m
2025-06-14T19:35:37.1447680Z [36;1m  [0m
2025-06-14T19:35:37.1448074Z [36;1m  # Transfer the changed_recipes_list.json into the VM[0m
2025-06-14T19:35:37.1448752Z [36;1m  echo "Transferring changed_recipes_list.json to VM / ..."[0m
2025-06-14T19:35:37.1449584Z [36;1m  cat changed_recipes_list.json | vmshell "cat > /changed_recipes_list.json"[0m
2025-06-14T19:35:37.1450650Z [36;1m  [0m
2025-06-14T19:35:37.1451173Z [36;1m  # In the VM: Ensure target directory exists and extract the tarball there[0m
2025-06-14T19:35:37.1451879Z [36;1melse[0m
2025-06-14T19:35:37.1452410Z [36;1m  echo "Not found: /runner/work/haikuports/haikuports/repository ..."[0m
2025-06-14T19:35:37.1453041Z [36;1mfi[0m
2025-06-14T19:35:37.1453522Z shell: bash --noprofile --norc -e -o pipefail {0}
2025-06-14T19:35:37.1453984Z env:
2025-06-14T19:35:37.1454242Z   VM_CPU: 4
2025-06-14T19:35:37.1454498Z   VM_RAM: 15G
2025-06-14T19:35:37.1454779Z ##[endgroup]
2025-06-14T19:35:40.2481480Z VM's haikuports.conf:
2025-06-14T19:35:41.2708819Z TREE_PATH=/boot/home/haikuports
2025-06-14T19:35:41.2709281Z PACKAGER="GitHub Actions Builder \<actions@github.com\>"
2025-06-14T19:35:41.2725477Z Not found: /runner/work/haikuports/haikuports/repository ...
2025-06-14T19:35:41.2804833Z ##[group]Run vmshell "cd ~/haikuports && \
2025-06-14T19:35:41.2805178Z [36;1mvmshell "cd ~/haikuports && \[0m
2025-06-14T19:35:41.2805574Z [36;1m  echo 'Reading list of changed packages from /changed_recipes_list.json' && \[0m
2025-06-14T19:35:41.2806017Z [36;1m  PACKAGES_JSON=\$(cat /changed_recipes_list.json) && \[0m
2025-06-14T19:35:41.2806455Z [36;1m  echo \"Packages to build (JSON list of recipe paths): \$PACKAGES_JSON\" && \[0m
2025-06-14T19:35:41.2806801Z [36;1m  \[0m
2025-06-14T19:35:41.2806978Z [36;1m  mkdir -p packages && \[0m
2025-06-14T19:35:41.2807214Z [36;1m  mkdir -p repository && \[0m
2025-06-14T19:35:41.2807423Z [36;1m  \[0m
2025-06-14T19:35:41.2807709Z [36;1m  # Convert JSON array to a space-separated string of shell-escaped arguments[0m
2025-06-14T19:35:41.2808148Z [36;1m  RECIPE_ARGS_STRING=\$(echo \"\$PACKAGES_JSON\" | jq -r '. | @sh')[0m
2025-06-14T19:35:41.2808454Z [36;1m  \[0m
2025-06-14T19:35:41.2808812Z [36;1m  if [ -z \"\$RECIPE_ARGS_STRING\" ] || [ \"\$RECIPE_ARGS_STRING\" = \"''\" ] || [ \"\$RECIPE_ARGS_STRING\" = \"'[]'\" ]; then \[0m
2025-06-14T19:35:41.2809276Z [36;1m    echo 'No packages specified in the list to build.' ; \[0m
2025-06-14T19:35:41.2809561Z [36;1m  else \[0m
2025-06-14T19:35:41.2809837Z [36;1m    echo \"Executing haikuporter with args: \$RECIPE_ARGS_STRING\" ; \[0m
2025-06-14T19:35:41.2810713Z [36;1m    # Use eval to correctly parse the space-separated, potentially quoted arguments[0m
2025-06-14T19:35:41.2811157Z [36;1m    if eval \"haikuporter \$RECIPE_ARGS_STRING -S -j4\"; then \[0m
2025-06-14T19:35:41.2811599Z [36;1m      echo \"✓ HaikuPorter command for batch build completed successfully.\" ; \[0m
2025-06-14T19:35:41.2811960Z [36;1m    else \[0m
2025-06-14T19:35:41.2812148Z [36;1m      BUILD_FAILURE_CODE=\$? ; \[0m
2025-06-14T19:35:41.2812557Z [36;1m      echo \"✗ HaikuPorter command for batch build failed with exit code \$BUILD_FAILURE_CODE.\" ; \[0m
2025-06-14T19:35:41.2813140Z [36;1m      # Exit the vmshell script with the failure code, which will fail the GitHub Actions step[0m
2025-06-14T19:35:41.2813536Z [36;1m      exit \$BUILD_FAILURE_CODE ; \[0m
2025-06-14T19:35:41.2813764Z [36;1m    fi ; \[0m
2025-06-14T19:35:41.2813925Z [36;1m  fi ; \[0m
2025-06-14T19:35:41.2814085Z [36;1m  \[0m
2025-06-14T19:35:41.2814264Z [36;1m  echo \"Build summary (within VM):\" ; \[0m
2025-06-14T19:35:41.2814786Z [36;1m  NUM_PACKAGES=\$(echo \"\$PACKAGES_JSON\" | jq -r '. | length') ; \[0m
2025-06-14T19:35:41.2815142Z [36;1m  echo \"- Packages in batch: \$NUM_PACKAGES\" ; \[0m
2025-06-14T19:35:41.2815579Z [36;1m  if [ -z \"\$RECIPE_ARGS_STRING\" ] || [ \"\$RECIPE_ARGS_STRING\" = \"''\" ] || [ \"\$RECIPE_ARGS_STRING\" = \"'[]'\" ]; then \[0m
2025-06-14T19:35:41.2816009Z [36;1m      echo \"No packages were attempted.\" ; \[0m
2025-06-14T19:35:41.2816253Z [36;1m  else \[0m
2025-06-14T19:35:41.2816619Z [36;1m      # If the script reaches here, the haikuporter command must have succeeded (due to 'exit' on failure)[0m
2025-06-14T19:35:41.2817162Z [36;1m      echo \"Batch build attempt reported success by HaikuPorter exit code.\" ; \[0m
2025-06-14T19:35:41.2817505Z [36;1m  fi"[0m
2025-06-14T19:35:41.2817755Z shell: sh -e {0}
2025-06-14T19:35:41.2817916Z env:
2025-06-14T19:35:41.2818063Z   VM_CPU: 4
2025-06-14T19:35:41.2818206Z   VM_RAM: 15G
2025-06-14T19:35:41.2818368Z ##[endgroup]
2025-06-14T19:35:42.3593308Z Reading list of changed packages from /changed_recipes_list.json
2025-06-14T19:35:42.3939108Z cat: /changed_recipes_list.json: No such file or directory
2025-06-14T19:35:42.4038271Z No packages specified in the list to build.
2025-06-14T19:35:42.4038969Z Build summary (within VM):
2025-06-14T19:35:42.5509855Z - Packages in batch: 
2025-06-14T19:35:42.5572313Z No packages were attempted.
2025-06-14T19:35:42.5599470Z ##[group]Run mkdir -p build-artifacts
2025-06-14T19:35:42.5600013Z [36;1mmkdir -p build-artifacts[0m
2025-06-14T19:35:42.5600501Z [36;1mvmshell "cd ~/haikuports && \[0m
2025-06-14T19:35:42.5600847Z [36;1m  if [ -d packages ] && [ \"\$(ls -A packages/*.hpkg 2>/dev/null)\" ]; then[0m
2025-06-14T19:35:42.5601193Z [36;1m    echo 'Found built packages:'[0m
2025-06-14T19:35:42.5601439Z [36;1m    ls -la packages/*.hpkg || true[0m
2025-06-14T19:35:42.5601742Z [36;1m    tar -czf /built-packages.tar.gz packages/*.hpkg[0m
2025-06-14T19:35:42.5602034Z [36;1m  else[0m
2025-06-14T19:35:42.5602222Z [36;1m    echo 'No packages were built'[0m
2025-06-14T19:35:42.5602515Z [36;1m    tar -czf /built-packages.tar.gz -T /null [0m
2025-06-14T19:35:42.5602777Z [36;1m  fi[0m
2025-06-14T19:35:42.5602945Z [36;1m  if [ -d work ]; then[0m
2025-06-14T19:35:42.5603387Z [36;1m    find work -name '*.log' -type f -print0 | head -z -n 20 | xargs -0 tar -czf /build-logs.tar.gz 2>/dev/null || \[0m
2025-06-14T19:35:42.5603864Z [36;1m    tar -czf /build-logs.tar.gz -T /null [0m
2025-06-14T19:35:42.5604124Z [36;1m  else[0m
2025-06-14T19:35:42.5604333Z [36;1m    tar -czf /build-logs.tar.gz -T /null[0m
2025-06-14T19:35:42.5604583Z [36;1m  fi"[0m
2025-06-14T19:35:42.5604897Z [36;1mvmshell cat /built-packages.tar.gz > build-artifacts/built-packages.tar.gz[0m
2025-06-14T19:35:42.5605386Z [36;1mvmshell cat /build-logs.tar.gz > build-artifacts/build-logs.tar.gz[0m
2025-06-14T19:35:42.5605822Z shell: sh -e {0}
2025-06-14T19:35:42.5605982Z env:
2025-06-14T19:35:42.5606129Z   VM_CPU: 4
2025-06-14T19:35:42.5606273Z   VM_RAM: 15G
2025-06-14T19:35:42.5606430Z ##[endgroup]
2025-06-14T19:35:43.9173585Z No packages were built
2025-06-14T19:35:46.3243591Z ##[group]Run actions/upload-artifact@v4
2025-06-14T19:35:46.3243858Z with:
2025-06-14T19:35:46.3244031Z   name: haikuports-build-84
2025-06-14T19:35:46.3244242Z   path: build-artifacts/
2025-06-14T19:35:46.3244448Z   retention-days: 30
2025-06-14T19:35:46.3244631Z   if-no-files-found: warn
2025-06-14T19:35:46.3244829Z   compression-level: 6
2025-06-14T19:35:46.3245014Z   overwrite: false
2025-06-14T19:35:46.3245194Z   include-hidden-files: false
2025-06-14T19:35:46.3245396Z env:
2025-06-14T19:35:46.3245536Z   VM_CPU: 4
2025-06-14T19:35:46.3245688Z   VM_RAM: 15G
2025-06-14T19:35:46.3245840Z ##[endgroup]
2025-06-14T19:35:46.3248167Z ##[command]/usr/bin/docker exec  11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1 sh -c "cat /*release | grep ^ID"
2025-06-14T19:35:46.6603369Z With the provided path, there will be 2 files uploaded
2025-06-14T19:35:46.6610487Z Artifact name is valid!
2025-06-14T19:35:46.6611371Z Root directory input is valid!
2025-06-14T19:35:46.8031704Z Beginning upload of artifact content to blob storage
2025-06-14T19:35:46.9461895Z Uploaded bytes 358
2025-06-14T19:35:46.9862681Z Finished uploading artifact content to blob storage!
2025-06-14T19:35:46.9866526Z SHA256 digest of uploaded artifact zip is d4f7d74160e0477baf3fec47756279127dda6e0ad46ba1e70bba317a5a139da7
2025-06-14T19:35:46.9868911Z Finalizing artifact upload
2025-06-14T19:35:47.0754795Z Artifact haikuports-build-84.zip successfully finalized. Artifact ID 3329029118
2025-06-14T19:35:47.0756873Z Artifact haikuports-build-84 has been successfully uploaded! Final size is 358 bytes. Artifact ID is 3329029118
2025-06-14T19:35:47.0763930Z Artifact download URL: https://github.com/icarito/haikuports/actions/runs/15655388384/artifacts/3329029118
2025-06-14T19:35:47.0897078Z ##[group]Run echo "## Build Summary" >> $GITHUB_STEP_SUMMARY
2025-06-14T19:35:47.0897783Z [36;1mecho "## Build Summary" >> $GITHUB_STEP_SUMMARY[0m
2025-06-14T19:35:47.0898318Z [36;1mecho "" >> $GITHUB_STEP_SUMMARY[0m
2025-06-14T19:35:47.0898996Z [36;1mecho "**Workflow:** Build HaikuPorts packages" >> $GITHUB_STEP_SUMMARY[0m
2025-06-14T19:35:47.0899742Z [36;1mecho "**Run Number:** 84" >> $GITHUB_STEP_SUMMARY[0m
2025-06-14T19:35:47.0900643Z [36;1mecho "**Trigger:** push" >> $GITHUB_STEP_SUMMARY[0m
2025-06-14T19:35:47.0901192Z [36;1mecho "" >> $GITHUB_STEP_SUMMARY[0m
2025-06-14T19:35:47.0901651Z [36;1m[0m
2025-06-14T19:35:47.0901972Z [36;1mif [ "true" = "true" ]; then[0m
2025-06-14T19:35:47.0902474Z [36;1m  PACKAGES_JSON_STRING='["gui-libs/gtk4"]'[0m
2025-06-14T19:35:47.0903308Z [36;1m  DISPLAY_PACKAGES=$(echo "$PACKAGES_JSON_STRING" | jq -r '. | join(", ")' || echo "$PACKAGES_JSON_STRING")[0m
2025-06-14T19:35:47.0904433Z [36;1m  echo "**Packages processed (recipe paths):** $DISPLAY_PACKAGES" >> $GITHUB_STEP_SUMMARY[0m
2025-06-14T19:35:47.0905169Z [36;1m  echo "" >> $GITHUB_STEP_SUMMARY[0m
2025-06-14T19:35:47.0906002Z [36;1m  echo "**Artifacts:** Check the uploaded build artifacts for built packages and logs." >> $GITHUB_STEP_SUMMARY[0m
2025-06-14T19:35:47.0906852Z [36;1melse[0m
2025-06-14T19:35:47.0907613Z [36;1m  echo "**Result:** No recipes needed to be built (based on change detection in prepare-build job)." >> $GITHUB_STEP_SUMMARY[0m
2025-06-14T19:35:47.0908435Z [36;1mfi[0m
2025-06-14T19:35:47.0908854Z shell: sh -e {0}
2025-06-14T19:35:47.0909163Z env:
2025-06-14T19:35:47.0909420Z   VM_CPU: 4
2025-06-14T19:35:47.0909698Z   VM_RAM: 15G
2025-06-14T19:35:47.0909988Z ##[endgroup]
2025-06-14T19:35:47.1799330Z Post job cleanup.
2025-06-14T19:35:47.1802513Z ##[command]/usr/bin/docker exec  11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1 sh -c "cat /*release | grep ^ID"
2025-06-14T19:35:47.4217735Z [command]/usr/bin/tar --posix -cf cache.tgz --exclude cache.tgz -P -C /haikuports/haikuports --files-from manifest.txt -z
2025-06-14T19:35:50.5548906Z Sent 34724000 of 34724000 (100.0%), 33.1 MBs/sec
2025-06-14T19:35:50.6881451Z Cache saved with key: Linux-haiku-deps-v3-8ccc15b061e242ccc0e6f5e4bc1d2ed2f99239d2
2025-06-14T19:35:50.7027796Z Post job cleanup.
2025-06-14T19:35:50.7031984Z ##[command]/usr/bin/docker exec  11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1 sh -c "cat /*release | grep ^ID"
2025-06-14T19:35:50.9057138Z Stop and remove container: 7c3f467b05dd44f9870fcf4203ac21fc_dockeriohectormqemuhaikulatest_e9c54c
2025-06-14T19:35:50.9061748Z ##[command]/usr/bin/docker rm --force 11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1
2025-06-14T19:35:51.3003081Z 11190ed56dbe72d03e4328f2cc20bc7e8f6a703c0c5b6d8305b21230e76d0cd1
2025-06-14T19:35:51.3034437Z Remove container network: github_network_450eee868c4a45b0b3f1eb2abe5c2179
2025-06-14T19:35:51.3038571Z ##[command]/usr/bin/docker network rm github_network_450eee868c4a45b0b3f1eb2abe5c2179
2025-06-14T19:35:51.4310299Z github_network_450eee868c4a45b0b3f1eb2abe5c2179
2025-06-14T19:35:51.4367275Z Cleaning up orphan processes