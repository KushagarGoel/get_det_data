from django.shortcuts import render
from .forms import UserAddressForm
from .models import Editor
# Create your views here.

def yo(request):
    form = UserAddressForm(request.POST or None)
    obj = Editor.objects.all()
    if form.is_valid():
        form.save()
    return render(request,'article/yo.html',{})