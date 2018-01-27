# Create your views here.
import datetime

from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from .forms import *
from  comments.forms import CommentForm
from  comments.models import Comment

from django.db.models import Q
import hashlib


def index(req):
    if req.method == "POST":
        return render_to_response('index.html')
    else:
        uf = DailyForm()
        dailyList = Daily.objects.all()
        username = False
        if req.session.has_key('username'):
            username = req.session['username']
        return render_to_response('index.html', {'uf': uf, 'userid': 1, 'dailyList': dailyList, 'username': username})


def archives(req, year, month):
    print(year,month)
    dailyList = Daily.objects.filter(created_time__year=year,
                                     created_time__month=month
                                     ).order_by('-created_time')
    print(dailyList)
    return render_to_response('index.html', {'dailyList': dailyList})


def login(req):
    if req.method == 'POST':
        uf = UserInfoLoginForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            print(username, password)
            password = hashlib.md5(password.encode("utf-8")).hexdigest()
            # user = UserInfo.objects.filter(username__exact = username)
            user = UserInfo.objects.get(username=username)
            print(user.userid)
            if user:
                req.session['username'] = username
                req.session['userid'] = user.userid
                response = HttpResponseRedirect('/myblog/index/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('/myblog/login/')
    else:
        uf = UserInfoLoginForm()
        return render_to_response('login.html', {'uf': uf}, )


def register(req):
    if req.method == 'POST':
        uf = UserInfoRegisterForm(req.POST)
        if (uf.is_valid()):
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            sex = uf.cleaned_data['sex']
            regtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            password = hashlib.md5(password.encode("utf-8")).hexdigest()
            UserInfo.objects.create(username=username, password=password, sex=sex, regtime=regtime)
            return HttpResponseRedirect('login.html')
    else:
        uf = UserInfoRegisterForm()
        return render_to_response('register.html', {'uf': uf})


def logout(req):
    response = HttpResponse('退出')
    response.delete_cookie('username')
    del req.session['username']
    return HttpResponseRedirect('/myblog/login.html')


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

            Daily.objects.create(daily=daily, userid=userid, dailyname=dailyname, postingdate=time)
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
    searchVal = req.POST.get('searchVal')
    uf = DailyForm()
    dailyList = Daily.objects.all().filter(Q(dailyname=searchVal) | Q(daily=searchVal))
    print(dailyList)
    list = []
    for i in dailyList:
        list.append(i.to_dict())
    print(list)
    return HttpResponse(json.dumps(list), content_type="application/json")


def showDaily(req):
    dailyid = req.GET.get('dailyid')
    daily = Daily.objects.get(id=dailyid)
    form = CommentForm()
    comment_list = Comment.objects.filter(dailyid=dailyid)
    print(comment_list)
    username = False
    if req.session.has_key('username'):
        username = req.session['username']
    context = {
        'daily': daily,
        'form': form,
        'comment_list': comment_list,
        'username': username
    }
    return render_to_response('detail.html', context=context)


def myblog(req):
    if req.method == "POST":
        uf = DailyForm(req.POST)
        if uf.is_valid():
            body = uf.cleaned_data['body']
            title = uf.cleaned_data['title']
            userid = req.session['userid']
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            time = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
            # 逆序，查找最后一条userid=userid的数据
            Daily.objects.create(body=body, author_id=userid, title=title, created_time=time, category_id='1',
                                 modified_time=time)
        return HttpResponseRedirect('/myblog/index/')
    else:
        uf = DailyForm()
        return render_to_response('myblog.html', {'username': req.session['username'], 'uf': uf})
