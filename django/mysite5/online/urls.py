from django.conf.urls import url
from online import views

urlpatterns =[
    url(r'^register*', views.register),
    # url(r'^regist_page*', views.regist_page),
    url(r'^login*', views.login),
    url(r'^index*', views.index),
    url(r'^logout*', views.logout),
    url(r'^forgetPwd/$', views.forgetPwd),
    url(r'^resetPwd/$', views.resetPwd),
]
