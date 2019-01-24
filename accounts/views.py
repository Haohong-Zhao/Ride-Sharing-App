from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        print('A USER LOGIN!!')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html') 

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # validations
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is being used')
                redirect('register')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'You are now registered and can login')
                redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

