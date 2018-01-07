# coding = utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,render_to_response
from django import forms
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
class UserForm(forms.Form):
    mobile = forms.CharField(label='手机号',max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

def register(req):
    if req.method =='POST':
        # print(req.POST)
        data  = req.POST
        print(data['password'])
        print(data['mobile'])
        # uf = UserForm(req.POST)
        # print(uf)
        # mobile = uf.cleaned_data['mobile']
        # password = uf.cleaned_data['password']
        User.objects.create(mobile=data['mobile'],password=data['password'])
        return HttpResponseRedirect('login.html')
    else:
        return render_to_response('register.html' )


def login(req):
    if req.method == 'POST':
        # uf = UserForm(req.POST)
        # if uf.is_valid():
        #     username = uf.cleaned_data['username']
        #     password = uf.cleaned_data['password']
        #     user = User.objects.filter(username__exact = username,password__exact = password)
        #     if user:
        #         response = HttpResponseRedirect('/online/index/')
        #         response.set_cookie('username',username,3600)
        #         return response
        #     else:
        #         return  HttpResponseRedirect('/online/login/')
        return HttpResponseRedirect('/online/index.html')
    else:
        uf = User
        return render_to_response('login.html', {'uf': uf},)
        context_instance = RequestContext(req)

def index(req):
    if req.method == 'POST':
        username = req.COOKIES.get('username','')
        return render_to_response('login.html')
    else:
        return render_to_response('index.html')

def forgetPwd(req):
    if req.method=='POST':
        # 如果输入的手机号和验证码正确，则跳转到充值密码页面
        return render_to_response('resetPwd.html')
    else:
        return render_to_response('forgetPwd.html')

def resetPwd(req):
    if req.method=='POST':
        #如果输入的新密码和确认密码相等，则跳转到login页面
        return render_to_response('login.html')

def logout(req):
    response =  HttpResponse('退出')
    response.delete_cookie('username')
    return HttpResponseRedirect('/online/login.html')

