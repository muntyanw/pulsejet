from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

# Гостевые страницы
class HomePageView(TemplateView):
    template_name = "guest/index.html"
    
class ModelingView(TemplateView):
    template_name = "guest/modeling.html"
    
class ProcessHowUseView(TemplateView):
    template_name = "guest/how_use.html"

class ProcessAboutPMView(TemplateView):
    template_name = "guest/about_pm.html"

class  DescriptionMmView(TemplateView):
    template_name = "guest/description_mat_model.html"

class  WhatToReadView(TemplateView):
    template_name = "guest/what-to-read.html"

class FAQView(TemplateView):
    template_name = "guest/faq.html"

class ContactsView(TemplateView):
    template_name = "guest/contacts.html"

# Личный кабинет (доступ только для авторизованных пользователей)
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "account/dashboard.html"

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')  # Перенаправление после успешной регистрации на страницу входа

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Если пользователь уже аутентифицирован, перенаправляем его на главную страницу
            return redirect('home')  # Здесь 'home' - это имя маршрута для главной страницы
        return super().get(request, *args, **kwargs)

class LogoutView(LogoutView):
    # Перенаправление после выхода
    next_page = reverse_lazy('home')
