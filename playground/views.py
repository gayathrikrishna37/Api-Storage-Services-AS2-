from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from playground.models import SignupData
from django.contrib.auth.hashers import make_password, check_password
from playground.pages import uuid
from django.contrib.auth.models import User
# Define the signup_list globally
signup_list = []



@login_required(login_url='home')
def HomePage(request):
    return render (request,'home.html')

def signup_view(request):
    if request.method == 'POST':
        # Process signup form submission
        usrname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Hash the password
        hashed_password = make_password(password)
        User.objects.create(username=usrname,password=hashed_password)

        # Store signup data in a dictionary
        signup_data = SignupData.objects.create(
            user_id = 212,
            username=usrname,
            email=email,
            password=hashed_password
        )

        
        # Append signup data to the global signup_list
        signup_list.append(signup_data)

        # Redirect to a success page after signup
        return redirect('signup_success')
    else:
        return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        login_user = authenticate(username='user', password='user_password_attempted')

        if login_user is not None:
            # User is authenticated
            print('Authentication successful')
            # Redirect to a success page
            return redirect('dashboard')  # Change 'dashboard' to your desired URL
        else:
            # Authentication failed
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # GET request, render the login page
        print('Authentication failed')
        return render(request, 'login.html')
    
    
def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('login')
    
    
    
def my_view(request):
    data = {
        'message': 'project is working properly'
    }
    return HttpResponse(JsonResponse(data))




# Starting of api part 

@api_view(['GET'])
def getData(request):
    return render(request,'home.html')