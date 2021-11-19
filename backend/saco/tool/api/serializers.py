from rest_framework import serializers
from tool import models

class OrdemServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrdemServico
        fields = '__all__'