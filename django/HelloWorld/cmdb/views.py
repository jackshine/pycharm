from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
import datetime
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>in %s hour,it will be %s.</body></html>"%now
    return HttpResponse(html)
def hours_ahead(request,offset):
    # offset =int(offset)
    now = datetime.datetime.now() +datetime.timedelta(hours=offset)
    html = "<html><body>in %s hour,it will be %s.</body></html>"%(now, offset)
    return HttpResponse(html)
# 表单
def search_form(request):
    print(os.path.join(BASE_DIR)+'/HelloWorld/templates')
    return render_to_response('search_form.html')
def search(request):
    if 'q' in request.GET:
        meassage = '你搜索的内容为：'+ request.GET['q']
    else:
        meassage = '你提交了空表单'
    return HttpResponse(meassage)
