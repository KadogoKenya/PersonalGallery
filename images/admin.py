from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Image,Category,Location


class ImageAdmin(admin.ModelAdmin):
    # filter_horizontal =('category',)

    admin.site.register(Image)
    admin.site.register(Category)
    admin.site.register(Location)