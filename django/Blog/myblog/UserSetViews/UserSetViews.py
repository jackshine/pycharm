
from django.shortcuts import render_to_response, HttpResponse,HttpResponseRedirect
import os
import sys
import json
import base64
import re
import datetime
import random
from django.conf import settings
from  myblog.models import UserInfo,UserDetails,Province,City
from myblog.util.mkdir import MkDir


def uploadImg(req):
    if req.method == 'POST':
        img = req.POST.get('photo')
        binaryImg = base64.b64decode(re.split(',', img)[1])
        userInfo = UserInfo.objects.get(userid=1)
        now_time = datetime.datetime.now().strftime('%Y%m%d')
        # 创建当前日期的文件夹
        date_path = settings.MEDIA_URL + 'upload/'+now_time
        mk = MkDir()
        mk.mkdir(date_path)
        # 随机生成16位十六进制数字,生成文件名
        path =  date_path + '/' + getRandomNum() + '.png'
        print(path)
        new_img = UserDetails(
                img=path,
                userId=userInfo
        )
        new_img.save()
        with open(path, 'wb') as f:
            f.write(binaryImg)
        return HttpResponse(json.dumps({'success':200}))
    else:
        return render_to_response("uploadImg.html")


def getRandomNum():
    random_list = [i for i in range(0, 10)] + [chr(i) for i in range(97, 122)]
    # 对应从“a”到“z”的ASCII码 [chr(i) for i in range(97,122)
    random_str = ''
    for i in range(16):
        random_str = random_str + str(random_list[random.randint(1, 16)])
    return random_str

def setUserInfo(req):
    if req.method == "POST":
        return render_to_response("setUserInfo.html")
    else:
        # 查询得到该用户的资料，再展示到setUserInfo页面
        userDetails = UserDetails.objects.all()
        print(userDetails)
        return render_to_response("setUserInfo.html")

def setProfile(req):
    # ajax  ProfileSubmit
    if req.method == 'POST':
        name = req.POST.get("name")
        gender = int(req.POST.get("gender"))
        marriage = int(req.POST.get("marriage"))
        birth_time = req.POST.get("birth_time")
        province = int(req.POST.get("province"))
        city = int(req.POST.get("city"))
        time = datetime.datetime.strptime(birth_time, '%Y-%m-%d')
        # 如何userid 存在，则修改数据，若userid不存在，则create数据
        city = City.objects.get(code=city)
        province = Province.objects.get(code=province)
        user = UserInfo.objects.get(userid='3')
        UserDetails.objects.create(sex=gender, marriage=marriage, birthtime=time, city=city, province=province,userId=user)
        return HttpResponseRedirect('/myblog/set/profile')
    else:
        user = UserInfo.objects.get(userid='1')
        userDetails = UserDetails.objects.get(userId=user)
        print(userDetails.province.code,userDetails.city.code,)
        return render_to_response('set_profile.html',{'userDetails':userDetails,'user':user})

def setAccount(req):
    # ajax  ProfileSubmit
    if req.method == 'POST':
       return render_to_response()
    else:

        return render_to_response('set_accout.html')