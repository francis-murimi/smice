from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('binary','Binary'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    location = models.CharField(max_length=100,default='Kutus',help_text='Nearest Town')
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default='male')
    
    def __str__(self):
        return self.user.username

class Topitem(models.Model):
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='topitem/%Y/%m/%d',blank=True)
    
    def __str__(self):
        return self.name