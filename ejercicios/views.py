from django.shortcuts import render
from rest_framework.views import APIView
from .utils import define_primo_proximo
from rest_framework.response import Response

class NumeroPrimoProximo(APIView):
    def get(self, request, *args, **kwargs):
        
        params = request.query_params

        if 'num' in params.keys():
            primo = define_primo_proximo(int(params['num']))
            return Response(primo)

        return Response('Error, al insertar argumento')