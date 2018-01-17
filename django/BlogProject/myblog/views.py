from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,render_to_response,HttpResponse
from .forms import DailyForm
from .models import Daily
import datetime
from django.http import JsonResponse
import json
from django.core import serializers
from .MyEncoder import MyEncoder
from .DateEncoder import DateEncoder

def index(req):
    if req.method == "POST":
        return render_to_response('index.html')
    else:
        #查找到useid =1 评论 展示到首页上
        uf = DailyForm()
        dailyList = Daily.objects.filter(userid__exact=1)
        return render_to_response('index.html',{'uf':uf,'userid':1,'dailyList':dailyList})

def blog_publish(req):
    if req.method == "POST":
        uf = DailyForm(req.POST)
        if uf.is_valid():
            daily = uf.cleaned_data['daily']
            dailyname = uf.cleaned_data['dailyname']
            userid = req.POST.get('userid')
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            time = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
            # 逆序，查找最后一条userid=userid的数据

            Daily.objects.create(daily=daily, userid=userid,dailyname=dailyname,postingdate=time)
            # dailyList = Daily.objects.all().filter(userid=userid).order_by('-dailyid')[0]
            # print(dailyList.dailyname)
            # print(type(dailyList))
            # dailyList = Daily.objects.filter(dailyid__exact=count)
            # if dailyList:
            #     dailyList = serializers.serialize("json",dailyList)
            #     # return JsonResponse({"dailyList":dailyList})
            #     return HttpResponse(dailyList,content_type="application/json")
            dailyList = Daily.objects.all().filter(userid=userid).order_by('-dailyid')[0]
            dailyList = dailyList.to_dict()
            print(json.dumps(dailyList, cls=DateEncoder))
            return HttpResponse(json.dumps(dailyList,cls=DateEncoder), content_type="application/json")

    else:
        return render_to_response('123')


