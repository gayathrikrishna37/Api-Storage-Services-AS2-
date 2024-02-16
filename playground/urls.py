from django.contrib import admin
from django.urls import path
from .views import signup_view, login_view,dashboard_view, my_view
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('test/', views.my_view, name='test'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]