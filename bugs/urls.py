from django.urls import path

from .views import BugListView, BugDetailView, BugCreateView, BugUpdateView, BugDeleteView, add_comment, SearchView, ReportsView, ResolvedReportView, CurrentBugsReportView, AssigneeBugsReportView


urlpatterns = [
  path('', BugListView.as_view(), name='bug_list'),
  path('<int:pk>', BugDetailView.as_view(), name='bug_detail'),
  path('<int:pk>/edit', BugUpdateView.as_view(), name='bug_update'),
  path('<int:pk>/delete', BugDeleteView.as_view(), name='bug_delete'),
  path('new/', BugCreateView.as_view(), name='bug_new'),
  path('<int:pk>/comment', add_comment, name='add_comment'),
  path('search/', SearchView.as_view(), name='search'),
  path('reports/', ReportsView.as_view(), name='reports'),
  path('resolved-bugs-year-report/', ResolvedReportView.as_view(), name='resolved_report'),
  path('current-bugs-report/', CurrentBugsReportView.as_view(), name='current_report'),
  path('bugs-by-assignee-report/', AssigneeBugsReportView.as_view(), name='assignee_report'),
]
