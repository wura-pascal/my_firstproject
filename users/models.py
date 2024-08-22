from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.TextField("first_name", max_length=50)
    last_name = models.TextField("last_name", max_length=50)
    email = models.EmailField(name= "email")
    gender = models.TextField()
    password = models.TextField()

class Wura(models.Model):
    full_name = models.TextField("full_name", max_length=20)
    class_grade = models.TextField("class_grade", max_length=50)
    age = models.TextField("age", max_length=10)
    name_school = models.TextField("name_school", max_length=30)