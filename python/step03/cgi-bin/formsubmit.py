#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

import sqlite3
db = sqlite3.connect('todo.db')

id = form.getvalue('id')
body = form.getvalue('body')
end = form.getvalue('end')
status = form.getvalue('status')

if id is '':
	sql = "insert into story(body, end, status) values('%s', '%s', '%s')" % (body, end, status)
	cursor = db.cursor()
	cursor.execute(sql)
else:
	sql = "update story set body = '%s', end = '%s', status = '%s' where id = %s" % (body, end, status, id)
	cursor = db.cursor()
	cursor.execute(sql)

db.commit()
db.close()
