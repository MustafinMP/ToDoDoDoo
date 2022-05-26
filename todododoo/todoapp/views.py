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
    if request.user.is_authenticated:
        return HttpResponsePermanentRedirect('/')

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            username = request.POST['username']
            try:
                if User.objects.get_by_natural_key(username):
                    register_form.add_error('username', 'Name is ')
                    return render(request, 'register.html', {'form': register_form})
            except:
                password = request.POST['password']
                confirm_password = request.POST['confirm_password']
                if password != confirm_password:
                    register_form.add_error('confirm_password', "Password isn't ")
                    return render(request, 'register.html', {'form': register_form})

                e_mail = request.POST['e_mail']
                user = User.objects.create_user('username', e_mail, password)
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.save()
                login(request, user)
                return HttpResponsePermanentRedirect('/')

    else:
        register_form = RegisterForm()
        return render(request, 'register.html', {'form': register_form})


def login_(request):
    if request.user.is_authenticated:
        return HttpResponsePermanentRedirect('/')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            login_form.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponsePermanentRedirect('/')

            else:
                login_form.add_error('password', 'Wrong password')
                return render(request, 'login.html', {'form': login_form})
        else:
            return HttpResponsePermanentRedirect('/')
    else:
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})
