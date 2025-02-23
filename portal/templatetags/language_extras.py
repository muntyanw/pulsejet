# your_app/templatetags/language_extras.py
import re
from django import template
from django.conf import settings

register = template.Library()

@register.filter
def remove_language_prefix(path):
    """
    Убирает из URL языковой префикс, если он присутствует.
    Например, из '/uk/some/page/' вернет '/some/page/'.
    """
    # Собираем список поддерживаемых языковых кодов из настроек
    lang_codes = [lang[0] for lang in settings.LANGUAGES]
    # Формируем регулярное выражение для поиска префикса
    pattern = r'^/(' + '|'.join(lang_codes) + r')(/|$)'
    # Заменяем найденный префикс на '/'
    new_path = re.sub(pattern, '/', path)
    # Если результат пустой, возвращаем '/'
    return new_path if new_path.strip() else '/'
