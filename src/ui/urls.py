from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^home/$', views.home),
    url(r'^query/$', views.query),
    url(r'^queries/$', views.queries),
    url(r'^logout/$', views.logout),
]