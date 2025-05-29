# Adminpanel/models.py
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class OperatingSystem(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    release_date = models.DateField()

class ServerLog(models.Model):
    log_entry = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
