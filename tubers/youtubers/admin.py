from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html


# Register your models here.

class YoutuberAdmin(admin.ModelAdmin):

    def image(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))

    list_display = ['id', 'name', 'image', 'subs_count', 'is_featured']
    list_filter = ['category', 'camera_type', 'city']
    search_fields = ['name', 'camera_type']
    list_display_links = ['id', 'name']
    list_editable = ['is_featured']


admin.site.register(Youtuber, YoutuberAdmin)
