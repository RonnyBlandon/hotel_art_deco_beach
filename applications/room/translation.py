# myapp/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import RoomModel

class RoomModelTranslationOptions(TranslationOptions):
    fields = ('description',)  # Campos a traducir

translator.register(RoomModel, RoomModelTranslationOptions)