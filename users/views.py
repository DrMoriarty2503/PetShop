from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import logout



from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')  # Замените 'home' на URL вашей главной страницы
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт успешно создан')
            return redirect('login')  # Замените 'home' на URL вашей главной страницы
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)



def logout_view(request):
    logout(request)
    return redirect('login')  # Замените 'login' на URL вашей страницы входа


