from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharFiels(max_length=200)
    content = models.TextField()
    author = models.TextFiels()
    category = models.ManyToManyField(Category) #ekta post multiple category er modhe thakte pare ekta category er modhe multiple oost thakte pare
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    
    


