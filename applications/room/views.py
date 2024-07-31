from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView, FormView
# import models
from .models import RoomModel
# import forms
from .forms import RoomReserveForm
from applications.home.forms import SubscriptionForm

# Create your views here.


class RoomsView(ListView):
    template_name = 'room/rooms.html'
    model = RoomModel
    context_object_name = 'rooms'
    paginate_by = 6
    ordering = '-modified'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_subscription'] = SubscriptionForm()
        return context


class RoomView(DetailView):
    template_name = 'room/room.html'
    model = RoomModel
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_subscription'] = SubscriptionForm()
        return context


class ReserveRoomView(FormView):
    template_name = 'room/reserve_room.html'
    form_class = RoomReserveForm
    success_url = reverse_lazy('room_app:rooms')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_subscription'] = SubscriptionForm()
        room_id = self.kwargs.get('pk', None)
        if room_id:
            context['room'] = RoomModel.objects.get(id=room_id)
        return context

    def form_valid(self, form):
        room_id = self.kwargs.get('pk', None)
        if room_id:
            room = RoomModel.objects.get(id=room_id)
            # Acceder a los datos del formulario a través de cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            rooms = form.cleaned_data['rooms']
            adults = form.cleaned_data['adults']
            date_start = form.cleaned_data['date_start']
            date_end = form.cleaned_data['date_end']
            message = form.cleaned_data['message']

            # Enviar correo electrónico al administrador
            subject = f"New Reservation for {room.name}"
            email_message = (
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Rooms: {rooms}\n"
                f"Adults: {adults}\n"
                f"Check-in Date: {date_start}\n"
                f"Check-out Date: {date_end}\n"
                f"Message: {message}"
            )
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [admin[1] for admin in settings.ADMINS]  # Obtener correos de los administradores

            try:
                send_mail(subject, email_message, from_email, recipient_list)
                messages.success(self.request, _('Thank you for your request. We will contact you soon'))
            except Exception as e:
                messages.error(self.request, _(f'An error occurred while submitting the request, please try again later.'))

        return super().form_valid(form)
