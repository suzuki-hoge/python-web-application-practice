#!/usr/bin/env python

import sqlite3
db = sqlite3.connect('todo.db')
cursor = db.cursor()

id = 1
#id = ''

if id == '':
	rows = cursor.execute('select * from story')
else:
	rows = cursor.execute('select * from story where id = 1')
for row in rows:
	print row

db.close()
