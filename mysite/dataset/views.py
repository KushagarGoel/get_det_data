from django.shortcuts import render

from .models import Contributor, Dataset




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
        Contributor.objects.bulk_create(ls)
        print(updatedImages, request.FILES)

        return render(request, 'dataset/upload.html', {'text': 'uploaded'})
    return render(request, 'dataset/upload.html', {'text':'Select Folder Upload Multiple Photos'})

