##タスクを追加・編集・削除する画面をそれぞれ作成してみましょう
*step02/urls.py*
```Python
url(r'^task/create/(?P<fk>\d+)/$', TaskCreateView.as_view()),

url(r'^task/update/(?P<pk>\d+)/$', UpdateView.as_view(
		model = Task,
		fields = ('body', 'end', 'status',),
		template_name = 'task/form.html',
		success_url = '/story'
	),
),

url(r'^task/delete/(?P<pk>\d+)$',
	DeleteView.as_view(
		model = Task,
		success_url = '/story'
	),
),
```
*todo/views.py*
```Python
from django.shortcuts import redirect
from django.views.generic import CreateView
from todo.models import *

class TaskCreateView(CreateView):
	template_name = "task/form.html"
	model = Task
	success_url = '/story'
	fields = ('body', 'end', 'status',)

	def form_valid(self, form):
		fk = self.kwargs.get('fk')
		story = Story.objects.get(pk = fk)
		self.object = form.save(commit = False)
		self.object.story = story
		self.object.save()

		return redirect(self.success_url)

	def get_context_data(self, **kwargs):
		context = super(TaskCreateView, self).get_context_data(**kwargs)

		context['story_id'] = 1

		return context
```
*tempate/task/form.html*
```HTML
<form action='' method='post'>
	{{ form.as_p }}
	<input type='hidden' name='story_id' value='{{ story_id }}'>
	{% csrf_token %}
	<input type='submit' value='send'>
</form>
```
**一覧画面からタスクの各画面へ遷移するボタン等を配置しておきましょう**  
  
**動作確認をしてみましょう**  
  
**タスクをストーリに紐付けるために、標準の*CreateView*ではなく**  
**独自拡張した*TaskCreateView*を作成しています**  
**どの様にストーリに紐付けているか確認しておきましょう**  
[http://localhost:18000/story/](http://localhost:18000/story/)  
[画面イメージ](https://github.com/tenshiPure/pyweb/blob/master/django/step03/images/index.png)  
