from rest_framework import serializers

from .models import Ativo, CotaPatrimonial

class CotaPatrimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotaPatrimonial
        fields = ['date','patrimonio_liquido','cota_patrimonial']

class AtivoSerializer(serializers.HyperlinkedModelSerializer):
    dados_de_mercado = CotaPatrimonialSerializer(many=True, read_only=True)
    class Meta:
        model = Ativo
        fields = ('ticker','nome', 'gestor','inicio','taxa_adm','juros','dados_de_mercado')