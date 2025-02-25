from django.urls import path
from .views import (
    HomePageView,
    ProcessHowUseView,
    ProcessAboutPMView,
    DescriptionMmView,
    WhatToReadView,
    FAQView,
    DashboardView,
    RegisterView,
    ContactsView,
    ModelingView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about-pm/', ProcessAboutPMView.as_view(), name='about-pm'),
    path('modeling/', ModelingView.as_view(), name='modeling'),
    path('how-use/', ProcessHowUseView.as_view(), name='how-use'),
    path('description-mat-model/', DescriptionMmView.as_view(), name='description-mat-model'),
    path('what-to-read/', WhatToReadView.as_view(), name='what-to-read'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('account/', DashboardView.as_view(), name='account'),
    path('register/', RegisterView.as_view(), name='register'),
]
