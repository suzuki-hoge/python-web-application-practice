# Step06

この章では Apache を使って Django で作った Web アプリを動作させる。

まず、開発環境のゲスト OS 上で動作させた後で、公開用サーバを設定しデプロイする。

ゲスト OS と公開用サーバとでは、Web アプリのコードが配備されているディレクトリが違うため、異なった設定が必要となる(ゲストOS /vagrant/step06, 公開用サーバ /var/www/step06)。

- ゲスト OS で Django を動かす（復習）。
- ゲスト OS で Apache を動かす（復習）。
- ゲスト OS で Apache + mod_wsgi + Django を動かす。
- 公開用サーバを設定する。
- 公開用サーバにデプロイする。

## ゲスト OS で Django を動かす（復習）。

ゲスト OS で Django を動かすまでの処理は setup.sh に記載してある。Vagrantfile の provision shell に指定してあるので、vagrant up --provision としたときに sudo で実行されている。

Vagrantfile:

```ruby
  config.vm.provision :shell, :path => "setup.sh"
```

公開用サーバの設定にも必要になるので、ここで内容を確認しておく。

setup.sh:
```sh
#!/bin/sh

# yum を最新にしておく。-y は yes を自動入力するコマンド
yum update -y
# 開発をするために必要となるツール一式をインストールする
yum groupinstall "Development tools" -y
# python のコンパイルなどに必要となるツール一式をインストールする
yum install wget zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel -y

# python のインストール
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

# pip のインストール。python のパッケージ管理をする。
cd /tmp
wget -q http://peak.telecommunity.com/dist/ez_setup.py
/usr/local/bin/python ez_setup.py
/usr/local/bin/easy_install pip

# django の最新版をインストールする。
cd /tmp
wget -q https://github.com/django/django/archive/master.zip
unzip master.zip
cd /tmp/django-master
/usr/local/bin/python setup.py install
```

## ゲスト OS で Apache を動かす（復習）。

ゲスト OS の 80 番ポートで Apache (httpd) を動かす。
ホスト OS の 8080 番ポートへのアクセスを、ゲスト OS の 80 番ポートに転送するため、Vagrantfile を修正する。

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos65"
  config.vm.box_url = "https://github.com/2creatives/vagrant-centos/releases/download/v6.5.3/centos65-x86_64-20140116.box"
  config.vm.synced_folder ".", "/vagrant", :mount_options => ["dmode=777", "fmode=777"]
  config.vm.network :forwarded_port, guest: 8000, host: 18000
  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.provision :shell, :path => "setup.sh"
end
```

ゲスト OS への port forwarding を変更するため、vagrant reload する、
のが正しいのだが、前回までの設定ミスがあったので、一度、破棄して provision する。

```sh
$ vagrant destroy
$ vagrant up --provision
```

ゲスト OS に httpd をインストールする。

```sh
$ vagrant ssh
[vagrant]$ sudo yum install httpd
Is this ok [y/N]: y

[vagrant]$ rpm -aq | grep httpd

[vagrant]$ sudo service httpd status
httpd is stopped
```

ゲスト OS にコンテンツを作り、httpd 起動後にアクセスできることを確認する。

```sh
[vagrant]$ sudo vi /var/www/html/index.html
<h1>Hello, world!</h1>
[vagrant]$ sudo service httpd restart
[vagrant]$ sudo service httpd status
httpd (pid  3959) is running...
[vagrant]$ curl http://localhost/
<h1>Hello, world</h1>
```

Webブラウザーで[http://localhost:8080/](http://localhost:8080/)にアクセスする。

ゲスト OS を再起動しても、httpd を立ち上げるように設定しておく。

```sh
[vagrant]$ sudo chkconfig httpd on
```

## ゲスト OS で Apache + mod_wsgi + Django を動かす。

### 背景
- Apache は様々なモジュールで機能拡張ができる。モジュールは mod_から始まる名前がついている。
- mod_wsgi は Python で作った Web アプリを Apache で動かすためのモジュール。正しくは、[WSGI](http://wsgi.readthedocs.org/en/latest/what.html)(Web Server Gateway Interface) というAPIに準拠して作られたWebアプリ。
- WSGI が生まれた背景については、[WSGI / Rack / PSGI てなんぞ - SlideShare](http://www.slideshare.net/katsuji/wsgi-rack-psgi)を参照。

### 具体的な手順

- [Apache と mod_wsgi 環境で Django を使う方法](http://docs.djangoproject.jp/en/latest/howto/deployment/wsgi/modwsgi.html)を学ぶ。
- ただし、インストールは [GrahamDumpleton/mod_wsgi](https://github.com/GrahamDumpleton/mod_wsgi) にある通り、pip を使うのが楽。事前に yum で http-devel をインストールしておく。
              
```sh
[vagrant]$ sudo yum install httpd-devel -y
[vagrant]$ sudo /usr/local/bin/pip install mod_wsgi
```

- [Apache と mod_wsgi 環境で Django を使う方法](http://docs.djangoproject.jp/en/latest/howto/deployment/wsgi/modwsgi.html)にあるように、モジュールを設定する (mod_wsgi.so の参照, httpd.conf の書き換え)。
- 忘れてはいけないのは、WSGIPythonPath で site-packages へのパスを入れること, /static/ の Alias を

```sh
[vagrant]$ sudo vi /etc/httpd/conf.d/wsgi.conf
# wsgi_module を /usr/local/lib/python2.7/site-packages/mod_wsgi/server/mod_wsgi-py27.so から Apache にインストールする
LoadModule wsgi_module /usr/local/lib/python2.7/site-packages/mod_wsgi/server/mod_wsgi-py27.so

[vagrant]$ sudo vi /etc/httpd/conf/httpd.conf
（末尾に以下を追記する）
# ルートURL / へのアクセスを、/vagrant/step06/step06/wsgi.py で処理する
WSGIScriptAlias / /vagrant/step06/step06/wsgi.py
# Python Pathは、/vagrant/step06 と /usr/local/lib/python2.7/site-packages を参照する。
WSGIPythonPath /vagrant/step06:/usr/local/lib/python2.7/site-packages
# wsgi.py へのアクセスは制限を外す
<Directory /vagrant/step06>
  <Files wsgi.py>
    Order deny,allow
    Allow from all
  </Files>
</Directory>
# URL /static/ へのアクセスは、/vagrant/step06/todo/static/ 以下のファイルを参照する。
Alias /static/ /vagrant/step06/todo/static/
# /vagrant/step06/todo/static/ へのアクセスは制限を外す
<Directory /vagrant/step06/todo/static>
  Order deny,allow
  Allow from all
</Directory>
```

この作業は vi を使って間違えやすいので、http.conf のバックアップを取った上で、予め準備したファイルを使うことにする。
```sh
[vagrant]$ sudo cp /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.org
[vagrant]$ sudo cp /vagrant/httpd.conf /etc/httpd/conf/
[vagrant]$ sudo cp /vagrant/wsgi.conf /etc/httpd/conf.d/
```

設定の変更を反映させるために、httpd を再起動する。

```sh
[vagrant]$ sudo service httpd restart
```

Web ブラウザーから [http://localhost:8080/story](http://localhost:8080/story) にアクセスして、Web アプリが使えることを確認する。

## 公開用サーバを設定する。

演習1: ssh でログインするので、鍵を作ってください。秘密鍵は厳重に管理してください。公開鍵と、公開用サーバで使いたいアカウント名(英字)を教えてください。

演習2: setup.sh などを参考に、公開用サーバの設定をしてください。ただし iptables は先に設定しておきます。

確認すること
- ssh でログインできた。
- python 2.7.8 がインストールできた。
- Django 1.8 がインストールできた。
- Apache 2.2.15 がインストールできた。
- wsgi.conf を配備できた。
- (Web アプリの場所が正しく設定された) httpd.conf を配備できた。

```sh
[サーバ]$ python --version
Python 2.7.8
[サーバ]$ python
>>> import django
>>> django.VERSION
(1, 8, 0, 'alpha', 0)
>>> exit()
[サーバ]$ httpd -v
Server version: Apache/2.2.15 (Unix)
Server built:   Jul 23 2014 14:17:29
```

ローカルで~/.ssh/config を設定しておくと便利。

```sh
$ vi ~/.ssh/config
Host <サーバの名前>
 HostName <サーバのIPアドレス>
 User <アカウント名>
$ ssh <サーバの名前>
```
 
## 公開用サーバにデプロイする。

### /var/www に書き込めるようにする。

最初は、/var/www はオーナーが root, グループが root になっている。

```sh
[サーバ]$ ls -ld /var/www
drwxr-xr-x 6 root root 4096 2014-10-15 10:25 /var/www

```

httpd は apache アカウントで動いている。

```sh
[サーバ]$ ps -ef | grep httpd
[サーバ]$ ps -ef | grep httpd
root     19634     1  0 09:25 ?        00:00:00 /usr/sbin/httpd
apache   19636 19634  0 09:25 ?        00:00:00 /usr/sbin/httpd
apache   19637 19634  0 09:25 ?        00:00:00 /usr/sbin/httpd
apache   19638 19634  0 09:25 ?        00:00:00 /usr/sbin/httpd
apache   19639 19634  0 09:25 ?        00:00:00 /usr/sbin/httpd
apache   19640 19634  0 09:25 ?        00:00:00 /usr/sbin/httpd
apache   19641 19634  0 09:25 ?        00:00:00 /usr/sbin/httpd
apache   19642 19634  0 09:25 ?        00:00:00 /usr/sbin/httpd
apache   19643 19634  0 09:25 ?        00:00:00 /usr/sbin/httpd
<自分のアカウント> 19709 19690  0 10:57 pts/1    00:00:00 grep httpd
```

/var/www のオーナー:グループを、apache:apache に変更する。

```sh
[サーバ]$ sudo chown -R apache:apache /var/www
[サーバ]$ ls -ld /var/www
drwxr-xr-x 7 apache apache 4096 Oct 16 09:21 /var/www
```

自分を apache グループに追加して、/var/www に書き込めるようにする。

```sh
[サーバ]$ sudo usermod -G apache <自分のアカウント>
cat /etc/group | grep apache
apache:x:48:<自分のアカウント>

[サーバ]$ sudo chmod -R g+w /var/www
[サーバ]$ ls -ld /var/www
drwxrwxr-x 7 apache apache 4096 Oct 16 09:21 /var/www
```

### ローカルからサーバにデプロイする

rsync を使って、ローカルの pyweb/django/step06 を公開用サーバの /var/www/step06 としてコピーする。事故防止のため、いきなり実行せずに、--dry-run してからコピーする。

- -n --dry-run コピーを実行せずに処理内容を表示
- -v --verbose 詳細なメッセージを表示
- -r --recursive ディレクトリを再帰的にコピーする
- -u --update コピー先がコピー元より古い場合にコピーする
- --exclude=PATTERN PATTERN にマッチしたファイルはコピーしない

```sh
$ pwd
/Users/takatama/python/pyweb/django
$ rsync -nvru --exclude="*.sqlite3" --exclude="*.pyc" --exclude="*.md" step06 <IPアドレス>:/var/www
building file list ... done
step06/
step06/manage.py
step06/images/
step06/images/edit.png
step06/images/index.png
step06/images/last.png
step06/images/plus.png
step06/images/trash.png
step06/step06/
step06/step06/__init__.py
step06/step06/settings.py
step06/step06/urls.py
step06/step06/wsgi.py
step06/template/
step06/template/base.html
step06/template/story/
step06/template/story/form.html
step06/template/story/index.html
step06/template/task/
step06/template/task/form.html
step06/todo/
step06/todo/__init__.py
step06/todo/admin.py
step06/todo/models.py
step06/todo/tests.py
step06/todo/views.py
step06/todo/static/
step06/todo/static/index.html
step06/todo/static/css/
step06/todo/static/css/bootstrap-theme.css
step06/todo/static/css/bootstrap-theme.css.map
step06/todo/static/css/bootstrap-theme.min.css
step06/todo/static/css/bootstrap.css
step06/todo/static/css/bootstrap.css.map
step06/todo/static/css/bootstrap.min.css
step06/todo/static/fonts/
step06/todo/static/fonts/glyphicons-halflings-regular.eot
step06/todo/static/fonts/glyphicons-halflings-regular.svg
step06/todo/static/fonts/glyphicons-halflings-regular.ttf
step06/todo/static/fonts/glyphicons-halflings-regular.woff
step06/todo/static/js/
step06/todo/static/js/bootstrap.js
step06/todo/static/js/bootstrap.min.js

sent 1123 bytes  received 278 bytes  2802.00 bytes/sec
total size is 988692  speedup is 705.70
(期待通りか確認する)

$ rsync -ru --exclude="*.sqlite3" --exclude="*.pyc" --exclude="*.md" step06 <IPアドレス>:/var/www
```
