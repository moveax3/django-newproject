from .views import TasksListView, TasksDetailView
from django.conf.urls import url

urlpatterns = (
    url(r'^list/$', TasksListView.as_view()),
    url(r'^detail/(?P<pk>\d+)/$', TasksDetailView.as_view()),
)
