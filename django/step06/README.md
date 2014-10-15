# Step06

この章では Apache を使って Django で作った Web アプリを動作させる。
- ゲスト OS で Apache を動かす（復習）。
- ゲスト OS で Apache + mod_wsgi + Django を動かす。
- 公開用サーバを設定する。
- 公開用サーバにデプロイする。

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
[vagrant]$ sudo yum install http-devel -y
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
## 公開用サーバにデプロイする。
