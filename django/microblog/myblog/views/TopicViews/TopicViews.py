from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404, render



def get_index(req):
    if req.method == 'POST':
        return render_to_response('topic/index.html')
    else:
        print(req.session['username'])
        return render_to_response('topic/index.html',{'username':req.session['username']})






