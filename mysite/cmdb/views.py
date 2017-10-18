# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

user_list = [
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"},
]

# Create your views here.
def index(request):
    if request.method =="POST":
        username = request.POST.get("username",None)
        pwd = request.POST.get("password",None)
        #添加数据到数据库
        models.UserInfo.objects.create(user=username,pwd=pwd)
        temp = {"user":username,"pwd":pwd}
        user_list.append(temp)
        print  user_list
    return render(request,"index.html",{"data":user_list})