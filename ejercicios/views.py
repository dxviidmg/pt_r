from django.shortcuts import render
from rest_framework.views import APIView
from .utils import define_primo_proximo, get_pokemon_type, get_pokemon_list
from rest_framework.response import Response

class NumeroPrimoProximo(APIView):
    def get(self, request):
        
        params = request.query_params

        if 'num' in params.keys():
            primo = define_primo_proximo(int(params['num']))
            return Response(primo)

        return Response('Error, al insertar argumento')


class PokemonType(APIView):
    def get(self, request):
        params = request.query_params
        if 'type' in params.keys():
            data = get_pokemon_type(params['type'])
            
            #Regresa solo la el dict pokemon
            data = data['pokemon']

            #Regresa lista de pokemons que inicien con la letra s
            data = get_pokemon_list(data, 's')

            return Response(data)

        return Response('Error, al insertar argumento')