import os
from django.shortcuts import render,redirect
from app.models import Registeration
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User,auth
from django.contrib.auth import login
from urllib.parse import urlencode


def register(request):
    return render(request,"register.html")

def add_details(request): 
    if(request.method=='POST'):
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        ag=request.POST['age']
        pwd=request.POST['password']
        cpwd=request.POST['cp']
        ph=request.POST['phone']
        ad=request.POST['address']
        mail=request.POST['email']
        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=pwd,email=mail)
                user.save()
                u=User.objects.get(id=user.id)
                reg=Registeration(age=ag,phnoenumber=ph,user=u,address=ad)
                reg.save()
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('/')
                
                
        else:
            messages.info(request,'Incorrect Password')
            return redirect('/')
        


def loginpage(request):
    return render (request,'loginpage.html')


def log(request):
    if request.method=='POST':
        username=request.POST['usname']
        password=request.POST['passd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_authenticated:
                if user.is_staff:
                    print('ok')
                    login(request,user)
                    request.session['user'] = user.username
                    return redirect('adminmod')
                else:
                    login(request,user)
                    auth.login(request,user)
                    request.session['user'] = user.username
                    return redirect('usermod',id=user.id)
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('loginpage')
    return render(request,'signuppage.html')

def usermod(request,id):
    user=User.objects.get(id=id)
    if 'user' in request.session:
        return render (request,'usermod.html',{'user':user})
    else:
        query_params = {'error': 'access_denied'}
        url = '{}?{}'.format(reverse('loginpage'), urlencode(query_params))
        return redirect(url)
    
def adminmod(request):
    if request.user.is_staff:
        return render(request,'adminmod.html')
    else:
        query_params = {'error': 'access_denied'}
        url = '{}?{}'.format(reverse('loginpage'), urlencode(query_params))
        return redirect(url)

def lgout(request):
    auth.logout(request)
    return redirect ('loginpage')