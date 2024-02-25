from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from playground.models import SignupData, AS2_bucket_db,AS2_user, sessions, DataModel
from django.contrib.auth.hashers import make_password, check_password
from playground.pages import uuid
from django.contrib.auth.models import User
from datetime import date, datetime
# from file_name import function_name 
from views.py import get_user_data


def api_get_request(request, userid, bucketid):
    print('hello')
    