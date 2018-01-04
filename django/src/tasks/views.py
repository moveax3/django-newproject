import logging
from django.views.generic import ListView, DetailView
from .models import Task

logger = logging.getLogger('default')

class TasksDetailView(DetailView):
    model = Task

    def get_object(self, queryset=None):
        object = super(TasksDetailView, self).get_object()
        return object

class TasksListView(ListView):
    model = Task



