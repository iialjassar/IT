from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
# Create your views here.


def login_view(request:HttpRequest):

    if request.method =="POST":

        user = authenticate(username = request.POST["username"],password=request.POST["password"])

        if user:
            login(request,user)
            return redirect('main:home_view')
        

    return render(request,"user/login.html")
