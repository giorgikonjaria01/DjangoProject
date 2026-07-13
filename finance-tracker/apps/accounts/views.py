from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .models import User


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Account created successfully"
            )

            return redirect("/")

    else:
        form = RegisterForm()


    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            messages.success(
                request,
                "Logged in successfully"
            )

            return redirect("/")

    else:
        form = AuthenticationForm()


    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )


def logout_view(request):
    logout(request)
    return redirect("login")