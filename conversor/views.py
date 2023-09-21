"""
Modulo view para acesso dos processos
"""
from django.shortcuts import render
from rest_framework import generics

from django.http.response import JsonResponse
from conversor.serializer import CotacaoSerialize
from conversor.models import Cotacao
from conversor.utils import converter_data

def index(request):
    """

    Args:
        request: Requisição da api

    Returns: template renderizado
    """    
    return render(request, "conversor/index.html")

class CotacoesList(generics.ListAPIView):
    model = Cotacao
    serializer_class = CotacaoSerialize


    def get_queryset(self):

        dt_inicio = self.request.query_params.get('dt_inicio')
        dt_fim = self.request.query_params.get('dt_fim')
        moeda = self.request.query_params.get('moeda', "EUR")

        resultado = Cotacao.objects.filter(moeda=moeda)

        if dt_inicio and dt_fim:
            resultado = resultado.filter(data__gte=converter_data(dt_inicio), data__lte=converter_data(dt_fim), moeda__in=["EUR", "JPY", "BRL"])
        elif dt_inicio:
            resultado = resultado.filter(data__gte=converter_data(dt_inicio), moeda__in=["EUR", "JPY", "BRL"])
        elif dt_fim:
            resultado = resultado.filter(data__lte=converter_data(dt_inicio), moeda__in=["EUR", "JPY", "BRL"])
        
        return resultado.order_by("data")[:5]

