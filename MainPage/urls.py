from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('AboutUs/', views.aboutus, name='about_us' ),
    path('ContactUs/', views.contactus, name='contact_us' ),

]