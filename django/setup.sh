#!/bin/sh

yum update -y
yum groupinstall "Development tools" -y
yum install wget zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel -y

cd /usr/local/src
wget -q https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz
tar xvfz Python-2.7.8.tgz
cd Python-2.7.8
./configure --with-threads --enable-shared
make
make altinstall
echo '/usr/local/lib' > /etc/ld.so.conf.d/python2.7.conf
ldconfig
ln -s /usr/local/bin/python2.7 /usr/local/bin/python

cd /tmp
wget -q http://peak.telecommunity.com/dist/ez_setup.py
/usr/local/bin/python ez_setup.py
/usr/local/bin/easy_install pip

cd /tmp
wget -q https://github.com/django/django/archive/master.zip
unzip master.zip
cd /tmp/django-master
/usr/local/bin/python setup.py install

yum install httpd httpd-devel -y
/usr/local/bin/pip install mod_wsgi

#if [ ! -f /etc/httpd/conf/httpd.conf.org ]; then
#  cp /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.org
#fi
#cp /vagrant/httpd.conf /etc/httpd/conf/
#cp /vagrant/wsgi.conf /etc/httpd/conf.d/
#chkconfig httpd on
#service httpd restart