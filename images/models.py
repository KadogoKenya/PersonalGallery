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
    editor = models.ForeignKey(Editor)
    editor = models.ForeignKey(Location)
    editor = models.ForeignKey(Category)
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =30)
    <label for="category">Choose a category for images:</label>
    <select name="category" id="category">
        <option value="Travel">Travel</option>
        <option value="Food & drinks">Food & drinks</option>
        <option value="Birthday">Birthday</option>
        <option value="Wedding">Wedding</option>
    </select>

    def __str__(self):
        return self.name
   
