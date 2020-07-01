from django.contrib import admin
from . import views
from django.urls import path,include
app_name = 'home'
urlpatterns = [
    path('',views.home, name='home'),
    path('about', views.about, name='about'),
    path('signup', views.signup, name='signup'),
]
