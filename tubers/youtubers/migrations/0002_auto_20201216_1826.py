# Generated by Django 3.1.4 on 2020-12-16 12:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('Nikon', 'Nikon'), ('Canon', 'Canon'), ('Fujifilm', 'Fujifilm'), ('Panasonic', 'Panasonic'), ('Kodak', 'Kodak'), ('Sony', 'Sony')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('Coding', 'Coding'), ('Gadget_review', 'Gadget_review'), ('Vlogs', 'Vlogs'), ('Comedy', 'Comedy'), ('Gaming', 'Gaming'), ('Cooking', 'Cooking'), ('Music', 'Music'), ('Lifestyle', 'Lifestyle')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('Solo', 'Solo'), ('Small', 'Small'), ('Large', 'Large')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]