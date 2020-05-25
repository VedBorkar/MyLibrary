from django.db import models

# Create your models here.

class Book(models.Model):
    
    title = models.CharField(max_length=100, unique="True")
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    age_grp = models.CharField(max_length=100)
    is_available = models.BooleanField(default="True")

    def __str__(self):
        return self.title

class Wishlist(models.Model):

    user_id = models.IntegerField()
    book_id = models.IntegerField()
