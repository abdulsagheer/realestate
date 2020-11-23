from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.core.validators import FileExtensionValidator
import os,uuid
# Create your models here.
def get_upload_path(instance,filename):
    ext=filename.split('.')[-1]
    filename="{}.{}".format(uuid.uuid4(),ext)
    return os.path.join('photos/%Y/%m/%d/',filename)



class Realtor(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to=get_upload_path,default='photos/%Y/%m/%d/',null=True,blank=True,validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    description=RichTextField(blank=True)
    phone=models.CharField(max_length=200)
    email=models.EmailField()
    is_mvp=models.BooleanField(default=False)
    hire_date=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name