from django.utils import dateformat
from django.db import models
from django.forms import ModelForm

STATUS = (
	(1, 'not yet'),
	(2, 'doing'),
	(3, 'done'),
)

class Story(models.Model):
	body = models.CharField(max_length = 32)
	end = models.DateTimeField()
	status = models.IntegerField(choices = STATUS)

	def __unicode__(self):
		end = dateformat.format(self.end, 'n/d H:i')
		status = self.get_status_display()
		return '%s ( %s ) [ %s ]' % (end, status, self.body)

	@property
	def sorted_tasks(self):
		return self.task_set.order_by('end')

class Task(models.Model):
	body = models.CharField(max_length = 32)
	end = models.DateTimeField()
	status = models.IntegerField(choices = STATUS)
	story = models.ForeignKey(Story)

	def __unicode__(self):
		end = dateformat.format(self.end, 'n/d H:i')
		status = self.get_status_display()
		return '%s ( %s ) [ %s ]' % (end, status, self.body)
