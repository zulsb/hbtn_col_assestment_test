from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from app.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


def register(request):

    if request.user.is_authenticated:
        return redirect('search')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Successful registration!!!')
                return redirect('search')

        return render(request, "register.html", {
            'title': 'Register',
            'register_form': register_form
        })


def login_page(request):

    if request.user.is_authenticated:
        return redirect('search')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('search')
            else:
                messages.warning(request, 'Failed registration :(')

        return render(request, "login.html", {
            'title': 'Login'
        })


def index(request):
    return render(request, "layout.html")


def search(request):
    return render(request, "search.html", {
        'title': 'Search'
    })


def users(request):
    return render(request, "users.html", {
        'title': 'Users'
    })


def orders(request):
    return render(request, "orders.html", {
        'title': 'Orders'
    })

def logout_user(request):
    logout(request)
    return redirect('login')
