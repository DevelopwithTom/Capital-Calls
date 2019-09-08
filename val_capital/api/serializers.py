from rest_framework import serializers
from core.models import Fund, Deposit, Call, Commitment

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ['id', 'name']

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['id', 'fund','date','amount','undrawn']


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ['id', 'amount', 'date']


class CommitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commitment
        fields = ['id', 'call', 'deposit', 'date', 'amount']