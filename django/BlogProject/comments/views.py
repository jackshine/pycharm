from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, HttpResponse,get_object_or_404, HttpResponseRedirect
from .forms import  *
from myblog.models import Daily

def daily_comment(req,daily_id):
    daily = get_object_or_404(Daily,dailyid=daily_id)
    comment_list = Comment.objects.filter(pdid=daily_id)
    print(daily_id)
    if req.method == "POST":
        form = CommentForm(req.POST)
        print(form)
        comment = form.save(commit=False)
        comment.pdid = daily_id
        comment.save()
        form_a = CommentForm()
        context = {
            'daily': daily,
            'form': form_a,
            'comment_list': comment_list
        }
        return render_to_response('detail.html', context=context)
    else:
        form = CommentForm()
        context = {
            'daily':daily,
            'form':form,
            'comment_list':comment_list
        }
        return render_to_response('detail.html',context=context)
    return redirect(daily)