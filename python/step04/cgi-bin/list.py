#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

id = form.getvalue('id', 'no id')

print "Content-type: text/html\n"
print '<html><body>'

import sqlite3
db = sqlite3.connect('todo.db')

rows = db.execute('select * from story')
for row in rows:
	id = row[0]
	body = row[1]
	end = row[2]
	if row[3] == 1:
		status = 'not yet'
	elif row[3] == 2:
		status = 'doing'
	else:
		status = 'done'
	print '<p>'
	print '%s : %s (%s) - %s' % (id, body, end, status)
	print "<a href='form.py?id=%s'>update</a>" % id
	print "<a href='deletesubmit.py?id=%s'>delete</a>" % id
	print '</p>'
	print '<hr>'

db.close()

print "<a href='form.py'>add</a>"
print '</body></html>'
