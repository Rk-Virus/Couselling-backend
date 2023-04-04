from django.shortcuts import render,HttpResponse
from .models import Contact, User

# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
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

def submission(request):
    formType = request.POST.get('formType','default')
    print(formType)
    if formType == "contact" :
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        print(name,email)
        contact = Contact(name=name,email=email)
        contact.save()
    # if formType == "signup" :
    #     name = request.POST.get('name','')
    #     email = request.POST.get('email','')
    #     passwd = request.POST.get('pass','')
    #     dob = request.POST.get('dob','')

    #     print(name,email)
    #     user = User(name=name,email=email, password=passwd, dob=dob)
    #     user.save()
    
    return HttpResponse(f"{formType}  form submited. Thanks!")

