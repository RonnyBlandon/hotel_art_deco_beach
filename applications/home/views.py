from django.db import IntegrityError
from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, ListView, FormView, View
# import models
from .models import HomeModel, IntroductionModel, GalleryModel, SubscriptionModel
# import forms
from .forms import HomeReserveForm, SubscriptionForm
# Create your views here.


class HomeView(FormView):
    template_name = 'home/home.html'
    form_class = HomeReserveForm
    success_url = reverse_lazy('home_app:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = HomeModel.objects.first()
        context['form_subscription'] = SubscriptionForm()
        return context

    def form_valid(self, form):
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
        subject = f"New reservation from the home page"
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
        # Obtener correos de los administradores
        recipient_list = [admin[1] for admin in settings.ADMINS]

        try:
            send_mail(subject, email_message, from_email, recipient_list)
            messages.success(self.request, _('Thank you for your request. We will contact you soon'))
        except Exception as e:
            messages.error(self.request, _(f'An error occurred while submitting the request, please try again later.'))

        return super().form_valid(form)


class IntroductionView(TemplateView):
    template_name = 'home/introduction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['introduction'] = IntroductionModel.objects.first()
        context['form_subscription'] = SubscriptionForm()
        return context


class GalleryView(ListView):
    template_name = 'home/gallery.html'
    model = GalleryModel
    context_object_name = 'gallery'
    paginate_by = 12
    ordering = '-id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_subscription'] = SubscriptionForm()
        return context


class ContactView(TemplateView):
    template_name = 'home/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_subscription'] = SubscriptionForm()
        return context


class SubscriptionView(View):
    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                # Intenta guardar el correo en la base de datos
                SubscriptionModel.objects.create(email=email)
                messages.success(request, _('You have successfully subscribed!'))
            except IntegrityError:
                # Si se produce un error de integridad (correo duplicado), muestra un mensaje de error
                messages.error(request, _('This email is already registered.'))
        else:
            messages.error(request, _('There was an error with your subscription. Please try again.'))

        # Redirige a la misma página desde la que se envió el formulario
        next_url = request.POST.get('next', '/')

        # Verifica si la URL es segura
        if not url_has_allowed_host_and_scheme(url=next_url, allowed_hosts=request.get_host()):
            next_url = '/'  # Redirige a la página principal si la URL no es segura

        return redirect(next_url)