##pythonの組み込みサーバを立ててみましょう
*run.py*
```Python
import CGIHTTPServer
CGIHTTPServer.test()
```

*index.html*
```HTML
<p>Hello world</p>
```
##URLごとに違うpythonスクリプトを実行できるようにしてみましょう
*cgi-bin/list.py*
```Python
#!/usr/bin/env python
print "Content-type: text/html\n"
print 'my first app'
```
**権限を755にする必要があります**
##GETパラメータを拾えるようにしてみましょう
*cgi-bin/list.py*
```Python
import cgi
form = cgi.FieldStorage()

id = form.getvalue('id', 'no id')

print 'id : %s' % id
```
**list.py や list.py?id=3 で出力がかわることを確認しましょう**
