##画面に一覧を表示してみましょう
*cgi-bin/list.py*
```Python
rows = db.execute('select * from story')
for row in rows:
    print '<p>%s</p>' % str(row)
```
[http://localhost:8000/cgi-bin/list.py](http://localhost:8000/cgi-bin/list.py)
##画面に詳細を表示してみましょう
*cgi-bin/list.py*
```Python
id = form.getvalue('id', '')
rows = db.execute('select * from story where id = %s' % id)
```
[http://localhost:8000/cgi-bin/list.py?id=1](http://localhost:8000/cgi-bin/list.py?id=1)
##追加する画面を作ってみましょう
*cgi-bin/form.py*
```Python
print "<form method='post' action='formsubmit.py'>"
print "<p><input type=hidden name=id value=''></p>"
print "<p>body : <input type=text name=body value=''></p>"
print "<p>end : <input type=text name=end value=''></p>"
print "<p>status : <input type=text name=status value=''></p>"
print "<p><input type='submit' value='send'></p>"
print "</form>"
```
**id指定がないので空の入力欄を表示するだけでOKです**  
**sendボタンを押すとlocalhost:8000/cgi-bin/formsubmit.pyに遷移すれば成功です(404になります）**
[http://localhost:8000/cgi-bin/form.py](http://localhost:8000/cgi-bin/form.py)
##追加の保存処理を作ってみましょう
*cgi-bin/formsubmit.py*
```Python
import os
if os.environ['REQUEST_METHOD'] == "POST":
~~
sql = "insert into story(body, end, status) values('%s', '%s', '%s')" % (body, end, status)
cursor = db.cursor()
cursor.execute(sql)
db.commit()
~~
print "Content-type: text/html\n"
print "<meta http-equiv='refresh' content='0;URL=http://localhost:8000/cgi-bin/list.py'>"
```
**sendボタンを押してlocalhost:8000/cgi-bin/list.pyに戻ってくれば成功です**
[http://localhost:8000/cgi-bin/form.py](http://localhost:8000/cgi-bin/form.py)
##編集する画面を作ってみましょう
*cgi-bin/form.py*
```Python
print "<form method='post' action='formsubmit.py'>"
print "<p><input type=hidden name=id value='%s'></p>" % id
print "<p>body : <input type=text name=body value='%s'></p>" % body
print "<p>end : <input type=text name=end value='%s'></p>" % end
print "<p>status : <input type=text name=status value='%s'></p>" % status
print "<p><input type='submit' value='send'></p>"
print "</form>"
```
**id指定がある場合は、指定idでselectをして初期値として設定しましょう**  
[http://localhost:8000/cgi-bin/form.py?id=1](http://localhost:8000/cgi-bin/form.py?id=1)
##編集の保存処理を作ってみましょう
*cgi-bin/formsubmit.py*
```Python
sql = "update story set body = '%s', end = '%s', status = '%s' where id = %s" % (body, end, status, id)
cursor = db.cursor()
cursor.execute(sql)
```
**内容や日付を入力しないでsendボタンを押すとどうなるか確認しましょう**  
[http://localhost:8000/cgi-bin/form.py?id=1](http://localhost:8000/cgi-bin/form.py?id=1)
##削除処理を作ってみましょう
*cgi-bin/deletesubmit.py*
```Python
sql = "delete from story where id = %s" % id
cursor = db.cursor()
cursor.execute(sql)
```
[http://localhost:8000/cgi-bin/deletesubmit.py?id=1](http://localhost:8000/cgi-bin/deletesubmit.py?id=1)
