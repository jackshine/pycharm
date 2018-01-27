from django.db import models
import json
# Create your models here.
class UserInfo(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField('用户名',max_length=20)
    password = models.CharField('密码',max_length=32)
    gender_choices = (
        (0, "男"),
        (1, "女"),
    )
    sex = models.IntegerField('性别',choices=gender_choices,default=0)
    regtime = models.DateTimeField('注册时间' )
    delflag_choices = (
        (0, "普通用户"),
        (1, "高级用户"),
    )
    delflag =models.IntegerField('用户类型标记',choices=delflag_choices,default=1)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Daily(models.Model):
    # 文章标题
    title = models.CharField('标题',max_length=70)
    # 文章正文，我们使用了 TextField。
    body = models.TextField('标题内容' )
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField(blank=True)
    # 摘要
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)







