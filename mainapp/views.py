from django.shortcuts import render
from mainapp.forms import UserYearBookForm,BlogForm
from mainapp.models import UserYearBook,BlogModel
from django.contrib.auth.models import User
# Create your views here.
def regbatchmate(request):
    form = UserYearBookForm()

    if request.method == 'POST':

        form = UserYearBookForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

    return render(request,"mainapp/registerbatchmate.html",{'form':form})

def alumniview(request):
    alum_list_user =  User.objects.order_by('first_name')
    alum_dict_user = {'alum_list_user':alum_list_user}
    alum_list_yearbook = UserYearBook.objects.order_by('user')
    alum_dict_yearbook = {'alum_list_yearbook':alum_list_yearbook}

    return render(request,"mainapp/alumnilist.html",context=alum_dict_user)


def myblogview(request):
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

    return render(request,"mainapp/myblog.html",{ 'form':form })

def mypostsview(request):
    return render(request,"mainapp/myposts.html")
