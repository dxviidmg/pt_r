from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import *

urlpatterns = [
    path('npp/', NumeroPrimoProximo.as_view(), name='numero-primo-proximo'),
]