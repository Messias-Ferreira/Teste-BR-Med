from rest_framework import serializers
from conversor.models import Cotacao

class CotacaoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Cotacao
        fields = "__all__"
    