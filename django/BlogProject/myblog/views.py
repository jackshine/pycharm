# Create your views here.
import datetime

from django.shortcuts import render_to_response, HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.db.models import Q
import hashlib

def index(req):
    if req.method == "POST":
        return render_to_response('index.html')
    else:
        uf = DailyForm()
        dailyList = Daily.objects.all()
        return render_to_response('index.html',{'uf':uf,'userid':1,'dailyList':dailyList})

def login(req):
    if req.method == 'POST':
        uf = UserInfoForm(req.POST)
        if uf.is_valid():
            mobile = uf.cleaned_data['mobile']
            password = uf.cleaned_data['password']
            password = hashlib.md5(password.encode("utf-8")).hexdigest()
            user = UserInfo.objects.filter(mobile__exact = mobile,password__exact = password)
            print(user)
            if user:
                req.session['mobile'] = mobile
                response = HttpResponseRedirect('/online/index/')
                response.set_cookie('mobile',mobile,3600)
                return response
            else:
                return  HttpResponseRedirect('/online/login/')
    else:
        uf = UserInfoForm()
        return render_to_response('login.html', {'uf':uf },)

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
            # dailyList = Daily.objects.all().filter(userid=userid)
            # print(dailyList.dailyname)
            # print(type(dailyList))
            # dailyList = Daily.objects.filter(dailyid__exact=count)
            # if dailyList:
            #     dailyList = serializers.serialize("json",dailyList)
            #     # return JsonResponse({"dailyList":dailyList})
            #     return HttpResponse(dailyList,content_type="application/json")
            dailyList = Daily.objects.all().filter(userid=userid).order_by('-dailyid')[0]
            dailyList = dailyList.to_json()
            return HttpResponse(dailyList, content_type="application/json")

    else:
        return render_to_response('123')


def deleteDaily(req):
    print(req.GET)
    dailyid = req.GET.get('dailyid')
    print(dailyid)
    Daily.objects.all().filter(dailyid=dailyid).delete()
    return HttpResponseRedirect('/myblog/index/')

def searchDaily(req):
    searchVal = req.GET.get('searchVal')
    print(searchVal)
    uf = DailyForm()
    dailyList = Daily.objects.all().filter(Q(dailyname=searchVal)|Q(daily=searchVal))
    return render_to_response('index.html', {'uf':uf, 'dailyList': dailyList})

def showDaily(req):
    dailyid = req.GET.get('dailyid')
    daily = Daily.objects.get(dailyid = dailyid)
    return render_to_response('blog.html', {'daily':daily})


