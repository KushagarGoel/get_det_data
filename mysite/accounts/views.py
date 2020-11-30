from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, HttpResponseRedirect,Http404
from django.urls import reverse
from .forms import LoginForm, RegistrationForm
import re
from .models import EmailConfirmed, UserDetails
from django.contrib import messages
from dataset.models import ContributrFolder
# Create your views here.


def logout_view(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return HttpResponseRedirect('%s'%(reverse("auth_login")))


def login_view(request):
    form = LoginForm(request.POST or None)
    btn = "Login"
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            messages.success(request, "Successfully Logged in")
            try:
                request.GET['next']
                return HttpResponseRedirect(request.GET['next'])
            except:
                return HttpResponseRedirect('/')
    context = {"form": form}
    return render(request, "form.html",context)



def registration_view(request):
    form = RegistrationForm(request.POST or None)
    btn = "Register"
    if form.is_valid():
        form.save()
        messages.success(request,"Registered Successfully, Please confirm your email")
        return HttpResponseRedirect("/")
    context = {"form": form, 'btn':btn}
    return render(request, "form2.html",context)

SHA1_RE = re.compile('^[0-9a-f]{40}$')

def activation_view(request, activation_key):
    if SHA1_RE.search(activation_key):
        try:
            user_confirmed = EmailConfirmed.objects.get(activation_key = activation_key)
        except EmailConfirmed.DoesNotExist:
            messages.error(request, "There Was some error with your request")
            return HttpResponseRedirect('/')
            user_confirmed = None
        if user_confirmed is not None and not user_confirmed.confirmed:
            msg = "Ativation Complete"
            user_confirmed.confirmed = True
            user_confirmed.save()
            messages.success(request, "Successfully Confirmed")
        elif user_confirmed is not None and user_confirmed.confirmed:
            msg = "Already Confirmed"
            messages.warning(request, "Already Confirmed")
        else:
            msg = ""
        context = {'msg':msg}
        return render(request, "accounts/activation_template.html", context)
    else:
        raise Http404

def show_account(request):
    user = request.user
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        phn = request.POST['phn']
        li = request.POST['li']
        git = request.POST['git']
        user_details = UserDetails.objects.get(username=user.id)
        if fname is not None:
            user_details.first_name = fname
        if lname is not None:
            user_details.last_name = lname
        if phn is not None:
            user_details.phone = phn
        if li is not None:
            user_details.linkedin_link = li
        if git is not None:
            user_details.github_link = git
        user_details.save()

        ls = [1, 2, 3, 4, 5]
        rating = int(user_details.rating)
        cont = ContributrFolder.objects.get(username=user.id)
        context = {'user_details': user_details, 'user': user, 'cont': cont, 'rating': rating, 'ls': ls}
        return render(request, 'accounts/show_acc.html', context)
    try:
        user_details = UserDetails.objects.get(username = user.id)

    except:
        user_details = UserDetails.objects.create(username = user)
    ls = [1,2,3,4,5]
    rating = int(user_details.rating)
    cont = ContributrFolder.objects.get(username = user.id)
    context = {'user_details':user_details, 'user':user, 'cont':cont, 'rating':rating, 'ls':ls}
    return render(request,'accounts/show_acc.html',context)