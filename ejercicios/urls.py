from django.urls import path
from .views import *

urlpatterns = [
    path('npp/', NumeroPrimoProximo.as_view(), name='numero-primo-proximo'),
    path('pokemon_type/', PokemonType.as_view(), name='pokemon-type'),
]