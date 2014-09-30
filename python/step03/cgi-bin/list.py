#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

id = form.getvalue('id', 'no id')

print "Content-type: text/html\n"
print '<html><body>'

import sqlite3
db = sqlite3.connect('todo.db')

id = form.getvalue('id', '')
if id == '':
	rows = db.execute('select * from story')
else:
	rows = db.execute('select * from story where id = %s' % id)
for row in rows:
	id = row[0]
	body = row[1]
	end = row[2]
	status = row[3]
	print '<p>%s : %s (%s) - %s</p>' % (id, body, end, status)
	print '<hr>'

db.close()

print '</body></html>'
