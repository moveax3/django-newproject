import logging
from django.views.generic import ListView, DetailView
from .models import Role

logger = logging.getLogger('default')

class RolesDetailView(DetailView):
    model = Role

    def get_object(self, queryset=None):
        object = super(RolesDetailView, self).get_object()
        return object

class RolesListView(ListView):
    model = Role
