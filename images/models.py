from django.db import models
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length =100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =100)
    

    def __str__(self):
        return self.name
   
class Image(models.Model):
    image = models.ImageField(upload_to = 'location/')
    name = models.CharField(max_length =100)
    description = models.TextField()

    author = models.CharField(max_length=30, default='admin')

    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location,on_delete=models.SET_NULL, null=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
