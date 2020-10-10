from django.db import models
from django.db import models


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'location/')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =1000)
    
   
