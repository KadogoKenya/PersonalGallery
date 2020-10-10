from django.db import models
from django.db import models


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

class Image(models.Model):
    image = models.ImageField(upload_to = 'location/')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =1000)
    
class location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class category(models.Model):
    name = models.CharField(max_length =255)

    def __str__(self):
        return self.name
   
