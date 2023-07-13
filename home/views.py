from django.shortcuts import render,HttpResponse, redirect
from .models import Contact, Appointment
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

from django_nextjs.render import render_nextjs_page_sync


# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    messages.info(request, "Welcome to Aksar ;)")
    params = {'siteName':'Aksar','phoneNo':'+911234567890'}
    return render(request, 'home/index.html',params)
    # return render_nextjs_page_sync(request)

def contact(request):
    # return render(request, 'home/contact.html')
    print("/contact running")
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        print(name,email, subject, message)
        contact = Contact(name=name,email=email, subject=subject, message=message)
        contact.save()
        # return redirect('/')
        return HttpResponse("Message Sent!")


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname','')
        email = request.POST.get('email','')
        passwd = request.POST.get('password','')

        # creating the user 
        user = User.objects.create_user(name,email,passwd)
        user.save()
        messages.success(request, "Your Aksar account has been created successfully!")
        return redirect('/login')
    return render(request, 'home/signUp.html')

def login(request):
    if request.method == 'POST':
        name = request.POST.get('uname','')
        passwd = request.POST.get('password','')

        # authenticating 
        user = authenticate(username=name, password=passwd)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome back {name}")
            return redirect('/')
        else:
            messages.error(request, "Username or password incorrect!")
            return redirect('/login')
    
    return render(request, 'home/login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, "Logged out!")
    return redirect('/')


def appointment(request):
    if request.method == 'POST':
        # print(request)
        # print(request.POST.get('finantial_status',''))

        # fetching form data 
        type_of_therapy = request.POST.get('type_of_therapy','')
        sex = request.POST.get('sex','')
        age = request.POST.get('age','')
        gender = request.POST.get('gender','')
        relationship_status = request.POST.get('relationship_status','')
        religious_status = request.POST.get('religious_status','').lower() in ['true', 'yes']
        religion = request.POST.get('religion','')
        spritual_status = request.POST.get('spritual_status','').lower() in ['true', 'yes']
        therapy_status = request.POST.get('therapy_status','').lower() in ['true', 'yes']
        reason_for_therapy = request.POST.getlist('reason_for_therapy','')
        expectation_from_counseller = request.POST.getlist('expectation_from_counseller','')
        anxiety_status = request.POST.get('anxiety_status','').lower() in ['true', 'yes']
        medication_status = request.POST.get('medication_status','').lower() in ['true', 'yes']
        chronic_pain_status = request.POST.get('chronic_pain_status','').lower() in ['true', 'yes']
        finantial_status = request.POST.get('finantial_status','')
        resources = request.POST.getlist('resources','')
        communication_mode = request.POST.get('communication_mode','')
        preferences = request.POST.get('preferences','')
        country = request.POST.get('country','')
        language = request.POST.get('language','')
        occupation_status = request.POST.getlist('occupation_status','')
        # print(chronic_pain_status)
        appointment = Appointment(type_of_therapy=type_of_therapy, sex=sex, age=age, gender=gender, relationship_status=relationship_status,is_religious=religious_status,religious_status=religion,is_spritual=spritual_status,taken_therapy=therapy_status,therapy_reason=reason_for_therapy,expectations=expectation_from_counseller, is_anxious=anxiety_status,taking_medications=medication_status, having_chronic_pain=chronic_pain_status, financial_status=finantial_status, resources=resources, communication_mode=communication_mode, preferences=preferences, country=country, language=language, mark_that_apply=occupation_status)

        #saving appointment
        appointment.save()

        #redirecting
        return redirect("/signup")
    
    return render(request, 'home/appointment.html')


