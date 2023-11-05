from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import Student, Avatar

# Create your views here.

# ================================================ Login ================================================

def login(request):
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        student = auth.authenticate(request, username=username, password=password)
        
        if student is not None:
            auth.login(request, student)
            return redirect('check_bandwidth')
        
        else:
            return redirect('login')
    
    return render(request, 'accounts/login.html')

# ===========================================   CHECK BANDWIDTH =========================================

def check_bandwidth(request):
    return render(request, "accounts/bandwidth.html")

# ================================================ Logout ================================================


def logout(request):
    auth.logout(request)
    return redirect('home')


# ================================================ Register ================================================


def register_username(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        
        request.session['username'] = username
        request.session['password'] = password
        request.session['confirm_password'] = confirm_password
        
        return redirect('register-age')
    
    return render(request, 'accounts/register-username.html')

def register_age(request):
    
    if request.method == 'POST':
        age = request.POST.get('age')
        
        request.session['age'] = age
        
        return redirect('register-avatar')
    
    return render(request, 'accounts/register-age.html')

def register_avatar(request):
    
    if request.method == 'POST':
        avatar = request.POST.get('avatar')
        
        print("\n\n\n\n", request.session['username'], "\n\n\n\n")
        
        new_student = Student(
            username = request.session['username'],
            age = request.session['age']
        )
        
        new_student.avatar = Avatar.objects.get(pk=avatar)
        
        new_student.set_password(request.session['password'])
        
        new_student.save()
        
        return redirect('login')
    
    parameters = {
        'avatars': Avatar.objects.all(),
    }
    
    return render(request, 'accounts/register-avatar.html', parameters)

def success(request):    
    
    parameters = {
        "student": Student.objects.get(username=request.session['username']),
    }
    
    return render(request, 'accounts/success.html', parameters)

