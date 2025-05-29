from django.db import models

class Adminpanel(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    description=models.TextField()
    cover=models.ImageField(upload_to='covers/', blank=True,null=True)
