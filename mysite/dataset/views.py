from django.shortcuts import render, HttpResponseRedirect

from .models import Contributor, Dataset, ContributrFolder




def home(request):
    return render(request, 'home.html')




def upload(request):
    if request.method == "POST":
        updatedImages = request.FILES.getlist('files[]')
        dataset_name = Dataset.objects.all()[0] #abhi yahi hai

        ls = []
        for i in updatedImages:
            if i.name.split(".")[-1] in ['png', 'jpg', 'jpeg']:
                ls.append(Contributor(username=request.user,dataset_name=dataset_name,file=i))

        yo = Contributor.objects.bulk_create(ls)
        user_is, created = ContributrFolder.objects.get_or_create(username = request.user)
        if created:
            user_is.file_count =  len(yo)
            user_is.save()
        else:
            user_is.file_count = str(len(yo)+int(user_is.file_count))
            user_is.save()

        return render(request, 'dataset/upload.html', {'text': 'uploaded'})
    return render(request, 'dataset/upload.html', {'text':'Select Folder Upload Multiple Photos'})

def all_dataset(request):
    all_datasets = Dataset.objects.all()
    context = {'all':all_datasets}
    return render(request, 'dataset/all_dataset.html', context)

def single(request, title):
    try:
        data = Dataset.objects.get(title = title)
    except:
        return HttpResponseRedirect('/')
    return render(request, 'dataset/single.html', {'data':data})