from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404, render
from myblog.mysql.dao.DailyDao import DailyDao
from myblog.mysql.dao.UserInfoDao import UserInfoDao
from myblog.mysql.dao.CommentDao import CommentDao
import datetime
import json




def get_index(req):
    if req.method == 'POST':
        return render_to_response('topic/index.html')
    else:
        print(req.session['username'])
        #获取得到日志
        dao = DailyDao()
        dailyList = dao.getAllDaily()
        recent_daily_list = dao.getRecentDaily()
        archives_list = dao.getArchivesDate()
        category_list  =  dao.getCategoryList()
        return render_to_response('topic/index.html',{'username':req.session['username'],'dailyList':dailyList,
                                                      'recent_daily_list':recent_daily_list,'archives_list':archives_list,'category_list':category_list})

def search_daily(req):
    search_str = req.GET.get('searchVal')
    type = req.GET.get('type')
    if type == 'note':
        dao = DailyDao()
        dailyList = dao.search_daily(search_str)
        return render_to_response('topic/search.html',{'username':req.session['username'],'dailyList':dailyList,'searchVal':search_str})
    else:
        dao = UserInfoDao()
        userList = dao.searchUserInfo(search_str)
        return HttpResponse(json.dumps(userList), content_type="application/json")

def daily_detail(req):
    daily_id = req.GET.get('dailyid')
    dao = DailyDao()
    daily = dao.getDailyById(daily_id)
    dao = CommentDao()
    commentList = dao.getAllCommentByDailyId(daily_id)
    print('----------')
    return render_to_response('topic/detail.html',
                              {'username': req.session['username'], 'daily': daily,'commentList':commentList})


def get_archives(req,year,month):
    print(year,month)
    if req.method == 'POST':
        return render_to_response('topic/index.html')
    else:
        #获取得到日志
        dao = DailyDao()
        # 获取指定月份下的所有文章
        dailyList = dao.getArchivesDaily(year,month)
        print(dailyList)
        #获取月份列表
        archives_list = dao.getArchivesDate()
        #获取最近的日志
        recent_daily_list = dao.getRecentDaily()
        category_list = dao.getCategoryList()
        return render_to_response('topic/index.html',{'username':req.session['username'],'dailyList':dailyList,
                                                      'recent_daily_list':recent_daily_list,'archives_list':archives_list,'category_list':category_list})

def get_category(req,id):
    print(id)
    if req.method == 'POST':
        return render_to_response('topic/index.html')
    else:
        #获取得到日志
        dao = DailyDao()
        # 获取指定分类下的所有文章
        dailyList = dao.getCategoryDailyList(id)
        print(dailyList)
        #获取月份列表
        archives_list = dao.getArchivesDate()
        #获取最近的日志显示列表
        recent_daily_list = dao.getRecentDaily()
        #获取年月显示列表
        category_list = dao.getCategoryList()
        return render_to_response('topic/index.html',{'username':req.session['username'],'dailyList':dailyList,
                                                      'recent_daily_list':recent_daily_list,'archives_list':archives_list,'category_list':category_list})


def setting_basic(req):
    # ajax  ProfileSubmit
    if req.method == 'POST':
        name = req.POST.get("name")
        gender = int(req.POST.get("gender"))
        marriage = int(req.POST.get("marriage"))
        birth_time = req.POST.get("birth_time")
        province = int(req.POST.get("province"))
        city = int(req.POST.get("city"))
        print(name,gender,marriage,birth_time,province,city)
        time = datetime.datetime.strptime(birth_time, '%Y-%m-%d')
        # 如何userid 存在，则修改数据，若userid不存在，则create数据
        # 插入数据


        return HttpResponseRedirect('/myblog/set/profile')
    else:
        return render_to_response('topic/setting.html', {'username': req.session['username']})












