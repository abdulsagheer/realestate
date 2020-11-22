from django.contrib import admin
from .models import Realtor
from django.utils.html import format_html
# Register your models here.from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius:10px;"/>'.format(object.photo.url))
    thumbnail.short_description='Photo'

    list_display = ('id','thumbnail', 'name', 'email', 'hire_date','is_mvp')
    list_editable=('is_mvp',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)