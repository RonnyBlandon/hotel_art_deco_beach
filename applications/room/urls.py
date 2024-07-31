from django import views
from django.urls import path
from . import views

app_name = "room_app"

urlpatterns = [
    path('rooms/', views.RoomsView.as_view(), name='rooms'),
    path('room/<slug>/', views.RoomView.as_view(), name='room'),
    path('reserve-room/<int:pk>/', views.ReserveRoomView.as_view(), name='reserve_room'),
]