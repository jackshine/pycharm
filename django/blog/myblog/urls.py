from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index*', views.index),
    url(r'^login*', views.login),
    url(r'^register*', views.register),
    url(r'^publish/$', views.blog_publish),
    url(r'^deleteDaily/*', views.deleteDaily),
    url(r'^searchDaily/*', views.searchDaily),
    url(r'^daily/*', views.showDaily),
    url(r'^myblog*', views.myblog),
]