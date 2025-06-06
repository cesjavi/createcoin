#!/bin/bash
set -euo pipefail

# Install required dependencies before using them
sudo apt-get update
sudo apt-get install -y autoconf make libtool build-essential libboost-all-dev rename

# Clone bitcoin repository and rename
git clone https://github.com/bitcoin/bitcoin.git
mv bitcoin tugo
cd tugo

# Replace occurrences of "bitcoin" with "tugo"
find ./ -execdir rename 's/bitcoin/tugo/' '{}' \+
find ./ -type f -exec sed -i 's/bitcoin/tugo/g' {} \;
find ./ -type f -exec sed -i 's/BITCOIN/TUGO/g' {} \;
find ./ -type f -exec sed -i 's/Bitcoin/Tugo/g' {} \;

# Build the project
./autogen.sh
./configure
make -j "$(($(nproc)+1))"
