from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404, render
from myblog.mysql.dao.DailyDao import DailyDao
from myblog.mysql.dao.UserInfoDao import UserInfoDao
from myblog.mysql.dao.CommentDao import CommentDao
from myblog.mysql.dao.UserDetailsDao import UserDetailsDao
from myblog.mysql.dao.CategoryDao import CategoryDao
from myblog.mysql.dao.UserCategoryDao import UserCategoryDao
from myblog.mysql.dao.UserDailyCategoryDao import UserDailyCategoryDao
from myblog.mysql.dao.UserImgDao import UserImgDao
from myblog.mysql.dao.UserTag import UserTag
from myblog.mysql.util.mkdir import MkDir
from django.conf import settings

import datetime
import json
import re
import base64
import random


def get_index(req):
    if req.method == 'POST':
        return render_to_response('topic/index.html')
    else:
        print(req.session['username'])
        # 获取得到日志
        dao = DailyDao()
        dailyList = dao.getAllDaily()
        recent_daily_list = dao.getRecentDaily()
        archives_list = dao.getArchivesDate()
        category_list = dao.getCategoryList()
        return render_to_response('topic/index.html', {'username': req.session['username'], 'dailyList': dailyList,
                                                       'recent_daily_list': recent_daily_list,
                                                       'archives_list': archives_list, 'category_list': category_list})


def search_daily(req):
    search_str = req.GET.get('searchVal')
    type = req.GET.get('type')
    if type == 'note':
        dao = DailyDao()
        dailyList = dao.search_daily(search_str)
        return render_to_response('topic/search.html', {'username': req.session['username'], 'dailyList': dailyList,
                                                        'searchVal': search_str})
    else:
        dao = UserInfoDao()
        userList = dao.searchUserInfo(search_str)
        return HttpResponse(json.dumps(userList), content_type="application/json")


def daily_detail(req):
    daily_id = req.GET.get('dailyid')
    dao = DailyDao()
    daily = dao.getDailyById(daily_id)
    dao = CommentDao()
    commentList = dao.getAllCommentByDailyId(daily_id)
    print('----------')
    return render_to_response('topic/detail.html',
                              {'username': req.session['username'], 'daily': daily, 'commentList': commentList})


def get_archives(req, year, month):
    print(year, month)
    if req.method == 'POST':
        return render_to_response('topic/index.html')
    else:
        # 获取得到日志
        dao = DailyDao()
        # 获取指定月份下的所有文章
        dailyList = dao.getArchivesDaily(year, month)
        print(dailyList)
        # 获取月份列表
        archives_list = dao.getArchivesDate()
        # 获取最近的日志
        recent_daily_list = dao.getRecentDaily()
        category_list = dao.getCategoryList()
        return render_to_response('topic/index.html', {'username': req.session['username'], 'dailyList': dailyList,
                                                       'recent_daily_list': recent_daily_list,
                                                       'archives_list': archives_list, 'category_list': category_list})


def get_category(req, id):
    print(id)
    if req.method == 'POST':
        return render_to_response('topic/index.html')
    else:
        # 获取得到日志
        dao = DailyDao()
        # 获取指定分类下的所有文章
        dailyList = dao.getCategoryDailyList(id)
        print(dailyList)
        # 获取月份列表
        archives_list = dao.getArchivesDate()
        # 获取最近的日志显示列表
        recent_daily_list = dao.getRecentDaily()
        # 获取年月显示列表
        category_list = dao.getCategoryList()
        return render_to_response('topic/index.html', {'username': req.session['username'], 'dailyList': dailyList,
                                                       'recent_daily_list': recent_daily_list,
                                                       'archives_list': archives_list, 'category_list': category_list})


def setting_basic(req):
    # ajax  ProfileSubmit
    if req.method == 'POST':
        name = req.POST.get("nickname")
        gender = int(req.POST.get("gender"))
        marriage = int(req.POST.get("marriage"))
        birthday = req.POST.get("birth_time")
        province = int(req.POST.get("province"))
        city = int(req.POST.get("city"))
        user_login_id = req.session['userid']
        print(name, gender, marriage, birthday, province, city, user_login_id)
        img_path = '/abc'
        # 如何userid 存在，则修改数据，若userid不存在，则create数据
        data = {'status': 303}
        dao = UserDetailsDao()

        user_details = dao.getUserDetail(user_login_id)
        print('-------------')
        print(user_details)
        print('-------------')

        if user_details:
            # 修改数据
            dao.updateUserDetail(user_login_id, gender, img_path, birthday, province, city, marriage,name)
            data['status'] = 200
        else:
            # 插入数据
            try:
                dao.addUserDetail(user_login_id, gender, img_path, birthday, province, city, marriage)
                data['status'] = 200
            except Exception as e:
                pass
        return HttpResponse(json.dumps(data), content_type="application/json")

    else:
        #获取用户的信息
        dao = UserDetailsDao()
        user_login_id = req.session['userid']
        data = dao.getUserDetail(user_login_id)
        user_details = data[0]
        distict = data[1]
        img_dao = UserImgDao()
        user_img = img_dao.getUserImg(user_login_id)
        dict = {'username': req.session['username'],
                'user_details': user_details,
                'distict': distict,
                }
        if user_img:
            dict['user_img'] = user_img
        print(dict)
        return render_to_response('topic/setting.html', dict)

def uploadImg(req):
    if req.method == 'POST':
        img = req.FILES.get('photo')

        now_time = datetime.datetime.now().strftime('%Y%m%d')
        # 创建当前日期的文件夹
        date_path = settings.MEDIA_URL + 'upload/'+now_time
        mk = MkDir()
        mk.mkdir(date_path)
        # 随机生成16位十六进制数字,生成文件名
        path =  date_path + '/' + getRandomNum() + '.png'
        dao = UserImgDao()
        user_login_id  =req.session['userid']
        with open(path, 'wb')as f:  # with open 无法创建文件夹，需要自己创建
            for chunk in img.chunks():
                f.write(chunk)
        print('---------------')
        print(path)
        print('333333333333333')
        if dao.getUserImgById(user_login_id):
            dao.updateUserImg(user_login_id, path)
        else:
            dao.addUserImg(user_login_id, path)
        msg = {
            'success': 200,
            'url': '/'+path
            # 客户端拿到路径，才能预览图片; media在setting中配置了别名，这里只写media，客户端就可以找到路径，前面不需要加/app
        }
        return HttpResponse(json.dumps(msg),content_type="application/json")

def getRandomNum():
    random_list = [i for i in range(0, 10)] + [chr(i) for i in range(97, 122)]
    # 对应从“a”到“z”的ASCII码 [chr(i) for i in range(97,122)
    random_str = ''
    for i in range(16):
        random_str = random_str + str(random_list[random.randint(1, 16)])
    return random_str

def publish(req):
    return render_to_response('topic/publish.html')


def publishEdit(req):
    user_id = req.session["userid"]
    username =req.session['username']
    if req.method =="POST":
         title = req.POST.get("title",'') #文章内容
         content = req.POST.get("content",'') #文章内容
         tagArr = req.POST.getlist("tagsArr[]") # 文章标签
         userCategoryList = req.POST.getlist("userCategoryList[]") #文章所属个人分类
         existUserCategoryList = req.POST.getlist("existUserCategoryList[]")#文章勾选已存在的个人分类
         category = int(req.POST.get("category"))# 文章所属系统分类
         user_id = req.session["userid"]
         # 插入日志内容
         dao = DailyDao()
         create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         modified_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         daily_id = dao.addDaily(title,content,create_time,category,user_id,modified_time,click=0)
         # 存储文章标签
         for tag in tagArr:
             dao = UserTag()
             dao.addUserTag(user_id,daily_id,tag)

         # 存储个人分类
         for category_name in  userCategoryList:
             print(userCategoryList)
             dao = UserCategoryDao()
             flag = dao.getUserCategoryByName(user_id,category_name)
             if flag:
                 continue
             else:
                 dao = UserCategoryDao()
                 category_id = dao.addUserCategory(user_id, category_name,0)
                 dao = UserDailyCategoryDao()
                 dao.addUserDailyDetail(category_id,daily_id)

         #添加新的博客所属的分类
         for category_id in existUserCategoryList:
             category_id = int(category_id)
             print(userCategoryList)
             dao = UserDailyCategoryDao()
             # 判断该博客的分类是否已添加到USER_DAILY_DETAILS中，如果没有添加，则添加，如果已经添加，则不处理
             flag = dao.getUserDailyDetailById(category_id, daily_id)
             if flag:
                 continue
             else:
                 dao = UserDailyCategoryDao()
                 dao.addUserDailyDetail(category_id, daily_id)
         msg = {
             'status':200
         }
         return HttpResponse(json.dumps(msg), content_type="application/json")

    else:

        #查询分类
        category = CategoryDao()
        categoryList = category.getCategoryList()
        #查询个人分类
        user_category = UserCategoryDao()
        existUserCategory = user_category.getUserCategory(user_id)
        data ={
            'categoryList': categoryList,
            'existUserCategory':existUserCategory,
            'username': username
        }
        return render_to_response('topic/publish-edit.html',data)

def publishSuccess(req):
    if req.method =="POST":
        pass
    else:
        return render_to_response('topic/publish-success.html')
