##一覧画面の出力を整形してみましょう
*list.py*
```Python
for row in rows:
    id = row[0]
    body = row[1]
    end = row[2]
    status = row[3]
    print '<p>%s : %s (%s) - %s</p>' % (id, body, end, status)
    print '<hr>'
```
##ステータスを数値から文字列に置き換えてみましょう
*list.py*
```Python
if row[3] == 1:
    status = 'not yet'
elif row[3] == 2:
    status = 'doing'
else:
    status = 'done'
```
*form.py*
```Python
print "<p>status : <select name=status>"
print "<option value='1' %s>not yet</option>" % ('selected' if status == 1 else '')
print "<option value='2' %s>doing</option>" % ('selected' if status == 2 else '')
print "<option value='3' %s>done</option>" % ('selected' if status == 3 else '')
print '</select>'
```
##画面遷移をするボタンを配置してみましょう
*list.py*
```Python
print "<a href='form.py?id=%s'>update</a>" % id
print "<a href='deletesubmit.py?id=%s'>delete</a>" % id

print "<a href='form.py'>add</a>"
```
