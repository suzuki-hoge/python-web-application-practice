##画面に一覧を表示してみましょう
*list.py*
```Python
rows = db.execute('select * from story')

id = row[0]
body = row[1]
end = row[2]
status = row[3]
print '<p>%s : %s (%s) - %s</p>' % (id, body, end, status)
print '<hr>'
```
##画面に詳細を表示してみましょう
*list.py*
```Python
id = form.getvalue('id', '')
rows = db.execute('select * from story where id = %s' % id)
```
##追加する画面を作ってみよう
*form.py*
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
**sendボタンを押すとlocalhost/cgi-bin/formsubmit.pyに遷移すれば成功です(404になります）**
##追加の保存処理を作ってみよう
*formsubmit.py*
```Python
sql = "insert into story(body, end, status) values('%s', '%s', '%s')" % (body, end, status)
cursor = db.cursor()
cursor.execute(sql)
db.commit()
```
##編集する画面を作ってみよう
*form.py*
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
##編集の保存処理を作ってみよう
*formsubmit.py*
```Python
sql = "update story set body = '%s', end = '%s', status = '%s' where id = %s" % (body, end, status, id)
cursor = db.cursor()
cursor.execute(sql)
```
##削除処理を作ってみよう
*deletesubmit.py*
```Python
sql = "delete from story where id = %s" % id
cursor = db.cursor()
cursor.execute(sql)
```