from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    message=models.TextField(max_length=600)
    
class Resume(models.Model):
    adminuploaded = models.FileField(upload_to='media')

