from django.urls import path
from home import views

app_name = 'home'

urlpatterns=[
    path('main/',views.index,name="main"),
    path('register/',views.register,name="register"),
]
