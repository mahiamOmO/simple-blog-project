from categories.models import Category
from author.models import Author
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.TextField()
    category = models.ManyToManyField(Category)  # ekta post multiple category er modhe thakte pare
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
