from django.urls import path

from . import views

urlpatterns = [

    path('', views.homepage, name=""),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('user-logout', views.user_logout, name="user-logout"),
    
    path('bucket/', views.bucket_view, name='bucket-page'),
    
    path('api/user/<int:userid>/bucket/<int:bucketid>/', views.post_user_data, name='post_user_data'),
    
]










