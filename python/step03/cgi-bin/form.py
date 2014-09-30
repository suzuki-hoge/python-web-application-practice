#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

print "Content-type: text/html\n"
print '<html><body>'

import sqlite3
db = sqlite3.connect('todo.db')

id = form.getvalue('id', '')
if id == '':
	body = ''
	end = ''
	status = ''
else:
	rows = db.execute('select * from story where id = %s' % id)
	for row in rows:
		body = row[1]
		end = row[2]
		status = row[3]

print "<form method='post' action='formsubmit.py'>"
print "<p><input type=hidden name=id value='%s'></p>" % id
print "<p>body : <input type=text name=body value='%s'></p>" % body
print "<p>end : <input type=text name=end value='%s'></p>" % end
print "<p>status : <input type=text name=status value='%s'></p>" % status
print "<p><input type='submit' value='send'></p>"
print "</form>"

print '</body></html>'
