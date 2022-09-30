from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class Caradmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width = "40" style="border-radius: 50px" />',format(object.car_photo.url))
    
    thumbnail.short_description="car image"

    list_display=('id','thumbnail','car_title','city','color','model','body_styles','fuel_type','is_featured')
    list_display_links=('id','thumbnail','car_title')
    list_editable=('is_featured',)
    search_fields=('id','car_title','city','model','body_styles')
    list_filter=('city','model','body_styles')

admin.site.register(Car,Caradmin)


