from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bug
from django.http import HttpResponseRedirect

class BugListView(ListView):
  model = Bug
  context_object_name = 'bug_list'
  template_name = 'bug_list.html'

class BugDetailView(DetailView):
  model = Bug
  context_object_name = 'bug'
  template_name = 'bug_detail.html'

class BugCreateView(CreateView):
  model = Bug
  fields=['title', 'description', 'assignee', 'priority', 'status']
  template_name = 'bug_new.html'
  success_url = reverse_lazy('bug_list')

class BugUpdateView(UpdateView):
    model = Bug
    fields = ['title', 'description', 'assignee', 'priority', 'status']
    template_name = 'bug_update.html'

class BugDeleteView(DeleteView):
    model = Bug
    success_url = reverse_lazy('bug_list')
    template_name = 'bug_delete.html'
