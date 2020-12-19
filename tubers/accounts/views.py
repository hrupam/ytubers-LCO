from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

        else:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in')
            return redirect('home')

    if not request.user.is_authenticated:
        return render(request, 'accounts/login.html')
    else:
        return redirect('home')


def logout_user(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exixts')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exixts')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registered successfully')
                auth.login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')

    return render(request, 'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        new_password = request.POST['password']
        request.user.set_password(new_password)
        request.user.save()
        return redirect('login')
    return render(request, 'accounts/change_password.html')
