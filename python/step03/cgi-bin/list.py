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
	print '<p>%s</p>' % str(row)

db.close()

print '</body></html>'
