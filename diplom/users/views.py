from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from users.forms import UserRegistrationForm, CustomUserCreationForm, ContactForm
from users.models import UserManager, User, UserProfileForm, Contact


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def superuser_register(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Superuser account created!')
            return redirect('login')
    else:
        form = SuperuserCreationForm()
    return render(request, 'registration/superuser_register.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register_user.html', {'form': form})


