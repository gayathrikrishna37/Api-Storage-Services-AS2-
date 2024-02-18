from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Define the signup_list globally
signup_list = []



@login_required(login_url='home')
def HomePage(request):
    return render (request,'home.html')

def signup_view(request):
    if request.method == 'POST':
        # Process signup form submission
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Store signup data in a dictionary
        signup_data = {
            'username': username,
            'email': email,
            'password': password
        }
        print(signup_data)
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
        user = authenticate(username=username, password=password)

        if user is not None:
            # User is authenticated
            login(request, user)
            # Redirect to a success page
            return redirect('dashboard')  # Change 'dashboard' to your desired URL
        else:
            # Authentication failed
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # GET request, render the login page
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