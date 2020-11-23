# Generated by Django 3.1.3 on 2020-11-23 05:24

import django.core.validators
from django.db import migrations, models
import listings.models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20201121_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(blank=True, default='photos/%Y/%m/%d/', null=True, upload_to=listings.models.get_upload_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_2',
            field=models.ImageField(blank=True, default='photos/%Y/%m/%d/', null=True, upload_to=listings.models.get_upload_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(blank=True, default='photos/%Y/%m/%d/', null=True, upload_to=listings.models.get_upload_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, default='photos/%Y/%m/%d/', null=True, upload_to=listings.models.get_upload_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, default='photos/%Y/%m/%d/', null=True, upload_to=listings.models.get_upload_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_6',
            field=models.ImageField(blank=True, default='photos/%Y/%m/%d/', null=True, upload_to=listings.models.get_upload_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(blank=True, default='photos/%Y/%m/%d/', null=True, upload_to=listings.models.get_upload_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]