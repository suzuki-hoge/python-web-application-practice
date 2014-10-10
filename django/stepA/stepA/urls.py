# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import *
from bch.models import *
from bch.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

	url(r'^top/$', ListView.as_view(
			queryset = Thread.objects.all(),
			context_object_name = 'thread_list',
			template_name = 'top.html'
		),
	),

	url(r'^thread/create/$', CreateView.as_view(
			model = Thread,
			fields = ('title',),
			template_name = 'thread/form.html',
			success_url = '/top'
		),
	),

	url(r'^thread/update/(?P<pk>\d+)/$', UpdateView.as_view(
			model = Thread,
			fields = ('title',),
			template_name = 'thread/form.html',
			success_url = '/top'
		),
	),

	url(r'^thread/(?P<pk>\d+)/$', DetailView.as_view(
			model = Thread,
			context_object_name = 'thread',
			template_name = 'thread/responses.html',
		),
	),

	url(r'^response/create/(?P<fk>\d+)/$', ResponseCreateView.as_view(),
	),
]
