from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from category.models import Category
from .models import Contributor, Dataset, ContributrFolder
from .forms import CreateDataset
import os
import zipfile
import shutil

def home(request):
    return render(request, 'home.html')



@login_required(redirect_field_name='next')
def upload(request, title):
    try:
        dataset_name = Dataset.objects.get(title=title)
        print()
    except:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        updatedImages = request.FILES.getlist('files[]')

        ty = ""
        ls = []
        if dataset_name.dataset_type == 'Image':
            for i in updatedImages:
                if i.name.split(".")[-1] in ['png', 'jpg', 'jpeg']:
                    ls.append(Contributor(username=request.user,dataset_name=dataset_name,file=i))
        elif dataset_name.dataset_type == 'Video':
            for i in updatedImages:
                if i.name.split(".")[-1] in ['mp4', 'wmv', 'avi', 'mkv']:
                    ls.append(Contributor(username=request.user, dataset_name=dataset_name, file=i))
        elif dataset_name.dataset_type == 'Audio':
            for i in updatedImages:
                if i.name.split(".")[-1] in ['pcm', 'wav', 'aiff', 'mp3']:
                    ls.append(Contributor(username=request.user, dataset_name=dataset_name, file=i))
        elif dataset_name.dataset_type == 'CSV':
            for i in updatedImages:
                if i.name.split(".")[-1] in ['csv', 'xlsx', 'xls', 'txt']:
                    ls.append(Contributor(username=request.user, dataset_name=dataset_name, file=i))


        yo = Contributor.objects.bulk_create(ls)
        user_is, created = ContributrFolder.objects.get_or_create(username = request.user)
        if created:
            user_is.file_count =  len(yo)
            user_is.save()
        else:
            user_is.file_count = str(len(yo)+int(user_is.file_count))
            user_is.save()

        return render(request, 'dataset/upload.html', {'text': 'uploaded', 'dataset':dataset_name})
    return render(request, 'dataset/upload.html', {'text':'Select Folder Upload Multiple Photos', 'dataset':dataset_name})

def all_dataset(request):
    all_datasets = Dataset.objects.all()
    cats = Category.objects.all()
    context = {'all':all_datasets, 'cats': cats}
    if len(all_datasets)==0:
        context = {'all':[{'title':'No Available'}]}
    return render(request, 'dataset/test_all.html', context)



@login_required(redirect_field_name='next')
def single(request, title):
    try:
        data = Dataset.objects.get(title = title)
    except:
        return HttpResponseRedirect('/')
<<<<<<< HEAD
    shutil.make_archive('../static/media/zip/%s'%(title), 'zip', '../static/media/datasets/%s'%(title))
=======
    try:
        shutil.make_archive('../static/media/zip/%s'%(title), 'zip', '../static/media/datasets/%s'%(title))
    except:
        pass
>>>>>>> 87e180d49143a67356ab4134095f986610e6832c
    return render(request, 'dataset/single.html', {'data':data})

@login_required(redirect_field_name='next')
def create_dataset(request):
    form = CreateDataset(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data['title']
        form.save(commit=False)
        form.instance.username = request.user
        form.save()
        return HttpResponseRedirect('/contribute/%s'%(title))
    return render(request, 'dataset/create.html',{'form':form})
