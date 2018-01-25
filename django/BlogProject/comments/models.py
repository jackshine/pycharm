from django.db import models

# Create your models here.
class Comment(models.Model):
    commentid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    #被评论内容(文章的id)
    pdid = models.IntegerField()
    comment = models.CharField('评论内容', max_length=200)
    commenttime = models.DateTimeField('评论时间', auto_now_add=True)
    #用户类型标记,0：普通用户1：高级用户

    flag = models.IntegerField(default='0')
    nickname = models.CharField('昵称', max_length=50, null=True)