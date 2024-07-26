from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
#import models
from .models import HomeModel, IntroductionModel, GalleryModel
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = HomeModel.objects.first()
        return context


class IntroductionView(TemplateView):
    template_name = 'home/introduction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['introduction'] = IntroductionModel.objects.first()
        return context


class GalleryView(ListView):
    template_name = 'home/gallery.html'
    model = GalleryModel
    context_object_name = 'gallery'


class ContactView(TemplateView):
    template_name = 'home/contact.html'