from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth import authenticate, login

def index(request):
    # if request.user.is_authenticated:
    #     return  # TODO redirect to calendar page
    return render(request, 'index.html')


def calendar(request):
    return render(request, 'calendar.html')


def task(request):
    return render(request, 'task.html')


def register(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return  # TODO: redirect to main page
    #     else:
    #         return render(request, 'pages/register.html', {'form': form, 'valid': False})
    # else:
    #     form = UserCreationForm()
    #     return render(request, 'pages/register.html', {'form': form, 'valid': True})
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST['username']
            e_mail = request.POST['e_mail']
            password = request.POST['password']
            user = User.objects.create_user(username, e_mail, password)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            login(request, user)
            return HttpResponsePermanentRedirect('/')
    else:
        register_form = RegisterForm()
        return render(request, 'register.html', {'form': register_form})
