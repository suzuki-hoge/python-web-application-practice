from django.conf.urls import include, url
from django.views.generic import *
from django.contrib import admin
from todo.models import *
from todo.views import *

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^story/$', ListView.as_view(
			queryset = Story.objects.order_by('end'),
			context_object_name = 'story_list',
			template_name = 'story/index.html'
		),
	),

	url(r'^story/create/$', CreateView.as_view(
			model = Story,
			fields = ('body', 'end', 'status',),
			template_name = 'story/form.html',
			success_url = '/story'
		),
	),

	url(r'^story/update/(?P<pk>\d+)/$', UpdateView.as_view(
			model = Story,
			fields = ('body', 'end', 'status',),
			template_name = 'story/form.html',
			success_url = '/story'
		),
	),

	url(r'^story/delete/(?P<pk>\d+)$',
		DeleteView.as_view(
			model = Story,
			success_url = '/story'
		),
	),

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
]
