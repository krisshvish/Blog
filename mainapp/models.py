from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class UserYearBook(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact_no = models.BigIntegerField(editable=True)
    address = models.TextField(max_length=250,editable=True)
    hobbies = models.TextField(max_length=250,blank=True,editable=True)
    dob = models.DateField()

    def __str__(self):
        return self.user.first_name


class BlogModel(models.Model):
    title = models.TextField(max_length=70,editable=True,blank=True)
    content = models.TextField(max_length=250,editable=True,blank=False)
    created_time = models.DateTimeField(default=timezone.now,editable=False)

    def __str__(self):
        return self.title
