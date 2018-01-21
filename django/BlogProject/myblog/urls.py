from django.conf.urls import url
from . import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^time/$', views.current_datetime),
    # url(r'^time/plus/(\d{1,2})/$',views.hours_ahead),
    url(r'^index/$', views.index),
    url(r'^login/$', views.login),
    url(r'^publish/$', views.blog_publish),
    url(r'^deleteDaily/*', views.deleteDaily),
    url(r'^searchDaily/*', views.searchDaily),
    url(r'^daily/*', views.showDaily),

]