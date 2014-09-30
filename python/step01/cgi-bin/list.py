#!/usr/bin/env python

print "Content-type: text/html\n"

import cgi
form = cgi.FieldStorage()

id = form.getvalue('id', 'no id')

print 'id : %s' % id
