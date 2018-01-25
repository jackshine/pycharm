from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(\d+)/$', views.daily_comment, name='daily_comment'),
]