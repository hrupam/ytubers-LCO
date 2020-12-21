from django.contrib import admin
from .models import Hiretuber

# Register your models here.


class HiretuberAdmin(admin.ModelAdmin):

    def fullname(self, object):
        return object.first_name+' '+object.last_name

    list_display = ['email', 'fullname', 'tuber_name']


admin.site.register(Hiretuber, HiretuberAdmin)
