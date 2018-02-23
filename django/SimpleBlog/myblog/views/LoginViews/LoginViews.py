from myblog.models import UserInfo
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404, render
import json


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
        return HttpResponseRedirect('login.html')
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
