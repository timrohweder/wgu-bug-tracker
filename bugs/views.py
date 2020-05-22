from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Bug
from django.http import HttpResponseRedirect
from .forms import CommentForm

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

def add_comment(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.bug = bug
            comment.author = request.user
            comment.save()
            return redirect('bug_detail', pk=bug.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})
