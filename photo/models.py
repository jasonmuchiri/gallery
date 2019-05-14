from django.db import models

# Create your models here.
class Category(models.Model):
  category = models.TextField()

class Location(models.Model):
  location = models.TextField()  

class Image(models.Model):
  image = models.ImageField(upload_to = 'images/')
  image_name = models.CharField(max_length=60)
  image_description = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  category = models.ManyToManyField(Category)
  location = models.ForeignKey(Location)