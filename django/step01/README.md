##Djangoアプリケーションを作成してみましょう
```Bash
> django-admin.py startproject step01
> cd step01
> python manage.py startapp todo
> python manage.py syncdb
> python manage.py runserver 0.0.0.0:8000
```
**アカウント作成を求められるので、yesを選択して適当にアカウントを作成します**  
**作成したアカウントは管理画面にログインするのに使用します**  
**It worked!が表示されれば成功です**  
[http://localhost:18000/](http://localhost:18000/)  
**ファイル構成は以下のようになります**  
```Bash
foo/bar/django/step01
> tree .
.
├── db.sqlite3
├── manage.py
├── step01
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── todo
    ├── __init__.py
    ├── admin.py
    ├── models.py
    ├── tests.py
    └── views.py
```

##モデル定義をしてみましょう
*todo/models.py*
```Python
class Story(models.Model):
    body = models.CharField(max_length = 32)
    end = models.DateTimeField()
    status = models.IntegerField()
    def __unicode__(self):
        return '%s : %s' % (self.id, self.body)

class Task(models.Model):
    body = models.CharField(max_length = 32)
    end = models.DateTimeField()
    status = models.IntegerField()
    story = models.ForeignKey(Story)
    def __unicode__(self):
        return '%s : %s' % (self.id, self.body)
```
*step01/settings.py*
```Python
INSTALLED_APPS = (
~~
'todo',
)
```
```Bash
> python manage.py makemigrations
> python manage.py migrate
```
**migrateはモデル定義を基にcreate table文を発行するコマンドです**  
**ここで発行されるSQLは使用するDBによって異なります（デフォルト設定はSqlite3です）**
##管理画面でストーリを編集できるようにしてみましょう
*todo/admin.py*
```Python
from todo.models import *
admin.site.register(Story)
admin.site.register(Task)
```
```Bash
> python manage.py runserver 0.0.0.0:8000
```
[http://localhost:18000/admin](http://localhost:18000/admin)
