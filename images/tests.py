from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.

class ImageTestClass(TestCase):


     # Creating a new tag and saving it
        self.location = Location('Desktop')
        self.location.save_location()


    # Set up method
    def setUp(self):
        self.imagetest= Image(id=1,image_name = 'image',image_author="james", image_description ='try this sample test image', location=self.location,category=self.category)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.imagetest,Image))

    def test_save_image(self):
        self.imagetest.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_save_image(self):
        self.imagetest.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


    def test_save_image(self):
        self.imagetest.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_save_image(self):
        self.imagetest.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_save_image(self):
        self.imagetest.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_save_image(self):
        self.imagetest.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)