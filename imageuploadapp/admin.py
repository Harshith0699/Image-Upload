from django.contrib import admin

# Register your models here.
from . models import img

@admin.register(img)
class ImageAdmin(admin.ModelAdmin):
    list=['id','photo','display']