#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

import sqlite3
db = sqlite3.connect('todo.db')

import os
if os.environ['REQUEST_METHOD'] == "POST":
	storyId = form.getvalue('storyid')
	taskId = form.getvalue('taskid')
	body = form.getvalue('body')
	end = form.getvalue('end')
	status = form.getvalue('status')

	if taskId is None:
		sql = "insert into task(body, end, status, storyid) values('%s', '%s', '%s', '%s')" % (body, end, status, storyId)
		cursor = db.cursor()
		cursor.execute(sql)
	else:
		sql = "update task set body = '%s', end = '%s', status = '%s', storyid = '%s' where id = %s" % (body, end, status, storyId, taskId)
		cursor = db.cursor()
		cursor.execute(sql)

	db.commit()
	db.close()

print "Content-type: text/html\n"
print "<meta http-equiv='refresh' content='0;URL=http://localhost:8000/cgi-bin/list.py'>"
