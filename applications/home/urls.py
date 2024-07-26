from django import views
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('introduction/', views.IntroductionView.as_view(), name='introduction'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]