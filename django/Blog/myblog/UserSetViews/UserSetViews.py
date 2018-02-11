
from django.shortcuts import render_to_response, HttpResponse
import os
import sys
import json
import base64
import re
import datetime
import random
from django.conf import settings
from  myblog.models import UserInfo,UserDetails
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