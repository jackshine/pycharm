from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from myblog.views.LoginViews import LoginViews

app_name = 'myblog'
urlpatterns = [
    url(r'^sign_in/$', LoginViews.sign_in),
    url(r'^sign_out/$', LoginViews.sign_out),
    url(r'^sign_up/$', LoginViews.sign_up),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)