from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
# import models
from .models import RoomModel, RoomImage

# Register your models here.
class RoomImageAdmin(admin.StackedInline):
    model = RoomImage
    extra = 0

class RoomModelAdmin(TranslationAdmin, admin.ModelAdmin):
    inlines = [RoomImageAdmin,]


admin.site.register(RoomModel, RoomModelAdmin)