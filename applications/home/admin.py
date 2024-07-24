from django.contrib import admin
#import models
from django.contrib.auth.models import User, Group
from .models import (HomeModel, HomeRoomImage, HomeTourImage, HomeBreakfastImage, IntroductionModel, GalleryModel)

# Register your models here.
class HomeWidgetRoom(admin.StackedInline):
    model = HomeRoomImage
    extra = 0

class HomeWidgetTour(admin.StackedInline):
    model = HomeTourImage
    extra = 0

class HomeWidgetBreakfast(admin.StackedInline):
    model = HomeBreakfastImage
    extra = 0

class HomePageAdmin(admin.ModelAdmin):
    inlines = [HomeWidgetRoom, HomeWidgetTour, HomeWidgetBreakfast]

    def has_add_permission(self, request):
        # Permitir añadir solo si no hay registros existentes
        if HomeModel.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    

class IntroductionPageAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # Permitir añadir solo si no hay registros existentes
        if IntroductionModel.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(HomeModel, HomePageAdmin)
admin.site.register(IntroductionModel, IntroductionPageAdmin)
admin.site.register(GalleryModel)