from rest_framework import viewsets
from tool.api import serializers
from tool import models

class OrdemServicoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrdemServicoSerializer
    queryset = models.OrdemServico.objects.all()