# your_app/context_processors.py
from portal.texts.utils import get_texts
from django.urls import resolve

def texts_context(request):
    current_url = resolve(request.path_info)
    url_name = current_url.url_name
    
    texts = get_texts()
    context_data = texts.get(url_name, {})
    return {
        't': context_data,
        "url_name":url_name
    }
