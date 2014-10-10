# -*- coding: utf-8 -*-
from django.db import models

class Thread(models.Model):
	title = models.CharField(max_length = 128)
	create_date = models.DateTimeField(auto_now_add = True)
	update_date = models.DateTimeField(auto_now = True)

	#
	# レスの数を返す関数
	#
	@property
	def get_response_num(self):
		return len(self.response_set.all())


	#
	# 管理画面等で {{ thread }} とやると表示される文字列
	#
	def __unicode__(self):
		return '%s : %s' % (self.id, self.title)
		
class Response(models.Model):
	contents = models.TextField()
	create_date = models.DateTimeField(auto_now_add = True)
	creator = models.CharField(max_length = 32, blank = True)
	thread = models.ForeignKey(Thread)

	#
	# 管理画面等で {{ response }} とやると表示される文字列
	#
	def __unicode__(self):
		return '%s : %s' % (self.id, self.contents)
