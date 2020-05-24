from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Bug
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.db.models import Q

class ReportsView(TemplateView):
  template_name = 'bug_reports.html'

class SearchView(TemplateView):
  template_name = 'bug_search.html'

class BugListView(ListView):
  model = Bug
  context_object_name = 'bug_list'
  template_name = 'bug_list.html'
  extra_context = {}

  def get_queryset(self):
    self.extra_context = {}
    results = Bug.objects.all()

    isSearch = self.request.GET.get('isSearch')
    if isSearch == 'True':
      self.extra_context["isSearch"] = True

    createdQuery = self.request.GET.get('createdQuery')
    if createdQuery is not None and createdQuery != '':
      dateList = createdQuery.split("/")
      month = dateList[0]
      day = dateList[1]
      year= dateList[2]
      results = results.filter(
          Q(created__month=month) & Q(created__day=day) & Q(created__year=year)
      )

    titleQuery = self.request.GET.get('titleQuery')
    if titleQuery is not None and titleQuery != '':
      results = results.filter(
          Q(title__icontains=titleQuery)
      )

    priorityQuery = self.request.GET.get('priorityQuery')
    if priorityQuery is not None and priorityQuery != '':
      results = results.filter(
          Q(priority__icontains=priorityQuery)
      )
      reportQuery = self.request.GET.get('reportQuery')
      if reportQuery == 'True':
        self.extra_context["reportType"] = priorityQuery

    assigneeQuery = self.request.GET.get('assigneeQuery')
    if assigneeQuery is not None and assigneeQuery != '':
      results = results.filter(
          Q(assignee__username__icontains=assigneeQuery)
      )

    statusQuery = self.request.GET.get('statusQuery')
    if statusQuery is not None and statusQuery != '':
      results = results.filter(
          Q(status__icontains=statusQuery)
      )
      reportQuery = self.request.GET.get('reportQuery')
      if reportQuery == 'True':
        self.extra_context["reportType"] = statusQuery

    yearQuery = self.request.GET.get('yearQuery')
    if yearQuery is not None and yearQuery != '':
      self.extra_context["reportType"] = yearQuery
      results = results.filter(
          Q(created__year=yearQuery)
      )

    return results

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
