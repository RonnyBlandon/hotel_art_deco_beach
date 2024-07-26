from django.shortcuts import render
from django.views.generic import ListView, DetailView
# import models
from .models import RoomModel

# Create your views here.
class RoomsView(ListView):
    template_name = 'room/rooms.html'
    model = RoomModel
    context_object_name = 'rooms'
    paginate_by = 6
    ordering = '-modified'
    

class RoomView(DetailView):
    template_name = 'room/room.html'
    model = RoomModel
    context_object_name = 'room'