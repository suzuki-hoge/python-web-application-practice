export http_proxy=http://133.205.242.72:8080
export https_proxy=http://133.205.242.72:8080
echo 'http_proxy=http://133.205.242.72:8080' >> /etc/wgetrc
echo 'https_proxy=http://133.205.242.72:8080' >> /etc/wgetrc

yum update -y
yum groupinstall "Development tools" -y
yum install wget zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel -y

cd /home/vagrant
wget -q https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz
tar xvfz Python-2.7.8.tgz
cd Python-2.7.8
./configure
make
make altinstall
ln -s /usr/local/bin/python2.7 /usr/local/bin/python
rm -rf /home/vagrant/Python-2.7.8*

cd /tmp
wget -q http://peak.telecommunity.com/dist/ez_setup.py
/usr/local/bin/python ez_setup.py
/usr/local/bin/easy_install pip

cd /tmp
wget https://github.com/django/django/archive/master.zip
unzip master.zip
cd /tmp/django-master
/usr/local/bin/python setup.py install
