from myblog.models import UserInfo
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404, render
import json
import re
import datetime
import hashlib


def sign_in(req):
    if req.method == 'POST':
        return HttpResponseRedirect('login.html')
    else:
        return render_to_response('sign_up.html')


def sign_out(req):
    if req.method == 'POST':
        return HttpResponseRedirect('login.html')
    else:
        return render_to_response('sign_up.html')


def sign_up(req):
    if req.method == 'POST':
        data = {
            'msg': '0'
        }
        username = req.POST.get('user_nickname')
        password = req.POST.get('user_password')
        print(username, password)
        # 后台验证用户名格式
        matchName = re.match('[a-zA-z]\\w{1,9}', username)
        if not matchName:
            # 301 用户名不符合规则
            data['msg'] = '301'
            return HttpResponse(json.dumps(data), content_type="application/json")
        # 后台验证密码格式
        matchPwd = re.match('.{6,16}', password)
        if not matchPwd:
            # 302 密码不符合规则
            data['msg'] = '302'
            return HttpResponse(json.dumps(data), content_type="application/json")
        user = UserInfo.objects.all().filter(username=username)
        # 若不存在该用户，则注册该用户，
        if not user:
            regtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            password = hashlib.md5(password.encode("utf-8")).hexdigest()
            UserInfo.objects.create(username=username, password=password, regtime=regtime)
            user = UserInfo.objects.all().filter(username=username)[0]
            req.session['username'] = username
            req.session['userid'] = user.userid
            response = HttpResponseRedirect('/myblog/index/')
            response.set_cookie('username', username, 3600)
            return response
        else:
            data['msg'] = '303'
            return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return render_to_response('sign/sign_up.html')


def sign_up_ajax_check(req):
    username = req.POST.get('username')
    msg = '1'
    try:
        user = UserInfo.objects.get(username=username)
    except UserInfo.DoesNotExist:
        msg = '0'
    data = {
        'msg': msg
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
