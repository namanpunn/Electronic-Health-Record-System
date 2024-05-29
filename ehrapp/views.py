from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Topic, Doctor, Individual
from .forms import DoctorForm
from django.db.models import Q

def home(request):
    return render(request, 'home.html', {})

def user_login(request):
    page = login
    context = {'page':page}
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist.')

    return render(request, 'ehrapp/login.html', {'page':page})

def user_logout(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('request')
        else:
            messages.error(request,'An Error occured during Registration')

    return render(request, 'ehrapp/signup.html', {'form':form})

@login_required(login_url='login')
def DoctorProfile(request, pk):
    doctor = Doctor.objects.get(id=pk)
    context = {'doctor': doctor}
    return render(request, 'ehrapp/doctor.html', context)

@login_required(login_url='login')
def IndividualProfile(request,name):
    individual = Individual.objects.get(name=name)
    context = {'individual':individual}
    return render(request,'ehrapp/individual.html',context)


def notexist(request):
    return render(request, 'ehrapp/notexist.html', {})

def search(request):
    query = request.GET.get('Individual')
    if query:
        allPosts = Individual.objects.filter(title__icontains=query)
    else:
        allPosts = []  # Empty queryset if no query provided
    context = {'allPosts': allPosts}
    return render(request, 'ehrapp/search.html', context)