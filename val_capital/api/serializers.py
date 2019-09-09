from rest_framework import serializers
from core.models import Fund, Commitment, Call, Drawdown

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ['id', 'name']

class CommitmentSerializer(serializers.ModelSerializer):
    fundname = serializers.CharField(source='fund.name')
    date = serializers.DateField(format="%d-%m-%Y")
    class Meta:
        model = Commitment
        fields = ['id', 'fund','date','amount','undrawn', 'fundname']


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ['id', 'amount', 'date']


class DrawdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawdown
        fields = ['id', 'call', 'commitment', 'date', 'amount']