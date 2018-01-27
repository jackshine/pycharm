from myblog.models import Daily,Category
from django import template
register = template.Library()
@register.simple_tag
def get_recent_dailys(num=5):
    return Daily.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives(num=5):
   return Daily.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    print(Category.objects.all())
    return Category.objects.all()