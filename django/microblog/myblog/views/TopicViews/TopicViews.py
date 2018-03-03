from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404, render
from myblog.mysql.dao.DailyDao import DailyDao
from myblog.mysql.dao.UserInfoDao import UserInfoDao
import json


def get_index(req):
    if req.method == 'POST':
        return render_to_response('topic/index.html')
    else:
        print(req.session['username'])
        #获取得到日志
        dao = DailyDao()
        dailyList = dao.getAllDaily()
        print(dailyList)
        recent_daily_list = dao.getRecentDaily()
        archives_list = dao.getArchivesDaily()
        category_list  =  dao.getCategoryDaily()
        print(category_list)
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
        print(userList)
        return HttpResponse(json.dumps(userList), content_type="application/json")










