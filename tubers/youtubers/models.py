from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.


class Youtuber(models.Model):

    crew_choices = [
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
    ]
    camera_choices = [
        ('nikon', 'nikon'),
        ('canon', 'canon'),
        ('fujifilm', 'fujifilm'),
        ('panasonic', 'panasonic'),
        ('kodak', 'kodak'),
        ('sony', 'sony'),
    ]
    category_choices = [
        ('coding', 'coding'),
        ('gadget_review', 'gadget_review'),
        ('vlogs', 'vlogs'),
        ('comedy', 'comedy'),
        ('gaming', 'gaming'),
        ('cooking', 'cooking'),
        ('music', 'music'),
        ('lifestyle', 'lifestyle'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/youtubers/%Y/%m/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices, max_length=255)
    camera_type = models.CharField(choices=camera_choices, max_length=255)
    subs_count = models.IntegerField()
    category = models.CharField(choices=category_choices, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
