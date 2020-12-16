# Generated by Django 3.1.4 on 2020-12-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_auto_20201216_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('nikon', 'Nikon'), ('canon', 'Canon'), ('fujifilm', 'Fujifilm'), ('panasonic', 'Panasonic'), ('kodak', 'Kodak'), ('sony', 'Sony')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('coding', 'Coding'), ('gadget_review', 'Gadget Review'), ('vlogs', 'Vlogs'), ('comedy', 'Comedy'), ('gaming', 'Gaming'), ('cooking', 'Cooking'), ('music', 'Music'), ('lifestyle', 'Lifestyle')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'Solo'), ('small', 'Small'), ('large', 'Large')], max_length=255),
        ),
    ]
