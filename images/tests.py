from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.imagetest= Image(id=1,name = 'image', description ='try this sample test image', location=self.location,category=self.category)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.imagetest,Image))