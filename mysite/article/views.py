from django.shortcuts import render
from .forms import UserAddressForm
from .models import Editor
from datetime import datetime
# Create your views here.

def yo(request):
    form = UserAddressForm(request.POST or None)
    obj = Editor.objects.all()
    if form.is_valid():
        form = form.save(commit=False)
        form.username = request.user
        form.save()
        print(form.timestamp)

    return render(request,'article/yo.html',{'form':form, 'obj':obj})