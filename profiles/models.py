from django.db import models
from author.models import Profile 

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    author = models.OneToOneField(Profile,on_delete=models.CASCADE,default=None)


    def __str__(self):
        return self.name
