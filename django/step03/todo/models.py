from django.db import models
from django.forms import ModelForm

class Story(models.Model):
	body = models.CharField(max_length = 32)
	end = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):
		return '%s : %s' % (self.id, self.body)

class Task(models.Model):
	body = models.CharField(max_length = 32)
	end = models.DateTimeField()
	status = models.IntegerField()
	story = models.ForeignKey(Story)

	def __unicode__(self):
		return '%s : %s' % (self.id, self.body)
