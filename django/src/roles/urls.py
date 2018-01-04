from .views import RolesListView, RolesDetailView
from django.conf.urls import url

urlpatterns = (
    url(r'^list/$', RolesListView.as_view()),
    url(r'^detail/(?P<pk>\d+)/$', RolesDetailView.as_view()),
)
