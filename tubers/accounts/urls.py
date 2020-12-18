from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),

    # django has in-built function logout, thats why logout_user
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('change_password', views.change_password, name='change_password'),
]
