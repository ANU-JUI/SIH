from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import auth,User
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def render_home(request):
    return render(request,"index.html")
def reset(request):
    return render(request,"reset_password.html")
def render_signin(request):
    if(request.method=='POST'):
        fname=request.POST['fname']
        sname=request.POST['sname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
       # user_id=User.objects.get(email='email')
        try:
            if( User.objects.filter(email=email).exists()==False):
                if(password==password1 ):
                    data=User.objects.create_user(first_name=fname,last_name=sname,email=email,username=username,password=password)
                    data.save()
                    User.is_active=True
                    return render(request,"in.html")
                else:
                    return HttpResponse("PASSWORD DOES NOT MATCH")
            else:
              return HttpResponse("ACCOUNT WITH THIS EMAIL ALREADY EXISTS")  
        except:
            return HttpResponse("USERNAME ALREADY EXISTS!!")
    return render(request,"in.Html")
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def ino(request):
    return render(request,"in.html")
def login_page(request):
    return render(request,"login.html")
def signin_page(request):
    return render(request,"signin.html")
def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        Username=request.POST.get("username")
        Password=request.POST.get("password")
        user_id=authenticate(request,username=Username,password=Password)
        if user_id is not None:
            login(request,user_id)
            return render(request,"in.html")
        else:
            return render(request,"signin.html")
def admin_dashboard(request):
    return render(request,"in.html")
def perform_logout(request):
    logout(request)
    return render(request,"index.html")
def perform_reset(request):
    if(request.method=='POST'):
        try:
            user=User.objects.get(username="username")
            user.set_password('new_password')
            user.save()
        except User.DoesNotExist:
            return HttpResponse("Invalid username") 
    return render(request,"login.html")
