

from django.shortcuts import render
from helper import forms,models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
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

# userLoginForm
def UserLogin(request):
    if request.method=='GET':
        form=AuthenticationForm()
        return render(request,'helper/loginForm.html',{'form':form})
    else:
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,'helper/me.html',{'data':username})
            else:
                form=AuthenticationForm()
                messages.warning(request,'You are not registered ,plese registered first.')
                return render(request,'helper/loginForm.html',{'form':form})
        else:
            return render(request,'helper/loginForm.html',{'form':form})

#USerLogout
def UserLogout(request):
    logout(request)
    return render(request,'helper/home.html')

#Notes 
def shareNotes(request):
    form=forms.NotesSubmission()
    return render(request,'helper/shareNotes.html',{'form':form})
def submitNotes(request):
    form=forms.NotesSubmission(request.POST,request.FILES)
    obj=models.Notes()
    obj.subject=request.POST['subject']
    obj.notes_pdf=request.FILES['notes_pdf']
    obj.user=request.user
    obj.save()
    messages.success(request,'Notes Submisson Successful , Thanks for Your Contribution.')
    return render(request,'helper/shareNotes.html',{'form':form})
#find Notes
def findNotes(request):
    return render(request,'helper/findNotes.html')
def returnNotes(request):
    Subject=request.GET['subject']
    ans=models.Notes.objects.filter(subject=Subject)
    if len(ans)==0:
        messages.success(request,'OOps ! Notes are not Available.')
    return render(request,'helper/findNotes.html',{'ans':ans})

#sell books
def TakeBooks(request):
    form=forms.BookForm()
    img=models.Books.objects.filter(user__username=request.user.username)
    if len(img)==0:
        img=None
    return render(request,'helper/me.html',{'form':form,'img':img,'data':request.user.username})
def SaveBook(request):
    form=forms.BookForm(request.POST,request.FILES)
    if form.is_valid:
        obj=models.Books()
        obj.book_name=request.POST['book_name']
        obj.book_img=request.FILES['book_img']
        obj.author=request.POST['author']
        obj.price=request.POST['price']
        obj.edition=request.POST['edition']
        obj.user=request.user
        obj.save()
    img=models.Books.objects.filter(user__username=request.user.username)
    if len(img)==0:
        img=None
    messages.success(request,'Book Detail Submitted Successfully!')
    return render(request,'helper/me.html',{'form':form,'img':img,'data':request.user.username})
