from django.contrib import admin
from .models import Image, Category, Location

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
  filter_horizontal=('Category')
  filter_horizontal=('Location')

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)
