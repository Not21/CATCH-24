from django.shortcuts import render,redirect
from.models import *
from.forms import Studentinfomodelform
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request,'index.html')


def Signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        passowrd2=request.POST['password2']
        if password1==passowrd2:
            try:
                user=User.objects.create_user(username=username,password=password1)
            except Exception as e:
                raise ValidationError("username already exists")
        
        else:
            raise ValidationError("password 1 and passoword 2 are not match")
        return redirect('index')
    return render(request,'signup.html')



def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('shows')
    return render(request,'login.html')


def Logout(request):
    logout(request)
    return render(request,'index.html')



@login_required(login_url='/Login')
def shows(request):
    data=Studentinfomodel.objects.all()
    return render(request,'Studshow.html',{'data':data})

def save(request):
    if request.method=='POST':
        data=Studentinfomodelform(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/shows')
    
    form=Studentinfomodelform()
    return render(request,'studsave.html',{'form':form})

def update(request,id):
    data=Studentinfomodel.objects.get(id=id)
    form=Studentinfomodelform(instance=data)

    if request.method=='POST':
        form=Studentinfomodelform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/shows')
    
    return render(request,'studsave.html',{'form':form})


def delete(request,id):
    obj=Studentinfomodel.objects.get(id=id)
    obj.delete()
    return redirect('/shows')