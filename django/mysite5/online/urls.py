from django.conf.urls import url
from online import views

urlpatterns =[
    url(r'^regist/$', views.regist),
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
]
