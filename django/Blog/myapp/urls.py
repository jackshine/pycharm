from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^blogs*', views.get_blogs),
    url(r'^detail/(\d+)/$',views.get_details),
]
