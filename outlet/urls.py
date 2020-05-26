from django.urls import path
from django.shortcuts import HttpResponse
from . import views

urlpatterns = [
    path('', views.index, name='OutletHome'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='Contact'),
    path('tracker/', views.tracker, name='Tracker'),
    path('search/', views.search, name='Search'),
    path('productview/<int:id>', views.prodview, name='ProductView'),
    path('checkout/', views.checkout, name='Checkout'),
] 
