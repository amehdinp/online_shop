from django.shortcuts import render


def user_login(request):
    return render(request, 'accounts/user_login.html')
