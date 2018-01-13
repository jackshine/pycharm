from django.shortcuts import render,render_to_response
# Create your views here.
from .models import *
from .forms import CommentForm
from django.http import Http404
def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created')
    print(blogs)
    return render_to_response('blog-list.html',{'blogs':blogs})

def get_details(request,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        print(blog)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            form.objects.create(**cleaned_data)
    ctx = {
        'blog':blog,
        'comments':Comments.objects.all().order_by('-created'),
        'form':form
    }
    return render_to_response('blog-details.html',ctx)