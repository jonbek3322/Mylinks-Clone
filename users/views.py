from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import custom_login_form, RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(password)
            user = User.objects.create(username = username)
            user.set_password(password)
            user.save()
            return redirect('/login/custom-login')
    return render(request, 'registration/create_user.html', {'form': form})


def login_view(request):
    form = custom_login_form

    if request.method == 'POST':
        form = custom_login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    print(request.user)
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


@login_required
def check_user(request):
    user = request.user
    return render(request, 'check-user.html', {'user': user})
