
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



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        login_user = authenticate(username='user', password='user_password_attempted')

        if login_user:
            print('Login successful')
        else:
            print('Invalid username or password')
    else:
        # GET request, render the login page
        return render(request, 'login.html')
    