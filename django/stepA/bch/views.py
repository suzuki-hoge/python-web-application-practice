from django.shortcuts import redirect
from django.views.generic import CreateView
from bch.models import *

class ResponseCreateView(CreateView):
	template_name = "response/form.html"
	model = Response
	fields = ('contents', 'creator',)

	def form_valid(self, form):
		fk = self.kwargs.get('fk')
		thread = Thread.objects.get(pk = fk)
		self.object = form.save(commit = False)
		self.object.thread = thread
		self.object.save()

		return redirect('/thread/%s' % fk)
