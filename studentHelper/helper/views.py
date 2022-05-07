
from sre_constants import SUCCESS
from django.shortcuts import render
from helper import forms,models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Home page
def homePage(request):
    return render(request,'helper/home.html')

#username and password creation form
def UsernamePass(request):
    if request.method=='GET':
        UserPassForm=UserCreationForm()
        return render(request,'helper/UsernamePass.html',{'UserForm':UserPassForm})
    else:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            UserForm=forms.UserDataForm()
            return render(request,'helper/UserRegistration.html',{'UserForm':UserForm,'username':form.cleaned_data['username']})
        else:
            return render(request,'helper/UsernamePass.html',{'UserForm':form})     

# user registration Form
def UserRegister(request):
    form=forms.UserDataForm(request.POST)
    if form.is_valid():
        ob=User.objects.get(username=request.POST['username'])
        data=models.UserData()
        data.user=ob
        data.name=form.cleaned_data['name']
        data.type=form.cleaned_data['type']
        data.collage_name=form.cleaned_data['collage_name']
        data.email=form.cleaned_data['email']
        data.mobile=form.cleaned_data['mobile']
        data.save()
        messages.success(request,"User Registration SuccessFul !")
        return render(request,'helper/success.html')
    else:
        return render(request,'helper/UserRegistration.html',{'UserForm':form,'username':request.POST['username']})

    