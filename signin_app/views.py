from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth,User
from django.urls import reverse

# Create your views here.
def render_home(request):
    return render(request,"index.html")

def render_signin(request):
    if(request.method=='POST'):
        fname=request.POST['fname']
        sname=request.POST['sname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        data=User.objects.create_user(first_name=fname,last_name=sname,email=email,username=username,password=password)
        data.save()
    return render(request,"in.html")
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
            return HttpResponseRedirect(reverse("admin_dashboard"))
        else:
            return render(request,"signin.html")
def admin_dashboard(request):
    return render(request,"in.html")
def perform_logout(request):
    logout(request)
    return render(request,"index.html")
