from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to = 'img')
    name=models.CharField(max_length=200, null=True)
    slug=models.SlugField(unique=True)
    price=models.CharField(max_length=200, null=True)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
