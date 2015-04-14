from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'ui/login.html')


@login_required(login_url='/')
def home(request):
    return render(request, 'ui/home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')