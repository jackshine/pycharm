from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, HttpResponse,HttpResponseRedirect
from .forms import  *

def post_comment(req,post_pk):
    if req.method == "method":
        form = CommentForm(req.POST)
        if form.is_vaild():
            comment = form.save(commit=False)
    else:
        return HttpResponseRedirect('index.html')