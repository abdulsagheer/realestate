from django.contrib import admin
from .models import Listing
from django.utils.html import format_html
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:10px;"/>'.format(object.photo_main.url))
    thumbnail.short_description='Building Image'
    list_display=('id','thumbnail','title','is_published','price','list_date','realtors')
    list_display_links=('id','title')
    list_editable=('is_published',)
    list_filter=('realtors','title','state','list_date')
    search_fields=('title','realtors','price','state','city','address','zipcode')
    list_per_page=25



admin.site.register(Listing,ListingAdmin)