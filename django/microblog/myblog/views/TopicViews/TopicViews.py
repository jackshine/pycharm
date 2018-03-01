from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404, render
from myblog.mysql.dao.DailyDao import DailyDao


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
        return render_to_response('topic/index.html',{'username':req.session['username'],'dailyList':dailyList,
                                                      'recent_daily_list':recent_daily_list,'archives_list':archives_list,'category_list':category_list})






