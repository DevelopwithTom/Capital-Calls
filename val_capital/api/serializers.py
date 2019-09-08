from rest_framework import serializers
from core.models import Fund

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ['id', 'name']