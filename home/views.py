from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import *
import uuid

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def contact(request):
    print("/contact running")
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        print(name,email, subject, message)
        contact = Contact(name=name,email=email, subject=subject, message=message)
        contact.save()
        return HttpResponse("Message Sent!")


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname','')
        email = request.POST.get('email','')
        passwd = request.POST.get('password','')

        # checking if user already exists
        if User.objects.filter(username=name).first():
            messages.warning(request, "User name already exists!")
            return redirect("signup")
        if User.objects.filter(email=email).first():
            messages.warning(request, "Email already exists!")
            return redirect("signup")

        # creating the user 
        user = User.objects.create_user(name,email, passwd)

        # creating profile 
        token = str(uuid.uuid4())
        profile = Profile.objects.create(name=name, email=email, user=user, auth_token=token)
        profile.save()

        send_verification_mail(email, token)

        return redirect(f'/verify/{email}')
    return render(request, 'home/signUp.html')

def verify(request,email):
    return render(request, 'home/verify.html',{'email':email})

def login(request):
    if request.method == 'POST':
        name = request.POST.get('uname','')
        passwd = request.POST.get('password','')

        # quering for user 
        user = User.objects.filter(username=name).first()

        if user is not None:
            profile = Profile.objects.filter(user=user).first()
            if profile.is_verified:
                # authenticating 
                authuser = authenticate(username=name, password=passwd)
                if authuser is not None:
                    auth_login(request, user)
                    return redirect('/appointment2')
                else:
                    messages.error(request, "Username or password incorrect!")
                    return redirect('/login')
            else:
                messages.warning(request, "Email is not verified, please check your mail or spam to verify!")
                return redirect('/login')
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



def appointment2(request):
    if request.method == 'POST':
        counseller_experience = request.POST.getlist('counseller_experience','')
        Additional_focus_areas = request.POST.getlist('Additional_focus_areas','')
        additional_details = request.POST.get('additional_details','')

        print(counseller_experience, additional_details, Additional_focus_areas)
        appointment2 = Appointment2(counseller_experience=counseller_experience,Additional_focus_areas=Additional_focus_areas, additional_details=additional_details)
        appointment2.save()
        return render(request, 'home/submit.html')
    return render(request, 'home/appointment2.html')


def send_verification_mail(email, token):
    subject = "Aksar | Verify your email address"
    message = f'Verify your email through the given link to complete your aksar account registration : http://localhost:8000/verifyemail/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)



def verifyemail(request,token):
    try:
        verifiedProfile = Profile.objects.filter(auth_token=token).first()
        # print(verifiedProfile)
        if verifiedProfile:
            if verifiedProfile.is_verified:
                messages.success(request,"Email is already verified!")
                return redirect('/login')

            verifiedProfile.is_verified = True
            verifiedProfile.save()
            messages.success(request, "Your account has been verified!")
            return redirect('/login')
        else:
            messages.success(request, "Sorry, email verification failed...")
            redirect('/signup')
    except Exception as e:
        print(e)