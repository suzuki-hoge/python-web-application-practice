##Djangoプロジェクトを作成して組み込みサーバを立ててみましょう
```Bash
> django-admin.py startproject step01
> cd step01
> python manage.py runserver
```
[http://localhost:18000/](http://localhost:18000/)
##Djangoアプリケーションを作成してモデル定義をしてみましょう
```Bash
> python manage.py startapp todo
```
*todo/models.py*
```Python
class Story(models.Model):
    body = models.CharField(max_length = 32)
    end = models.DateTimeField()
    status = models.IntegerField()

class Task(models.Model):
    body = models.CharField(max_length = 32)
    end = models.DateTimeField()
    status = models.IntegerField()
    storyId = models.ForeignKey(Story)
```
*step01/settings.py*
```Python
INSTALLED_APPS = (
~~
'todo',
)
```
```Bash
> python manage.py syncdb
```
**アカウント作成を求められるので、yesを選択して適当にアカウントを作成します**  
**作成したアカウントは管理画面にログインするのに使用します**
##管理画面でストーリを編集できるようにしてみましょう
*todo/admin.py*
```Python
from todo.models import *
admin.site.register(Story)
admin.site.register(Task)
```
*todo/models.py*
```Python
def __unicode__(self):
    return '%s : %s' % (self.id, self.body)
```
[http://localhost:18000/admin](http://localhost:18000/admin)
