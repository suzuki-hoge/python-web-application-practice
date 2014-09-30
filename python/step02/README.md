##データベースを作ってみましょう
```Bash
> sqlite3 todo.db
sqlite> create table story(id integer primary key autoincrement, body varchar(32), end datetime, status int);
```
確認コマンド**select * from story;**
##データの追加をしてみましょう
```Bash
sqlite> insert into story(body, end, status) values('sample', '2014-09-30 17:15:00', 1);
```
##データの更新をしてみましょう
```Bash
sqlite> update story set status = 2 where id = 3;
```
##データの削除をしてみましょう
```Bash
sqlite> delete from story where id = 3;
```
##pythonを通して一覧を取得してみましょう
*workspace.py*
```Python
import sqlite3
db = sqlite3.connect('todo.db')
cursor = db.cursor()
rows = cursor.execute('select * from story')
```

##pythonを通して詳細を取得してみましょう
*workspace.py*
```Python
rows = cursor.execute('select * from story where id = 1')
```
