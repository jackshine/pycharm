from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404, render
from myblog.mysql.dao.DailyDao import DailyDao
from myblog.mysql.dao.UserInfoDao import UserInfoDao
from myblog.mysql.dao.CommentDao import CommentDao
import json
import datetime

def create_comment(req):
    if req.session.has_key('username') and req.session.has_key('userid'):
        username = req.session['username']
        user_id = req.session['userid']
        #插入评论
        content = req.POST.get('content')
        daily_id = int(req.POST.get('dailyid'))
        create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dao = CommentDao()
        #添加评论
        dao.addComment(content,create_time,daily_id,user_id)
        #查找该文章最后一条评论
        comment = dao.getLastComment(daily_id)
        return HttpResponse(json.dumps(comment), content_type="application/json")
    else:
        print('bbbbbbbbbbbbbbb')















