from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FreedomFighters(models.Model):
    name = models.CharField(max_length = 100, primary_key = True)
    DOB = models.DateField()
    DOD = models.DateField()
    POB = models.CharField(max_length = 100 )
    image = models.ImageField(upload_to = 'pp')
    biodata = models.TextField()

    def __str__(self):
        return self.name
    

