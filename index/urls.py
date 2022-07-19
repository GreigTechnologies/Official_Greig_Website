from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('about/', views.aboutus, name='about' ),
    path('contact/', views.contactus, name='contact' ),
]