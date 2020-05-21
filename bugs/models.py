from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

class Bug(models.Model):
  PRIORITY_CHOICES = (('low', 'Low'), ('medium', 'Medium'), ('high', 'High'))
  STATUS_CHOICES = (('deferred', 'Deferred'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'))

  title = models.CharField(max_length=300)
  description = models.TextField()
  assignee = models.ForeignKey(
    get_user_model(),
    on_delete=models.SET_NULL,
    related_name='bug_assignee',
    null=True
  )
  created = models.DateTimeField(default=timezone.now)
  priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='deferred')

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('bug_detail', kwargs={'pk': str(self.pk)})
