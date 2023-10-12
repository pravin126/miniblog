from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post

# Home
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

#ABOUT
def about(request):
    return render(request,'blog/about.html')

#Contact
def contact(request):
    return render(request,'blog/contact.html') 

#dashbord

def dashbord(request):
    if request.user.is_authenticated:
     posts=Post.objects.all()
     return render(request,'blog/dashbord.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/')
    
#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#signup
def user_signup(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congartlation!! You have Become an Author')
            form.save()
    else:
         form =SignUpForm()
    return render(request,'blog/signup.html', {'form':form})

#login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form =LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Succesfully!!')
                    return HttpResponseRedirect('/dashbord/')
        else:
            form=LoginForm()
        return render(request,'blog/login.html', {'form':form})
    else:
       return HttpResponseRedirect('/dashbord/')
