from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import UserData

import json



def post_user_data(request):
    if request.method == 'POST':
        try:
            post_data = json.loads(request.body)
            userid = post_data.get('userid')
            bucketid = post_data.get('bucketid')
            data = post_data.get('data')

            if userid is None or bucketid is None or data is None:
                return JsonResponse({'error': 'userid, bucketid, and data fields are required'}, status=400)

            UserData.objects.create(userid=userid, bucketid=bucketid, data=data)
            return JsonResponse({'success': 'Data posted successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def homepage(request):

    return render(request, 'crm/index.html')




def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save()
            user_id = user.id

# Now you can use user_id as needed
            print("User ID:", user_id)

            return redirect("my-login")


    context = {'registerform':form}

    return render(request, 'crm/register.html', context=context)



def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)
                user_Credentials(request)

                return redirect("dashboard")


    context = {'loginform':form}

    return render(request, 'crm/my-login.html', context=context)


def user_logout(request):

    auth.logout(request)

    return redirect("")



@login_required(login_url="my-login")
def dashboard(request):

    return render(request, 'crm/dashboard.html')

def bucket_view(request):
    return render(request, 'crm/bucket.html')



def user_Credentials(request):
    user_id = request.user.id
    username = request.user.username
    email = request.user.email
    print(user_id)
    user_credentials = {
        'userid': user_id,
        'username': username,
        'email': email
    }
    
    # Store user credentials in the session
    request.session['user_credentials'] = user_credentials
    
@csrf_exempt
def post_user_data(request, userid, bucketid):
    if request.method == 'POST':
        try:

            post_data = json.loads(request.body)
            userid = userid
            bucketid = bucketid
            data = post_data.get('data')
            
            if userid is None or bucketid is None or data is None:
                
                return JsonResponse({'error': 'userid, bucketid, and data fields are required'}, status=400)
            user_credentials = request.session.get('user_credentials')
            if userid == user_Credentials.get('user_id'):
                UserData.objects.create(userid=userid, bucketid=bucketid, data=data)
                return JsonResponse({'success': 'Data posted successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)