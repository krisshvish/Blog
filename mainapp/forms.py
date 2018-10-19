from django.contrib.auth.models import User
from home.models import UserProfileInfo
from mainapp.models import UserYearBook,BlogModel
from django import forms

class UserYearBookForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Permanent Address'}))
    hobbies = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Hobbies'}))
    contact_no = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','placeholder':'Username'}))
    dob = forms.CharField(widget=forms.SelectDateWidget(attrs={'class':'form-control form-control-sm'}))

    class Meta():
        model = UserYearBook
        exclude = ('user',)


class BlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-sm','placeholder':'Content...'}))

    class Meta():
        model = BlogModel
        exclude = ('created_time',)
