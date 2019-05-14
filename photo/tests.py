from django.test import TestCase
from .models import Category, Location, Image
import datetime as dt

# Create your tests here.

class ImageTestClass(TestCase):
  def setUp(self):
    self.earth = Image(image_name='Earth', image_description='A breath taking landscape')

  def test_instance(self):
    self.assertTrue(isinstance(self.earth, Image))

  def test_save_instance(self):
    self.earth.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)

  def test_delete_instance(self):
    self.earth.save_image()
    self.earth.del_image()
    images = Image.objects.all()
    self.assertTrue(len(images) == 0)

  def test_get_images(self):
    self.earth.save_image()
    images = Image.get_image(1)
    self.assertTrue(len(images)>0)

  def test_get_all_images(self):
    self.earth.save_image()
    images = Image.all_images()
    self.assertTrue(len(images)>0)

  def tearDown(self):
    Image.objects.all().delete()
    

class CategoryTestClasss(TestCase):
  def setUp(self):
    self.landscape = Category(category='landscape')

  def test_instance(self):
    self.assertTrue(isinstance(self.landscape, Category))

  def test_save_instance(self):
    self.landscape.save_category()
    cats = Category.objects.all()
    self.assertTrue(len(cats)>0)

  def test_delete_instance(self):
    self.landscape.save_category()
    self.landscape.del_category()
    cats = Category.objects.all()
    self.assertTrue(len(cats) == 0)

