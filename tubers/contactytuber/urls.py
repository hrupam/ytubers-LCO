from django.urls import path
from . import views

urlpatterns = [
    path('contactytuberteam', views.contactytuberteam, name='contactytuberteam'),
]
