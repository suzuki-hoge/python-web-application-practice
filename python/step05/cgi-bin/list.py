#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

id = form.getvalue('id', 'no id')

print "Content-type: text/html\n"
print '<html><body>'

import sqlite3
db = sqlite3.connect('todo.db')

stories = db.execute('select * from story')
for story in stories:
	storyId = story[0]
	storyBody = story[1]
	storyEnd = story[2]
	if story[3] == 1:
		storyStatus = 'not yet'
	elif story[3] == 2:
		storyStatus = 'doing'
	else:
		storyStatus = 'done'
	print '<p>'
	print '%s : %s (%s) - %s' % (storyId, storyBody, storyEnd, storyStatus)
	print "<a href='storyform.py?id=%s'>update</a>" % storyId
	print "<a href='storydeletesubmit.py?id=%s'>delete</a>" % storyId
	print '</p>'

	tasks = db.execute('select * from task where storyid = %s' % storyId)
	for task in tasks:
		taskId = task[0]
		taskBody = task[1]
		taskEnd = task[2]
		if task[3] == 1:
			taskStatus = 'not yet'
		elif task[3] == 2:
			taskStatus = 'doing'
		else:
			taskStatus = 'done'
		print '<p>'
		print '%s%s : %s (%s) - %s' % ('&nbsp;' * 8, taskId, taskBody, taskEnd, taskStatus)
		print "<a href='taskform.py?storyid=%s&taskid=%s'>update</a>" % (storyId, taskId)
		print "<a href='taskdeletesubmit.py?id=%s'>delete</a>" % taskId
		print '</p>'
	print "%s<a href='taskform.py?storyid=%s'>task-add</a>" % ('&nbsp;' * 8, storyId)
	print '<hr>'

db.close()

print "<a href='storyform.py'>story-add</a>"
print '</body></html>'
