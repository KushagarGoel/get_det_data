from django.shortcuts import render

# Create your views here.

def yo(request):
    return render(request,'article/yo',{})