# Generated by Django 3.1.3 on 2020-11-21 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sq_ft',
            field=models.IntegerField(max_length=220),
        ),
    ]