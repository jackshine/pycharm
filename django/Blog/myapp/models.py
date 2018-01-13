from django.db import models

# Create your models here.
from  django.db import models

class Catagory(models.Model):
    name = models.CharField('名称',max_length=30)



class Tag(models.Model):
    name = models.CharField('名称',max_length=16)

class Blog(models.Model):
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('博客正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    catagory = models.ForeignKey('Catagory',  on_delete=models.CASCADE,verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')

class Comments(models.Model):
    blog = models.ForeignKey(Blog,  on_delete=models.CASCADE,verbose_name='博客')
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=240)
    created = models.DateTimeField('发布时间', auto_now_add=True)