from django.db import models

# Create your models here.

class Newsletter(models.Model):
    title = models.TextField()
    sub_title = models.TextField()
    body = models.TextField()
