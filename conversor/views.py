"""
Modulo view para acesso dos processos
"""
from django.shortcuts import render
from rest_framework import generics

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

        resultado = Cotacao.objects.all()

        if dt_inicio and dt_fim:
            resultado = resultado.filter(data__gte=converter_data(dt_inicio), data__lte=converter_data(dt_fim))
        elif dt_inicio:
            resultado = resultado.filter(data__gte=converter_data(dt_inicio))
        elif dt_fim:
            resultado = resultado.filter(data__lte=converter_data(dt_inicio))

        return resultado
