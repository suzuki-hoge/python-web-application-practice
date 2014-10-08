##ステータスを文字列にしてみましょう
*todo/models.py*
```Python
STATUS = (
	(1, 'not yet'),
	(2, 'doing'),
	(3, 'done'),
)

status = models.IntegerField(choices = STATUS)
```
[http://localhost:18000/story/create](http://localhost:18000/story/create)  
[http://localhost:18000/story/update/1](http://localhost:18000/story/update/1)  
[http://localhost:18000/task/create/1](http://localhost:18000/task/create/1)  
[http://localhost:18000/task/update/1](http://localhost:18000/task/update/1)  
##ストーリごとのタスクを期限順で取得できるようにしておきましょう
*todo/models.py*
```Python
class Story(models.Model):
~~
	@property
	def sorted_tasks(self):
		return self.task_set.order_by('end')
```
##モデルに出力フォーマットを定義してみましょう
*todo/models.py*
```Python
from django.utils import dateformat
~~
def __unicode__(self):
	end = dateformat.format(self.end, 'n/d H:i')
	status = self.get_status_display()
	return '%s ( %s ) [ %s ]' % (end, status, self.body)
```
**管理画面が変わっていることを確認しましょう**  
[http://localhost:18000/admin](http://localhost:18000/admin)  
##HTMLを整理して画面を整えましょう
*template/story/index.html*
```HTML
{% for story in story_list %}
	<dl>
		<dt>
			<form action='/story/delete/{{ story.id }}' method='post'>
				{{ story }}
				{% csrf_token %}
				<a id='story_update_{{ story.id }}' href='/story/update/{{ story.id }}'><img height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/edit.png'></a>
				<input id='story_delete_{{ story.id }}' type='image' height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/trash.png'>
			</form>
		</dt>
		{% for task in story.sorted_tasks %}
			<dd>
				<form action='/task/delete/{{ task.id }}' method='post'>
					{{ task }}
					{% csrf_token %}
					<a id='task_update_{{ task.id }}' href='/task/update/{{ task.id }}'><img height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/edit.png'></a>
					<input id='task_delete_{{ task.id }}' type='image' height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/trash.png'>
				</form>
			</dd>
		{% endfor %}
		<dd>
			<a id='task_create' href='/task/create/{{ story.id }}'><img height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/plus.png'></a>
		</dd>
	</dl>
	<hr>
{% endfor %}

<a id='story_create' href='/story/create'><img height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/plus.png'></a>
```
[http://localhost:18000/story](http://localhost:18000/story)  
[最終画面イメージ](https://github.com/tenshiPure/pyweb/blob/master/django/step04/images/last.png)
