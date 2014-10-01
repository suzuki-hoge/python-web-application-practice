#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

import sqlite3
db = sqlite3.connect('todo.db')

id = form.getvalue('id')

sql = "delete from task where id = %s" % id
cursor = db.cursor()
cursor.execute(sql)

db.commit()
db.close()

print "Content-type: text/html\n"
print "<meta http-equiv='refresh' content='0;URL=http://localhost:8000/cgi-bin/list.py'>"
