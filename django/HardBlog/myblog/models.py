from django.db import models

# Create your models here.
class UserInfo(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField('用户名',max_length=20)
    password = models.CharField('密码',max_length=32)
    regtime = models.DateTimeField('注册时间' )
    delflag_choices = (
        (0, "普通用户"),
        (1, "高级用户"),
    )
    delflag =models.IntegerField('用户类型标记',choices=delflag_choices,default=1)