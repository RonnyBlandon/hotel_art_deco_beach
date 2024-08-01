from modeltranslation.translator import translator, TranslationOptions
from .models import HomeModel

class HomeModelTranslationOptions(TranslationOptions):
    fields = ('title_banner','subtitle_banner')  # Campos a traducir

translator.register(HomeModel, HomeModelTranslationOptions)