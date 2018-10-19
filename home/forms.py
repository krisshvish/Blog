from django import forms
from django.contrib.auth.models import User
from home.models import UserProfileInfo

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'size':10,'class':'form-control form-control-sm','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','placeholder':'Password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-sm','placeholder':'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Last Name'}))

    class Meta():
        model = User
        fields = ('username','password','email','first_name','last_name')

class UserProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required=False,widget=forms.URLInput(attrs={'class':'form-control form-control-sm','placeholder':'Enter URL'}))
    profile_pic = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class':'form-control-file form-control-sm'}))

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio','profile_pic')
