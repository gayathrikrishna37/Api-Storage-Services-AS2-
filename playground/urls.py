from django.contrib import admin
from django.urls import path
from .views import signup_view, login_view, my_view,getData
from django.views.generic import TemplateView

from . import views

urlpatterns =[   
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('test/', views.my_view, name='test'),
    path('post/user/')
    path('', views.getData),
    path('api/user/<int:userid>/bucket/<int:bucketid>/', get_user_data, name='get_user_data'),
]

# i edited this code 