from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from .models import CustomUser
from .decorators import admin_required, editor_required

from .forms import CustomUserCreationForm


def is_admin(user):
    return user.role == CustomUser.Role.ADMIN


@admin_required
def admin_panel(request):
    return HttpResponse("You are now in  Admin Panel")


@editor_required
def editor_pane(request):
    return HttpResponse("You are now in  Editor Panel")


def author_panel(request):
    return redirect(reverse("core:index"))


def register_page(request):
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect(reverse("accounts:login"))
        else:
            # Form is invalid, print errors
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"{field}: {error}")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


def create_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("accounts:login"))
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/create_account.html", {"form": form})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == CustomUser.Role.ADMIN:
                return redirect(reverse("accounts:admin_panel"))
            elif user.role == CustomUser.Role.EDITOR:
                return HttpResponse("Editor Panel")
            elif user.role == CustomUser.Role.AUTHOR:
                return HttpResponse("Author Panel")
            else:
                return render("core:index")
        else:
            messages.error(request, "Incorrect username or password")

    return render(request, "accounts/login.html")


def index(request):
    return render(request, "accounts/base.html")


def logout_user(request):
    logout(request)
    return redirect(reverse("core:index"))
