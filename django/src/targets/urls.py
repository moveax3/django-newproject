from .views import TargetsListView, TargetsDetailView
from django.conf.urls import url

urlpatterns = (
    url(r'^list/$', TargetsListView.as_view()),
    url(r'^detail/(?P<pk>\d+)/$', TargetsDetailView.as_view()),
)
