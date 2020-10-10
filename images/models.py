from django.db import models
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length =100)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =100)

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name
   
class Image(models.Model):
    image = models.ImageField(upload_to = 'location/')
    image_name = models.CharField(max_length =100)
    image_description = models.TextField()

    image_author = models.CharField(max_length=30, default='admin')

    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location,on_delete=models.SET_NULL, null=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()