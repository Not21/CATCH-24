from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
     college=models.CharField(max_length=50,null=True,blank=True)
     age=models.IntegerField(null=True,blank=True)

class Studentinfomodel(models.Model):
    regno=models.IntegerField()
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    gender=models.CharField(max_length=20,null=True,blank=True)
    department=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    year=models.CharField(max_length=20,null=True,blank=True)
    mobile=models.CharField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=10,null=True,blank=True)
    hostel_or_dayscholar=models.CharField(max_length=20,null=True,blank=True)
    quota=models.CharField(max_length=20,null=True,blank=True)



    def __str__(self):
        return self.name
    

    