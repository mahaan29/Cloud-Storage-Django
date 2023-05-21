from django.db import models

# Create your models here.

class customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class audiodata(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    browse = models.FileField(default='')

class photodata(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    browse = models.FileField(default='')

class videodata(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    browse = models.FileField(default='')

class filedata(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    browse = models.FileField(default='')
