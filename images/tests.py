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

    def test_update_image(self):
        self.imagetest.save_image()
        self.imagetest.update_image(self.imagetest.id,'images/test.jpg')
        imageschange = Image.objects.filter(image='images/test.jpg')
        self.assertTrue(len(imageschange) > 0)

    def test_delete_image(self):
        self.imagetest.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)


    def test_get_image_by_id(self):
        imagesfind=self.imagetest.get_image_by_id(self.imagetest.id)
        images = Image.objects.filter(id=self.imagetest.id)
        self.assertTrue(imagesfind,image)

    def test_search_image_by_category(self):
        self.imagetest.save_image()
        imagesFind = self.imagetest.search_image_by_category(category)
        self.assertTrue(len(imagesFind) == 1)

    def test_filter_by_location(self):
        self.imagetest.save_image()
        imagesfind=self.imagetest.filter_by_location(location='desktop')
        self.assertTrue(len(imagesfind) > 0)

    