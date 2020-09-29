from rest_framework import viewsets
from core.models import Fund, Commitment, Call, Drawdown
from api.serializers import FundSerializer, CommitmentSerializer, CallSerializer, DrawdownSerializer

class FundViewSet(viewsets.ModelViewSet):
    serializer_class = FundSerializer
    queryset = Fund.objects.all()

class CommitmentViewSet(viewsets.ModelViewSet):
    serializer_class = CommitmentSerializer
    queryset = Commitment.objects.all()

class CallViewSet(viewsets.ModelViewSet):
    serializer_class = CallSerializer
    queryset = Call.objects.all()

class DrawdownViewSet(viewsets.ModelViewSet):
    serializer_class = DrawdownSerializer
    queryset = Drawdown.objects.all()

