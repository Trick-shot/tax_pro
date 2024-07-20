from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 


from django.contrib import admin

from core.models import User
from .models import Client
from .models import admin
from .forms import ClientCreationForm, ClientLoginForm


def index(request):
    return render(request)

def register_client(request):
    template_name = 'client/register.html'
    
    if request.method == 'POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_login')
        
    else:
        form = ClientCreationForm()
    return render(request, template_name, {'form': form})    
        

def client_login(request):
    template_name = 'client/login.html'
    if request.method == 'POST':
        form = ClientLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password=form.cleaned_data['password']
            client = authenticate(request, email=email, password=password)
            if client:
                login(request, client)
                return redirect('home')
            else:
                form.add_error(None, "Invalid email address or password.")
            
    else:
        form = ClientLoginForm()
    return render(request, template_name, {'form': form})


def client_logout(request):
    logout(request)
    return redirect('client_login')