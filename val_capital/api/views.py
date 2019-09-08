from rest_framework import viewsets
from core.models import Fund
from api.serializers import FundSerializer

class FundViewSet(viewsets.ModelViewSet):
    serializer_class = FundSerializer
    queryset = Fund.objects.all()

