# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from datetime import datetime
import pytz

class DataModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    
    
class AS2_user(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    
    
class AS2_bucket_db(models.Model):
    bucket_name = models.CharField(max_length=100)
    # bucket_id = models.CharField(max_length=100)
    creation_date = models.DateTimeField()
    updation_date = models.DateTimeField(auto_now=True)
    data = models.ForeignKey(DataModel, on_delete=models.CASCADE)
    
class SignupData(models.Model):
    # user_id = models.TextField(max_length=500)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    
    
class  sessions(models.Model):
    user_id = models.CharField(max_length=500)
    active = models.BooleanField(default=False)





hai