from django.shortcuts import render,HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    messages.info(request, "Welcome to Aksar ;)")
    params = {'siteName':'Aksar','phoneNo':'+911234567890'}
    return render(request, 'home/index.html',params)

def about(request):
    return render(request, 'home/about.html')
    # return HttpResponse("this is about page")

def contact(request):
    return render(request, 'home/contact.html')
    # return HttpResponse("this is contact page")

def signup(request):
    return render(request, 'home/signUp.html')

def login(request):
    return render(request, 'home/login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, "Logged out!")
    return redirect('/')

def submission(request):
    # for submitting on the same page 
    if request.method == 'POST':
        formType = request.POST.get('formType','default')
        print(formType)
        if formType == "contact" :
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            print(name,email)
            contact = Contact(name=name,email=email)
            contact.save()
        if formType == "signup" :
            name = request.POST.get('uname','')
            email = request.POST.get('email','')
            passwd = request.POST.get('password','')

            # creating the user 
            user = User.objects.create_user(name,email,passwd)
            user.save()
            messages.success(request, "Your Aksar account has been created successfully!")
            return redirect('/')
        
        if formType == "login" :
            name = request.POST.get('uname','')
            passwd = request.POST.get('pass','')

            # authenticating 
            user = authenticate(username=name, password=passwd)

            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome back {name}")
                return redirect('/')
            else:
                messages.error(request, "Username or password incorrect!")
                return redirect('/login')
        
    return HttpResponse(f"404 page not found!")

