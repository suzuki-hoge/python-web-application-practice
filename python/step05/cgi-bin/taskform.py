#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

print "Content-type: text/html\n"
print '<html><body>'

import sqlite3
db = sqlite3.connect('todo.db')

storyId = form.getvalue('storyid', '')
taskId = form.getvalue('taskid', '')

if taskId == '':
	body = ''
	end = ''
	status = ''
else:
	rows = db.execute('select * from task where id = %s' % taskId)
	for row in rows:
		body = row[1]
		end = row[2]
		status = row[3]

print "<form method='post' action='taskformsubmit.py'>"
print "<p><input type=hidden name=storyid value='%s'></p>" % storyId
print "<p><input type=hidden name=taskid value='%s'></p>" % taskId
print "<p>body : <input type=text name=body value='%s'></p>" % body
print "<p>end : <input type=text name=end value='%s'></p>" % end
print "<p>status : <select name=status>"
print "<option value='1' %s>not yet</option>" % ('selected' if status == 1 else '')
print "<option value='2' %s>doing</option>" % ('selected' if status == 2 else '')
print "<option value='3' %s>done</option>" % ('selected' if status == 3 else '')
print '</select></p>'
print "<p><input type='submit' value='send'></p>"
print "</form>"

print '</body></html>'
