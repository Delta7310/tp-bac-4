# tp-bac-4

## Compiler la derniere version de Python
```shell
sudo apt-get update
wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
tar -zxvf Python-3.9.1.tgz 
cd Python-3.9.1
sudo apt-get -y install build-essential
sudo apt-get -y install libreadline-dev
sudo apt-get -y install libsqlite3-dev
sudo apt-get -y install libssl-dev libffi-dev libgdm-dev
sudo apt-get -y install zlib1g-dev  lzma-dev libbz2-dev
sudo apt-get -y install uuid-dev
gcc --version
./configure --enable-optimizations 
# Profile guided optimization (PGO) et Link Time Optimization (LTO).
# significant speed boost 10%-20%. 
make -j`nproc`
sudo make install
```
## Verifier les parametres techniques de la version compilee
```
python3 -c "import sysconfig;print('{}'.format('\n'.join(['{} = {}'.format(v, sysconfig.get_config_var(v)) for v in sorted(sysconfig.get_config_vars(), key=lambda s: s.lower())])))" > /tmp/python3.conf
```

Voir dans le fichier genere la ligne 29 , pour verifier l'application des optimisations du compilateur

## Mise en place du virtualenv sous Ubuntu
```shell
cd tp-bac-4
python3 -m venv venv
source venv/bin/activate
```
## Installation des packages de test et de verification de code
```shell
pip3 install pytest flake8 pylint
```

## Ecriture d'un premier programme de type hello-world





