from django import forms
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(forms.Form):
    username = forms.CharField(label='login')
    first_name = forms.CharField(label='First name:')
    last_name = forms.CharField(label='Last name:')
    e_mail = forms.EmailField(label='Email:')
    password = forms.CharField(label='Password:',
                               widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password:',
                                       widget=forms.PasswordInput)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput)
