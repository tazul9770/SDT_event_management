from django.shortcuts import render, redirect
from user.forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('register')
    return render(request, 'authentication/register.html', {'form':form})

def log_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'authentication/login.html', {'form':form})

def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
