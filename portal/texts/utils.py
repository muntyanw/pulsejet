# texts/utils.py
from django.utils import translation
from .texts_en import texts as texts_en
from .texts_uk import texts as texts_uk


def get_texts():
    
    current_language = translation.get_language()
    
    if current_language.startswith('uk'):
        return texts_uk
    elif current_language.startswith('en'):
        return texts_en
    else:
        return texts_en 
