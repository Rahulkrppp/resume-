from django.contrib import auth
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from .models import Education,skills,profile
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    if request.user.is_authenticated:
       person= request.user
       edu= Education.objects.filter(user=person)
       pro= profile.objects.get(user=person) 
       skill= skills.objects.filter(user=person)
       context={'person':person,'edu':edu,'pro':pro,'skill':skill}
    return render(request,"index.html",context)

    
def Login(request):
    
    if request.method=='POST':
        Username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=Username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request,'login.html')