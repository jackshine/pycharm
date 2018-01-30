# Create your views here.
import datetime

from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect,get_object_or_404,render
from .forms import *
from  comments.forms import CommentForm
from  comments.models import Comment
from django.views.generic import ListView
import re
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


from django.db.models import Q
import hashlib


class IndexView(ListView):
    model = Daily
    template_name = 'index.html'
    context_object_name = 'dailyList'
    paginate_by = 3

# def index(req):
#     if req.method == "POST":
#         return render_to_response('index.html')
#     else:
#         uf = DailyForm()
#         dailyList = Daily.objects.all()
#         username = False
#         if req.session.has_key('username'):
#             username = req.session['username']
#         return render_to_response('index.html', {'uf': uf, 'userid': 1, 'dailyList': dailyList, 'username': username})
#模拟测试网页数据
USER_LIST = []
for i in range(1,999):
    temp = {"name":"root"+str(i),"age":i}
    USER_LIST.append(temp)

def index(req):
    from .pager import Pagination
    current_page = req.GET.get('p')
    page_obj = Pagination(50, current_page)
    dailyList = Daily.objects.all()[page_obj.start():page_obj.end()]
    print(dailyList)
    return render_to_response( 'index.html',{'dailyList':dailyList,'page_obj':page_obj,'username':req.session['username']})

def index1(request):
    # 全部数据:USER_LIST,=>得出共有多少条数据
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象 (是否具有下一页，是否有上一页)

    current_page = request.GET.get('p')
    # Paginator对象，里面封装了上面那些值，把USER_LIST对象传过来了，显示10页
    paginator = Paginator(USER_LIST, 10)
    try:
        # page对象
        # posts配置对象(current_page用户可能填些不合法的字段）
        # paginator通过拿到了page对象，把current_page传进来
        posts = paginator.page(current_page)
        # has_next              是否有下一页
        # next_page_number      下一页页码
        # has_previous          是否有上一页
        # previous_page_number  上一页页码
        # object_list           分页之后的数据列表,已经切片好的数据
        # number                当前页
        # paginator             paginator对象

        # 表示你填的东西不是个整数
    except PageNotAnInteger:
        posts = paginator.page(1)
    # 空页的时候，表示你看完了，显示最后一页
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render_to_response('index1.html', {'posts': posts})

def index2(request):
    from .pager import Pagination
    current_page = request.GET.get('p')
    page_obj = Pagination(666, current_page)

    data_list = USER_LIST[page_obj.start():page_obj.end()]
    return render(request, 'index2.html', {'data': data_list, 'page_obj': page_obj})

class CustomPaginator(Paginator):
    def __init__(self, current_page, per_pager_num, *args, **kwargs):
        # per_pager_num  显示的页码数量
        self.current_page = int(current_page)
        self.per_pager_num = int(per_pager_num)
        super(CustomPaginator, self).__init__(*args, **kwargs)

    def pager_num_range(self):
        '''
        自定义显示页码数
        第一种：总页数小于显示的页码数
        第二种：总页数大于显示页数  根据当前页做判断  a 如果当前页大于显示页一半的时候  ，往右移一下
                                                b 如果当前页小于显示页的一半的时候，显示当前的页码数量
        第三种：当前页大于总页数
        :return:
        '''
        if self.num_pages < self.per_pager_num:
            return range(1, self.num_pages + 1)

        half_part = int(self.per_pager_num / 2)
        if self.current_page <= half_part:
            return range(1, self.per_pager_num + 1)

        if (self.current_page + half_part) > self.num_pages:
            return range(self.num_pages - self.per_pager_num + 1, self.num_pages)
        return range(self.current_page - half_part, self.current_page + half_part + 1)


class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        if re.match(r'\d+', year) and re.match(r'\d+', month):
            ym_date = year + '-' + (month if int(month) > 9 else ('0' + month))
        return super(ArchivesView, self).get_queryset().filter( created_time__startswith=ym_date).order_by('-created_time')



# def archives(req, year, month):
#     print(year,month)
#     if re.match(r'\d+', year) and re.match(r'\d+', month):
#         ym_date = year + '-' + (month if int(month) > 9 else ('0' + month))
#         dailyList = Daily.objects.filter( created_time__startswith=ym_date).order_by('-created_time')
#     print(dailyList)
#     return render_to_response('index.html', {'dailyList': dailyList})


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category,id=self.kwargs.get('id'))
        return super(CategoryView,self).get_queryset().filter(category=cate)

# def showCategory(req,id):
#     cate = get_object_or_404(Category, id=id)
#     dailyList = Daily.objects.filter(category = cate)
#     return render_to_response('index.html',{'dailyList': dailyList})

def login(req):
    if req.method == 'POST':
        uf = UserInfoLoginForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            print(username, password)
            password = hashlib.md5(password.encode("utf-8")).hexdigest()
            # user = UserInfo.objects.filter(username__exact = username)
            user = UserInfo.objects.get(username=username)
            print(user.userid)
            if user:
                req.session['username'] = username
                req.session['userid'] = user.userid
                response = HttpResponseRedirect('/myblog/index/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('/myblog/login/')
    else:
        uf = UserInfoLoginForm()
        return render_to_response('login.html', {'uf': uf}, )


def register(req):
    if req.method == 'POST':
        uf = UserInfoRegisterForm(req.POST)
        if (uf.is_valid()):
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            sex = uf.cleaned_data['sex']
            regtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            password = hashlib.md5(password.encode("utf-8")).hexdigest()
            UserInfo.objects.create(username=username, password=password, sex=sex, regtime=regtime)
            return HttpResponseRedirect('login.html')
    else:
        uf = UserInfoRegisterForm()
        return render_to_response('register.html', {'uf': uf})


def logout(req):
    response = HttpResponse('退出')
    response.delete_cookie('username')
    del req.session['username']
    return HttpResponseRedirect('/myblog/login.html')


def blog_publish(req):
    if req.method == "POST":
        uf = DailyForm(req.POST)
        if uf.is_valid():
            daily = uf.cleaned_data['daily']
            dailyname = uf.cleaned_data['dailyname']
            userid = req.POST.get('userid')
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            time = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
            # 逆序，查找最后一条userid=userid的数据

            Daily.objects.create(daily=daily, userid=userid, dailyname=dailyname, postingdate=time)
            dailyList = Daily.objects.all().filter(userid=userid).order_by('-dailyid')[0]
            dailyList = dailyList.to_json()
            return HttpResponse(dailyList, content_type="application/json")

    else:
        return render_to_response('123')


def deleteDaily(req):
    print(req.GET)
    dailyid = req.GET.get('dailyid')
    print(dailyid)
    Daily.objects.all().filter(dailyid=dailyid).delete()
    return HttpResponseRedirect('/myblog/index/')


def searchDaily(req):
    searchVal = req.POST.get('searchVal')
    uf = DailyForm()
    dailyList = Daily.objects.all().filter(Q(dailyname=searchVal) | Q(daily=searchVal))
    print(dailyList)
    list = []
    for i in dailyList:
        list.append(i.to_dict())
    print(list)
    return HttpResponse(json.dumps(list), content_type="application/json")


def showDaily(req):
    dailyid = req.GET.get('dailyid')
    daily = Daily.objects.get(id=dailyid)
    form = CommentForm()
    comment_list = Comment.objects.filter(dailyid=dailyid)
    print(comment_list)
    username = False
    if req.session.has_key('username'):
        username = req.session['username']
    context = {
        'daily': daily,
        'form': form,
        'comment_list': comment_list,
        'username': username
    }
    return render_to_response('detail.html', context=context)


def myblog(req):
    if req.method == "POST":
        uf = DailyForm(req.POST)
        if uf.is_valid():
            body = uf.cleaned_data['body']
            title = uf.cleaned_data['title']
            userid = req.session['userid']
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            time = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
            # 逆序，查找最后一条userid=userid的数据
            Daily.objects.create(body=body, author_id=userid, title=title, created_time=time, category_id='1',
                                 modified_time=time)
        return HttpResponseRedirect('/myblog/index/')
    else:
        uf = DailyForm()
        return render_to_response('myblog.html', {'username': req.session['username'], 'uf': uf})

def showUserInfo(req):
    if req.method == "POST":
        return  render_to_response("userInfo.html")
    else:
        return render_to_response("userInfo.html")

def setUserInfo(req):
    if req.method == "POST":
        return render_to_response("setUserInfo.html")
    else:
        return render_to_response("setUserInfo.html")

def upload(req):
    if req.method == 'POST':
        userInfo = daily = UserInfo.objects.get(userid=1)
        new_img = UserDetails(
            img = req.FILES.get('img'),
            userId=userInfo
        )
        new_img.save()
        return HttpResponseRedirect('showImg.html')
    else:
        return render_to_response("uploadImg.html")

def showImg(req):

    imgs = UserDetails.objects.all()
    for i in imgs:
        print(i.img)
    content = {
        'imgs':imgs,
    }
    return render_to_response('showImg.html',content)