from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'myblog'
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index*', views.index),
    url(r'^index1.html$', views.index1),
    url(r'^index2.html/$', views.index2),
    url(r'^login*', views.login),
    url(r'^logout*', views.logout),
    url(r'^register*', views.register),
    url(r'^publish/$', views.blog_publish),
    url(r'^deleteDaily/*', views.deleteDaily),
    url(r'^searchDaily/*', views.searchDaily),
    url(r'^daily/*', views.showDaily),
    url(r'^myblog*', views.myblog),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    #[0-9]表示这部分必须是数字，+表示至少1个数字
    url(r'^category/(?P<id>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    # url(r'^showUserInfo*', views.showUserInfo),
    # url(r'^setUserInfo*', views.uploadImg),
    url(r'^showImg', views.showImg),
    url(r'^uploadImg', views.uploadImg),
    url(r'^update_img*', views.update_img),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)