import sys
from django.core.checks import messages
from django.shortcuts import render, redirect
from httplib2 import Response
from .models import Registeration
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import YouToob
from urllib.parse import urlparse,parse_qs

 
# Create your views here.

#video_id = "-aQMjByEeo8"

def Home(request):
    return render(request,'home.html')

def Registration(request):
    if request.method=="POST":
        name = request.POST["Name"]
        email = request.POST["Email"]
        phone = request.POST["phone"]
        password = request.POST["Password"]
        gender = request.POST["Gender"]
        try:
            usr = User.objects.create_user(name,email,password)
            usr.save()
            record = Registeration(Name=name,Email=email,Mobile=phone,Password=password,Gender=gender)
            record.save()
            return redirect(Home)
        except:
            messages.info(request, 'Username already exist')
    return render(request,'Registration.html')


def Login(request):
    if request.method=="POST":
        loginname = request.POST["name"]  
        loginemail = request.POST['email']
        loginpassword = request.POST["Password"]  
        user = authenticate(username=loginname, email=loginemail, password=loginpassword)
        if user is not None:
            login(request,user)
            if request.GET.get('next', None):
                return redirect(request.GET['next']) 
            return redirect(analyser)
            
        else:
            return redirect(Home)         
    return render(request,'login.html')

@login_required(login_url='/login/')
def analyser(request):
    Response = "This is comment"
    Translated_Response = "This is translated comment"
    if request.method=="POST":
        vid_url = request.POST["url"]
        url_data = urlparse(vid_url)
        query = parse_qs(url_data.query)
        video = query["v"][0]
        Response = YouToob.video_comments(video)
        comments = '\n\n'.join([(comment) for comment in Response])
        Translated_Response = YouToob.translatebaazi(comments)
        Response = comments
    return render(request,'main.html', {'comments': f'{Response}','translated_data':Translated_Response})




# @login_required(login_url='/login/')
# def Translate(request):
#     TransResponse = "This is translated comment comment"
#     if request.method=="POST":
#         vid_url = request.POST["url"]
#         url_data = urlparse(vid_url)
#         query = parse_qs(url_data.query)
#         video = query["v"][0]
#         Comment = YouToob.video_comments(video)
#         Comment = '\n\n'.join(Comment)
#         TransResponse = YouToob.translatebaazi(Comment)
#     return render(request,'main.html', {'translated_data': f'{TransResponse}'})


@login_required()
def signout(request):
    logout(request)
    return redirect(Home)
    

def FAQ(request):
    return render(request,'FAQ.html')