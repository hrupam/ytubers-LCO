from django.contrib import admin
from django.utils.html import format_html
from .models import Slider, Team, About

# Register your models here.


class SliderAdmin(admin.ModelAdmin):

    def slider_image(self, object):
        return format_html('<img src="{}" width="100"/>'.format(object.photo.url))

    list_display = ['headline', 'slider_image', 'button_text']
    list_display_links = ['headline']


class TeamAdmin(admin.ModelAdmin):

    # ATTRIBUTES OPERATION OF A MODEL CAN ALSO BE DONE FROM MODELS.PY, READ DOCUMENTATION FOR MORE
    def image(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))

    def fullname(self, object):
        return (object.first_name+' '+object.last_name).upper()

    list_display = ['id', 'fullname', 'image', 'role', 'created_date']
    list_display_links = ['fullname', 'image']
    search_fields = ['first_name', 'last_name']
    list_filter = ['role']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']


admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(About, AboutAdmin)
