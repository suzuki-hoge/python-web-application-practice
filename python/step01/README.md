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
[http://localhost:8000/](http://localhost:8000/)
##URLごとに違うpythonスクリプトを実行できるようにしてみましょう
*cgi-bin/list.py*
```Python
#!/usr/bin/env python
print "Content-type: text/html\n"
print 'my first app'
```
**list.pyの権限を755にする必要があります**  
[http://localhost:8000/cgi-bin/list.py](http://localhost:8000/cgi-bin/list.py)
##GETパラメータを拾えるようにしてみましょう
*cgi-bin/list.py*
```Python
import cgi
form = cgi.FieldStorage()

id = form.getvalue('id', 'no id')

print 'id : %s' % id
```
[http://localhost:8000/cgi-bin/list.py](http://localhost:8000/cgi-bin/list.py)  
[http://localhost:8000/cgi-bin/list.py?id=1](http://localhost:8000/cgi-bin/list.py?id=1)
