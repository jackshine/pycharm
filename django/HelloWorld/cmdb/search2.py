from django.shortcuts import render
from django.views.decorators import csrf

#接收post请求数据
def search_post(request):
    print('123')
    ctx = {}
    print(request.POST)
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request,'post.html',ctx)
