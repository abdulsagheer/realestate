from django.db import models
from ckeditor.fields import RichTextField
from realtors.models import Realtor
from datetime import datetime
import os,uuid
from django.core.validators import FileExtensionValidator
# Create your models here.

def get_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext)
    return os.path.join('photos/%Y/%m/%d/', filename)

class Listing(models.Model):
    realtors=models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=220)
    address=models.CharField(max_length=220)
    city=models.CharField(max_length=220)
    state=models.CharField(max_length=220)
    zip_code=models.CharField(max_length=20)
    description=RichTextField(blank=True)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2,decimal_places=1)
    garage=models.IntegerField(default=0)
    sq_ft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=5,decimal_places=1)
    photo_main=models.ImageField(upload_to=get_upload_path,default='photos/%Y/%m/%d/',null=True,blank=True,validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    photo_1=models.ImageField(upload_to=get_upload_path,default='photos/%Y/%m/%d/',null=True,blank=True,validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    photo_2=models.ImageField(upload_to=get_upload_path,default='photos/%Y/%m/%d/',null=True,blank=True,validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    photo_3=models.ImageField(upload_to=get_upload_path,default='photos/%Y/%m/%d/',null=True,blank=True,validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    photo_4=models.ImageField(upload_to=get_upload_path,default='photos/%Y/%m/%d/',null=True,blank=True,validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    photo_5=models.ImageField(upload_to=get_upload_path,default='photos/%Y/%m/%d/',null=True,blank=True,validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    photo_6=models.ImageField(upload_to=get_upload_path,default='photos/%Y/%m/%d/',null=True,blank=True,validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title
