from django.db import models

# Create your models here.


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    # %Y,%m can also be added
    button_link = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='media/slider')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255, blank=True)
    linkedin_link = models.CharField(max_length=255, blank=True)
    ytube_link = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d/")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
