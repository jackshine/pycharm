from django.conf.urls import url
from . import views
app_name = 'myblog'
urlpatterns = [
    url(r'^index*', views.index),
    url(r'^login*', views.login),
    url(r'^logout*', views.logout),
    url(r'^register*', views.register),
    url(r'^publish/$', views.blog_publish),
    url(r'^deleteDaily/*', views.deleteDaily),
    url(r'^searchDaily/*', views.searchDaily),
    url(r'^daily/*', views.showDaily),
    url(r'^myblog*', views.myblog),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(\d+)/$', views.showCategory, name='category')
]