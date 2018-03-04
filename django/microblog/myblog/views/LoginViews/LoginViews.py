from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404, render
import json
import re
import datetime
import hashlib
from myblog.mysql.dao.UserInfoDao import UserInfoDao


def sign_in(req):

    if req.method == 'POST':
        data = {
            'status': 200
        }
        username = req.POST.get('username')
        password = req.POST.get('password')
        print(username,password)
        # user = UserInfo.objects.all().filter(username=username)
        dao = UserInfoDao()
        user = dao.getUserInfoByName(username)
        # 若不存在该用户，则提示用户不存在，
        if not user:
            data['status'] = 304 #用户不存在
            data['info'] = '用户不存在'
            return render_to_response('sign/sign_in.html',{'data':data})
        else:
            password = hashlib.md5(password.encode("utf-8")).hexdigest()
            if password==user['password']:
                req.session['username'] = user['username']
                req.session['userid'] = user['userid']
                response = HttpResponseRedirect('/myblog/index/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                data['status'] = 305#密码不对
                data['info'] = '密码不对'
            return render_to_response('sign/sign_in.html', {'data': data})
    else:
        return render_to_response('sign/sign_in.html')


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
        # user = UserInfo.objects.all().filter(username=username)
        dao = UserInfoDao()
        user = dao.getUserInfoByName(username)
        # 若不存在该用户，则注册该用户，
        if not user:
            create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(create_time)
            password = hashlib.md5(password.encode("utf-8")).hexdigest()
            # UserInfo.objects.create(username=username, password=password, regtime=regtime)
            # user = UserInfo.objects.all().filter(username=username)[0]
            dao.addUserInfo(username,password,create_time)
            user = dao.getUserInfoByName(username)
            print(user)
            req.session['username'] = user['username']
            req.session['userid'] = user['userid']
            response = HttpResponseRedirect('/myblog/index/')
            response.set_cookie('username', username, 3600)
            response.set_cookie('userid', user['userid'], 3600)
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
