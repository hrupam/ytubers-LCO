# Generated by Django 3.1.4 on 2020-12-15 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='fb_link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin_link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
