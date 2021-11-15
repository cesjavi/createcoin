git clone https://github.com/bitcoin/bitcoin.git
mv bitcoin tugo
cd tugo
find ./ -execdir rename 's/bitcoin/tugo/' '{}' \+
find ./ -type f -exec sed -i 's/bitcoin/tugo/g' {} \;
find ./ -type f -exec sed -i 's/BITCOIN/TUGO/g' {} \;
find ./ -type f -exec sed -i 's/Bitcoin/Tugo/g' {} \;
sudo apt-get install autoconf make libtool build-essential libboost-all-dev rename
./autogen.sh
./configure
make -j "$(($(nproc)+1))"