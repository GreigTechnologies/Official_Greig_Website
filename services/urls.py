from django.urls import path
from . import views

urlpatterns = [
    path('', views.oil, name='oil'),
    path('iridium/', views.iridium, name='iridium' ),
    path('fleet/', views.fleet, name='fleet' ),
    path('ship/', views.ship, name='ship'),
    
]