# coding = utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
from  .forms import UserForm
import hashlib
from PIL import Image, ImageDraw, ImageFont
import random
from io import BytesIO
from django.http import JsonResponse




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
        mobile = req.POST.get('mobile')
        vcode = req.POST.get('vcode').upper()
        vcode_session = req.session.get('verifyCode').upper()
        print(mobile,vcode,vcode_session)
        #检查数据库是否有该手机号码，查到后，并传id 到resetPwd页面
        user = User.objects.filter(mobile=mobile)
        user_id = user[0].id
        # user = User.objects.get(mobile=data['mobile'])
        # # 如果输入的手机号和验证码正确，则跳转到重置密码页面
        if user:
            if vcode == vcode_session:
                return HttpResponseRedirect('resetPwd.html?' + 'user_id=' + str(user_id))
            else:
                return render_to_response('forgetPwd.html', {'msg': 'fail_verify'})
        else:
            return render_to_response('forgetPwd.html',{'msg': 'fail_mobile'})
    else:
        return render_to_response('forgetPwd.html')

def resetPwd(req):
    if req.method=='POST':
        #如果输入的新密码和确认密码相等，则跳转到login页面
        data = req.POST
        print(data)
        new_password =data['new_password']
        comfirm_password = data['comfirm_password']
        user_id = data['user_id']
        if(new_password==comfirm_password):
            pwd = hashlib.md5(new_password.encode("utf-8")).hexdigest()
            User.objects.filter(id=int(user_id)).update(password=pwd )
            return HttpResponseRedirect('login.html')
        else:
            return render_to_response('resetPwd.html')
    else:
        user_id = req.GET['user_id']
        print(user_id)
        return render_to_response('resetPwd.html',{'user_id': user_id})
        # return render_to_response('resetPwd.html')
def logout(req):
    response =  HttpResponse('退出')
    response.delete_cookie('mobile')
    return HttpResponseRedirect('/online/login.html')


def verify_code(request):
    # 1，定义变量，用于画面的背景色、宽、高
    # random.randrange(20, 100)意思是在20到100之间随机找一个数
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    # 2，创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 3，创建画笔对象
    draw = ImageDraw.Draw(im)
    # 4，调用画笔的point()函数绘制噪点，防止攻击
    for i in range(0, 100):
        # 噪点绘制的范围
        xy = (random.randrange(0, width), random.randrange(0, height))
        # 噪点的随机颜色
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        # 绘制出噪点
        draw.point(xy, fill=fill)
    # 5，定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 6，随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 7，构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    # 字体对象1为simsunb，字大小为36号
    # simsunb是三种ttf文件的集合，是“宋体、新宋体、宋体-PUA”三种字体的集合，可以通过在truetype中增加index参量实现对集合内字体的调用
    font = ImageFont.truetype('C:\Windows\Fonts\simsunb.ttf', 23)
    # 8，构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 9，绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 9，用完画笔，释放画笔
    del draw
    print(rand_str)
    # 10，存入session，用于做进一步验证
    request.session['verifyCode'] = rand_str
    # 11，内存文件操作
    buf = BytesIO()
    # 12，将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 13，将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
