from sre_constants import BRANCH
from turtle import mode
from django.db import models
from django.urls import clear_script_prefix

# Create your models here.
class Admin_Singup(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=70)
    Password=models.CharField(max_length=15)

    class Meta:
        db_table="Admin"

class Books(models.Model):
    Book_name=models.CharField(max_length=150)
    Branch=models.CharField(max_length=50)
    No_of_books=models.CharField(max_length=10)
    class Meta:
        db_table="Books"