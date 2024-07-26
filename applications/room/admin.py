from django.contrib import admin
# import models
from .models import RoomModel, RoomImage

# Register your models here.
class RoomImageAdmin(admin.StackedInline):
    model = RoomImage
    extra = 0

class RoomModelAdmin(admin.ModelAdmin):
    inlines = [RoomImageAdmin,]


admin.site.register(RoomModel, RoomModelAdmin)