from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,render_to_response
from .forms import DailyForm
from .models import Daily
import datetime

def index(req):
    if req.method == "POST":
        return render_to_response('index.html')
    else:
        uf = DailyForm()
        return render_to_response('index.html',{'uf':uf,'userid':1})

def blog_publish(req):
    if req.method == "POST":
        uf = Daily(req.POST)
        if(uf.is_valid()):
            daily = uf.cleaned_data['daily']
            userid = uf.cleaned_data['userid']
            dailyname = uf.cleaned_data['dailyname']
            now_time = datetime.datetime.time()
            Daily.objects.create(daily=daily, userid=userid,dailyname=dailyname)
            render_to_response('index.html',{'uf':uf})
    else:
        return render_to_response('123')


