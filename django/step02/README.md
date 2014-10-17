##一覧表示をする画面を作成してみましょう
*step02/settings.py*
```Python
TEMPLATE_DIRS = ( 
    os.path.join(BASE_DIR, 'template'),
)
```
*step02/urls.py*
```Python
from django.views.generic import *
from todo.models import *

url(r'^story/$', ListView.as_view(
		queryset = Story.objects.order_by('end'),
		context_object_name = 'story_list',
		template_name = 'story/index.html'
	),
),
```
*template/story/index.html*
```HTML
{% for story in story_list %}
	<p>{{ story.body }}</p>
	{% for task in story.task_set.all %}
		<p>{{ task.body }}</p>
	{% endfor %}
	<hr>
{% endfor %}
```
[http://localhost:18000/story/](http://localhost:18000/story/)
##ストーリを追加・編集・削除する画面をそれぞれ作成してみましょう
*step02/urls.py*
```Python
url(r'^story/create/$', CreateView.as_view(
		model = Story,
		fields = ('body', 'end', 'status',),
		template_name = 'story/form.html'
	),
),

url(r'^story/update/(?P<pk>\d+)/$', UpdateView.as_view(
		model = Story,
		fields = ('body', 'end', 'status',),
		template_name = 'story/form.html'
	),
),

url(r'^story/delete/(?P<pk>\d+)$',
	DeleteView.as_view(
		model = Story,
		success_url = '/story'
	),
),
```
*tempate/story/form.html*
```HTML
{{ form.as_p }}
```
**生成されたHTMLを確認してみましょう**  
**削除画面はまだ確認できません**  
[http://localhost:18000/story/create](http://localhost:18000/story/create)  
[http://localhost:18000/story/update/1](http://localhost:18000/story/update/1)
##各種ボタンを配置してみましょう
*template/story/index.html*
```HTML
{% for story in story_list %}
	<p>
		<form action='/story/delete/{{ story.id }}' method='post'>
			{{ story.body }}

			<a href='/story/update/{{ story.id }}'>story-update</a>

			{% csrf_token %}
			<input type='submit' value='story-delete'>
		</form>
	</p>
	{% for task in story.task_set.all %}
		<p>{{ task.body }}</p>
	{% endfor %}
	<hr>
{% endfor %}

<a href='/story/create'>story-create</a>
```
[http://localhost:18000/story/](http://localhost:18000/story/)  
*template/story/form.html*
```HTML
<form action='/story/form/' method='post'>
	{{ form.as_p }}
	{% csrf_token %}
	<input type='submit' value='send'>
</form>
```
**追加・編集・削除がそれぞれ動作することを確認しましょう**  
**内容や日付を入力しないでsendボタンを押すとどうなるか確認しましょう**  
[http://localhost:18000/story/create](http://localhost:18000/story/create)  
[http://localhost:18000/story/update/1](http://localhost:18000/story/update/1)
