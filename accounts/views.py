from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you login successfully', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'your user and pass is wrong', 'alert')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'you logout', 'success')
    return redirect('shop:home')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['fullname'], cd['password'])
            user.save()
            messages.success(request, 'you register success fully', 'success')
            return redirect('shop:home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


