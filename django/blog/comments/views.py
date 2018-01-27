from django.shortcuts import render

# Create your views here.

from .forms import  *
from myblog.models import Daily
from django.shortcuts import render_to_response, HttpResponse,get_object_or_404, HttpResponseRedirect


def daily_comment(req,dailyid):
    daily = get_object_or_404(Daily,id=dailyid)
    comment_list = Comment.objects.filter(dailyid=dailyid)
    print(dailyid)
    if req.method == "POST":
        form = CommentForm(req.POST)
        comment = form.save(commit=False)
        comment.dailyid = daily
        comment.save()
        return HttpResponseRedirect('/myblog/daily/?dailyid='+dailyid)
    else:
        form = CommentForm()
        context = {
            'daily':daily,
            'form':form,
            'comment_list':comment_list
        }
        return render_to_response('detail.html',context=context)
    return redirect(daily)