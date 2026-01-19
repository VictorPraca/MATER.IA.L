from rest_framework import viewsets
from .models import Engenheiro
from .serializers import EngenheiroSerializer

class EngenheiroViewSet(viewsets.ModelViewSet):
    queryset = Engenheiro.objects.all()
    serializer_class = EngenheiroSerializer
