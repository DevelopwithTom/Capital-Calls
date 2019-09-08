from rest_framework import viewsets
from core.models import Fund, Deposit, Call, Commitment
from api.serializers import FundSerializer, DepositSerializer, CallSerializer, CommitmentSerializer

class FundViewSet(viewsets.ModelViewSet):
    serializer_class = FundSerializer
    queryset = Fund.objects.all()

class DepositViewSet(viewsets.ModelViewSet):
    serializer_class = DepositSerializer
    queryset = Deposit.objects.all()

class CallViewSet(viewsets.ModelViewSet):
    serializer_class = CallSerializer
    queryset = Call.objects.all()

class CommitmentViewSet(viewsets.ModelViewSet):
    serializer_class = CommitmentSerializer
    queryset = Commitment.objects.all()

