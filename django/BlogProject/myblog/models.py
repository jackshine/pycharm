from django.db import models

# Create your models here.
class UserInfo(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField('用户名',max_length=20)
    nickname = models.CharField('昵称',max_length=20)
    blogname = models.CharField('博客名',max_length=30)
    blogsign = models.CharField('博客个性签名',max_length=50, null=True)
    password = models.CharField('密码',max_length=20)
    lastlogin = models.DateTimeField('最后登录时间', auto_now=True, null=True)
    name = models.CharField(max_length=16, null=True)
    gender_choices = (
        (0, "男"),
        (1, "女"),
    )
    sex = models.IntegerField('性别',choices=gender_choices,default=0)
    province = models.CharField('省份',max_length=20, null=True)
    city = models.CharField('城市',max_length=20, null=True)
    address = models.CharField('地址',max_length=100, null=True)
    birthday = models.CharField('生日',max_length=16, null=True)
    email = models.EmailField('邮箱',max_length=30, null=True)
    tel = models.CharField('手机号',max_length=20, null=True)
    regtime = models.DateTimeField('注册时间', auto_now_add=True)
    profile = models.CharField('简介',max_length=200, null=True)
    delflag_choices = (
        (0, "普通用户"),
        (1, "高级用户"),
    )
    delflag =models.IntegerField('用户类型标记',choices=delflag_choices,default=1)

class AdminInfo(models.Model):
    adminid = models.AutoField(primary_key=True)
    adminname = models.CharField('管理员', max_length=20)
    password = models.CharField('密码', max_length=20)
    name = models.CharField('姓名', max_length=20, null=True)
    tel = models.CharField('联系电话', max_length=20, null=True)
    regtime = models.DateTimeField('注册时间', auto_now_add=True)

class Daily(models.Model):
    dailyid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    dailyname = models.CharField('日志名', max_length=20)
    daily  = models.TextField('日志内容',max_length=100)
    postingdate = models.DateTimeField('发布时间', auto_now_add=True)
    modifytime =  models.DateTimeField('修改时间', auto_now=True, null=True)
    keyword = models.CharField('关键字', max_length=20, null=True)
    tab = models.CharField('标签', max_length=20, null=True)

class PhotoInfo(models.Model):
    photoid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    albumid = models.IntegerField()
    photoname = models.CharField('图片名', max_length=30)
    photoaddress = models.CharField('图片地址', max_length=50)
    photodepict = models.CharField('图片描述', max_length=50)
    uploadtime =  models.DateTimeField('发布时间', auto_now=True)
    keyword = models.CharField('关键字', max_length=20,null=True)

class PhotoAlbum(models.Model):
    albumid =  models.AutoField(primary_key=True)
    userid = models.IntegerField()
    albumname =  models.CharField('相册名', max_length=30)
    albumdepict = models.CharField('相册描述', max_length=50, null=True)
    createtime = models.DateTimeField('建立时间', auto_now_add=True)
    keyword = models.CharField('关键字', max_length=20, null=True)

class Comment(models.Model):
    commentid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    pdid = models.IntegerField()
    comment = models.CharField('评论内容', max_length=200)
    commenttime = models.DateTimeField('评论时间', auto_now_add=True)
    flag = models.IntegerField()
    nickname = models.CharField('昵称', max_length=50, null=True)

class Message(models.Model):
    messageid = models.AutoField(primary_key=True)
    blogid = models.IntegerField()
    userid = models.IntegerField()
    message = models.CharField('留言内容', max_length=200)
    messagetime = models.DateTimeField('留言时间', auto_now_add=True)
    messagename = models.CharField('留言姓名', max_length=50, null=True)

