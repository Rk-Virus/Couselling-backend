from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    params = {'siteName':'Aksar','phoneNo':'+911234567890'}
    return render(request, 'index.html',params)

def about(request):
    return HttpResponse("this is about page")

def signup(request):
    return render(request, 'signUp.html')

def submission(request):
    usrName = request.POST.get('userName','default')
    print(usrName)
    return HttpResponse("Welcome "+usrName)

