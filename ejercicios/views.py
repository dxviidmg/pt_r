from django.shortcuts import render
from rest_framework.views import APIView
from .utils import define_primo_proximo
from rest_framework.response import Response

class NumeroPrimoProximo(APIView):
    def get(self, request):
        primo = define_primo_proximo(20)
        return Response(primo)