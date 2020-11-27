from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from .forms import ArticleForm, CommentForm
from .models import Editor, Comment
from datetime import datetime
# Create your views here.
@login_required(redirect_field_name='next')
def create_article(request):
    form = ArticleForm(request.POST or None)
    obj = Editor.objects.all()


    if form.is_valid():
        form.instance.username = request.user
        form.save()


    return render(request,'article/yo.html',{'form':form, 'obj':obj})

def view_article(request):
    obj = Editor.objects.all()
    return render(request, 'article/view.html',{'obj':obj})

@login_required(redirect_field_name='next')
def single(request, title):
    try:
        obj = Editor.objects.get(title = title)
    except:
        return HttpResponseRedirect('/')
    form = CommentForm(request.POST or None)

    if form.is_valid():
        form.save(commit=False)
        form.instance.username = request.user
        form.instance.article_id = obj
        form.save()
        form = CommentForm()

    obj_com = Comment.objects.filter(article_id = obj)
    return render(request, 'article/single.html', {'obj': obj, 'form':form, 'obj_com':obj_com})
