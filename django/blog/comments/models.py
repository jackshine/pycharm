from django.db import models
# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    #评论内容text
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    dailyid = models.ForeignKey('myblog.daily', on_delete=models.CASCADE)