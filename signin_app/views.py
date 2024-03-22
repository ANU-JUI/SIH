from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import auth,User
from django.http import JsonResponse
import cv2
import base64
#video_processor = VideoProcessor(source='car.mp4', cy1=222, cy2=368, distance_in_meters=10, thresh_speed=10, email='kushwahaatish1@gmail.com')
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
              return HttpResponse("ACCOUNT WITH THIS EMAIL ALREADY EXISTS . TRY SIGNING IN OR CREATE ACCOUNT WITH DIFFERENT EMAIL-ID")  
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
            return HttpResponse("Invalid username or password !!")
def admin_dashboard(request):
    return render(request,"in.html")
def perform_logout(request):
    logout(request)
    return render(request,"index.html")
def perform_reset(request):
    if(request.method=='POST'):
        try:
            W=request.POST.get("username")
            user=User.objects.get(email=W)
            P=request.POST.get("new_password")
            user.set_password(P)
            user.save()
        except User.DoesNotExist:
            return HttpResponse("Account does not exist with the email") 
    return render(request,"login.html")
def upload_video(request):
    if request.method=='GET':
        return render (request,'upload.html')
def process_video(request):
    if request.method=='POST' and request.FILES['input_video']:
        input_video=request.FILES['input_video']
        cap=cv2.VideoCapture(input_video)
        while cap.isOpened():
            ret,frame=cap.read()
            if not ret:
                break
            processed_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            buffer=cv2.imencode('.jpg',processed_frame)
            encoded_frame=base64.b64encode(buffer).decode('utf-8')
            return JsonResponse({'processed_frame':encoded_frame})
        return render(request,'process.html')
    
    

        