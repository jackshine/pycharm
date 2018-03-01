from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from myblog.views.LoginViews import LoginViews
from myblog.views.TopicViews import TopicViews

app_name = 'myblog'
urlpatterns = [
    url(r'^sign_in/$', LoginViews.sign_in,name='sign_in'),
    url(r'^sign_out/$', LoginViews.sign_out,name='sign_out'),
    url(r'^sign_up/$', LoginViews.sign_up,name='sign_up'),
    # url(r'^sign_up_ajax_check/$', LoginViews.sign_up_ajax_check),
    url(r'^index/$', TopicViews.get_index,name='index'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', TopicViews.get_index, name='archives'),
]