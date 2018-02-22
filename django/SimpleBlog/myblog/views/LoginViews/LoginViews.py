from myblog.models import *
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404, render


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
