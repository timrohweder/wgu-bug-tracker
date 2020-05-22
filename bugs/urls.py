from django.urls import path

from .views import BugListView, BugDetailView, BugCreateView, BugUpdateView, BugDeleteView, add_comment


urlpatterns = [
  path('', BugListView.as_view(), name='bug_list'),
  path('<int:pk>', BugDetailView.as_view(), name='bug_detail'),
  path('<int:pk>/edit', BugUpdateView.as_view(), name='bug_update'),
  path('<int:pk>/delete', BugDeleteView.as_view(), name='bug_delete'),
  path('new/', BugCreateView.as_view(), name='bug_new'),
  path('<int:pk>/comment', add_comment, name='add_comment'),
]
