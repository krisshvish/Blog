from django.shortcuts import render
from home.forms import UserForm,UserProfileInfoForm
from home.models import UserProfileInfo
from mainapp.forms import BlogForm
from mainapp.models import BlogModel
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
@login_required
def index(request):

    post = BlogModel.objects.order_by('-created_time')[:10]

    return render(request,"home/main.html",{'post':post})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True
                return HttpResponseRedirect(reverse('user_login'))

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form  = UserProfileInfoForm()

    return render(request,'home/registration.html',{'user_form':user_form,
    'profile_form':profile_form,'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('usernamefromtemplate')
        password = request.POST.get('passwordfromtemplate')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home:main'))

        else:
            print("Login Failed!")
            print("Username:{} and password:{}".format(username,password))
            return HttpResponseRedirect(reverse('user_login'))

    else:
        return render(request,'home/login.html')

@login_required
def user_logout(request):
    logout(request,user)
    return render(request,'home/login.html')
