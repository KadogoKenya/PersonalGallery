from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.

class LocationTestClass(TestCase):

    def setUp(self):
        self.location = Location(name='desktop')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)


    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='mainpage')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):

        self.location = Location(name='desktop')
        self.location.save_location()

        self.category = Category(name='mainpage')
        self.category.save_category()

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
        self.imagetest.update_image(self.imagetest.id,'1')
        imageschange = Image.objects.filter(image='images/1')
        self.assertTrue(len(imageschange) > 0)

    def test_delete_image(self):
        self.imagetest.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)


    def test_get_image_by_id(self):
        today_images=self.imagetest.get_image_by_id(self.imagetest.id)
        images = Image.objects.filter(id=self.imagetest.id)
        self.assertTrue(today_images,image)

    def test_search_image_by_category(self):
        self.imagetest.save_image()
        imagesFind = self.imagetest.search_image_by_category(category)
        self.assertTrue(len(imagesFind) == 1)

    def test_filter_by_location(self):
        self.imagetest.save_image()
        imagesfind=self.imagetest.filter_by_location(location='desktop')
        self.assertTrue(len(imagesfind) > 1)


    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_get_images_today(self):
        today_images = Image.todays_images()
        self.assertTrue(len(today_images)>0)

    def test_get_images_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        images_by_date = Image.days_images(date)
        self.assertTrue(len(images_by_date) == 0)

        

    
    