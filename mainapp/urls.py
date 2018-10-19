from mainapp import views
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('registerbatchmate/',views.regbatchmate,name="regbatchmate"),
    path('alumni/',views.alumniview,name="alumni"),
    path('myblog/',views.myblogview,name="myblog"),
    path('myposts/',views.mypostsview,name="myposts"),

]
