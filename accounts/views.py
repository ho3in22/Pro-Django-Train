from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms
from django.urls import reverse


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "نام کاربری"
        })
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "رمز عبور"
        })
    )

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "نام کاربری"
        })
    )

    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "رمز عبور"
        })
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "تکرار رمز عبور"
        })
    )


# Create your views here.
def login_view(request):

    if request.user.is_authenticated :
        return redirect('/')
    
    if request.method == 'POST' :
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect('/') 

    if request.user.is_authenticated :
        msg = f'user is authenticated as {request.user.username}'
    else :
        msg = 'user is not authenticated'
    form = LoginForm()
    context = {'msg' : msg, 'form' : form}
    return render(request, 'accounts/login.html', context=context)


@login_required
def logout_view(request):
    # if request.user.is_authenticated :
    logout(request=request)
    return redirect('/') 


def signup_view(request):
    if request.user.is_authenticated :
        return redirect('/') 
    if request.method == "POST" :
        form = SignupForm(data=request.POST)
        if form.is_valid() :
            form.save()
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"{field}: {error}")

    form = SignupForm()
    context = {'form' : form}
    return render(request, 'accounts/signup.html', context=context)