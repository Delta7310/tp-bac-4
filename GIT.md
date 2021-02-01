# Git
## Pre-requis
```shell
 sudo apt install -y build-essential dh-autoreconf libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev
```
## install the latest version 
```shell
wget https://github.com/git/git/archive/v2.30.0.tar.gz
tar -zxvf v2.30.0.tar.gz
cd git-2.30.0
make configure
./configure
make -j`nproc`
make test
sudo make install

```
