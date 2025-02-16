from django.urls import path
from .views import (
    HomePageView,
    ProcessDescriptionView,
    ProcessModelingView,
    FAQView,
    DashboardView,
    RegisterView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('description/', ProcessDescriptionView.as_view(), name='description'),
    path('modeling/', ProcessModelingView.as_view(), name='modeling'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('account/', DashboardView.as_view(), name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
]
