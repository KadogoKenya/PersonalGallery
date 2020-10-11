from django.db import models
from django.db import models
# import datetime as dt



class Location(models.Model):
    name = models.CharField(max_length =100)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)


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

    @classmethod
    def get_image_by_id(cls,id):
        images = cls.objects.filter(id = id)
        return images

    @classmethod
    def search_image_by_category(cls,category):
        images = cls.objects.filter(category=category)
        return images

    @classmethod
    def filter_by_location(cls):
        images = cls.objects.filter(location=location)
        return images

    @classmethod
    def update_image(cls,location,id):
        images = cls.objects.update(id=id)
        return images

    @classmethod
    def todays_images(cls):
        # today = dt.date.today()
        images = cls.objects.filter()
        return images

    
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_name__icontains=search_term)
        return images