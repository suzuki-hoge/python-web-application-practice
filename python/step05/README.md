##ストーリ関連のファイルをリネームして、タスク関連のファイルを作成しましょう
```Bash
> mv form.py storyform.py
> mv formsubmit.py storyformsubmit.py
> mv deletesubmit.py storydeletesubmit.py
> cp storyform.py taskform.py
> cp storyformsubmit.py taskformsubmit.py
> cp storydeletesubmit.py taskdeletesubmit.py
```
**step04の様に正しく遷移するためには、ソースコードの修正も必要です**
##タスクのデータベースを作成して初期データを投入してみましょう
```Bash
> sqlite3 todo.db
sqlite> create table task(id integer primary key autoincrement, body varchar(32), end datetime, status int, storyid integer);
sqlite> insert into task(body, end, status, storyid) values('sample', '2014-09-30 17:15:00', 1, 1);
```
**ストーリとタスクは一対多の関係になっています**
##ストーリごとにタスクをselectして、画面に出力してみましょう
*cgi-bin/list.py*
```Python
tasks = db.execute('select * from task where storyid = %s' % storyId)
~~
print '%s%s : %s (%s) - %s' % ('&nbsp;' * 8, taskId, taskBody, taskEnd, taskStatus)
```
##ストーリごとのタスクを追加してみましょう
[画面イメージ](https://github.com/tenshiPure/pyweb/blob/master/python/step05/images/list.png)  
*cgi-bin/list.py*
```Python
print "%s<a href='taskform.py?storyid=%s'>task-add</a>" % ('&nbsp;' * 8, storyId)
```
*cgi-bin/taskform.py*
```Python
print "<form method='post' action='taskformsubmit.py'>"
print "<p><input type=hidden name=storyid value='%s'></p>" % storyId
print "<p><input type=hidden name=taskid value='%s'></p>" % taskId
print "<p><input type='submit' value='send'></p>"
print "</form>"
```
*cgi-bin/taskformsubmit.py*
```Python
sql = "insert into task(body, end, status, storyid) values('%s', '%s', '%s', '%s')" % (body, end, status, storyId)
```
##ストーリごとのタスクを編集してみましょう
*cgi-bin/list.py*
```Python
print "<a href='taskform.py?storyid=%s&taskid=%s'>update</a>" % (storyId, taskId)
```
*cgi-bin/taskform.py*
```Python
rows = db.execute('select * from task where id = %s' % taskId)
```
*cgi-bin/taskformsubmit.py*
```Python
sql = "update task set body = '%s', end = '%s', status = '%s', storyid = '%s' where id = %s" % (body, end, status, storyId, taskId)
```
##ストーリごとのタスクを削除してみましょう
*cgi-bin/list.py*
```Python
print "<a href='taskdeletesubmit.py?id=%s'>delete</a>" % taskId
```
*cgi-bin/taskformsubmit.py*
```Python
sql = "delete from task where id = %s" % id
```
