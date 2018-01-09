# coding = utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
from  .forms import UserForm
import hashlib


def register(req):
    if req.method =='POST':
        uf = UserForm(req.POST)
        if(uf.is_valid()):
            mobile = uf.cleaned_data['mobile']
            password = uf.cleaned_data['password']
            password = hashlib.md5(password.encode("utf-8")).hexdigest()
            User.objects.create(mobile=mobile, password=password)
            return HttpResponseRedirect('login.html')
    else:
        uf = UserForm()
        return render_to_response('register.html',{'uf': uf} )


def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            mobile = uf.cleaned_data['mobile']
            password = uf.cleaned_data['password']
            password = hashlib.md5(password.encode("utf-8")).hexdigest()
            user = User.objects.filter(mobile__exact = mobile,password__exact = password)
            print(user)
            if user:
                response = HttpResponseRedirect('/online/index/')
                response.set_cookie('mobile',mobile,3600)
                return response
            else:
                return  HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
        return render_to_response('login.html', {'uf':uf },)
        context_instance = RequestContext(req)

def index(req):
    if req.method == 'POST':
        username = req.COOKIES.get('username','')
        return render_to_response('login.html')
    else:
        return render_to_response('index.html')

def forgetPwd(req):
    if req.method=='POST':
        #判断手机号和验证码是否正确，
        data = req.POST
        #检查数据库是否有该手机号码，查到后，并传id 到resetPwd页面
        user = User.objects.filter(mobile=data['mobile'])
        user_id = user[0].id
        # user = User.objects.get(mobile=data['mobile'])
        # # 如果输入的手机号和验证码正确，则跳转到重置密码页面
        return HttpResponseRedirect('resetPwd.html?'+'user_id='+str(user_id))
    else:
        return render_to_response('forgetPwd.html')

def resetPwd(req):
    if req.method=='POST':
        #如果输入的新密码和确认密码相等，则跳转到login页面
        return HttpResponseRedirect('login.html')
    else:
        user_id = req.GET['user_id']
        print(user_id)
        return render_to_response('resetPwd.html',{'user_id': user_id})
        # return render_to_response('resetPwd.html')
def logout(req):
    response =  HttpResponse('退出')
    response.delete_cookie('mobile')
    return HttpResponseRedirect('/online/login.html')

