from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    phone_no = models.CharField(max_length=12)
    email = models.EmailField(max_length=254) 

    def __str__(self):
        return self.name

   