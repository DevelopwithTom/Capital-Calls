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


class DrawdownSerializer(serializers.ModelSerializer):
    callid = serializers.CharField(source='call.id')
    commitment = CommitmentSerializer()

    class Meta:
        model = Drawdown
        fields = ['id', 'call', 'commitment', 'date', 'amount', 'callid']


class CallSerializer(serializers.ModelSerializer):
    # Below is a nested serializer for dealing with related objects
    drawdown_set = DrawdownSerializer(many=True, read_only=True)
    class Meta:
        model = Call
        fields = ['id', 'amount', 'date', 'drawdown_set' ]

