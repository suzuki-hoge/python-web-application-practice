##step01
djangoアプリを作成して管理画面を操作してみましょう
##step02
ストーリのCRUDをできるようにしてみましょう
##step03
タスクのCRUDをできるようにしてみましょう
##step04
見た目や挙動を整えてみましょう
  
###djangoセットアップ
・zipファイルの[ダウンロード](https://github.com/django/django/zipball/master)  
・Vagrantfileがあるディレクトリに*django.zip*という名前で保存する  
・Vagrantfileがあるディレクトリでvagrant up --provisionを実行する
  
###djangoプロジェクトのサーバの起動方法
python manage.py runserver 0.0.0.0:8000
  
###djangoプロジェクトのデータベース作成方法
python manage.py syncdb
  
###step数の違う新しいディレクトリを作る方法
・step0xのディレクトリをstep0yとしてコピーする  
・step0yが内包するstep0xディレクトリをリネームする  
・*step0y/step0y/settings.py*内のstep0xをstep0yに置換する  
・*step0y/manage.py*内のstep0xをstep0yに置換する  
  
※上記手順が必要なのは研修のためにstep数をわけるためだけです　通常は行いません
