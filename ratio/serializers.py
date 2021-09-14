"""
Serializers for Auth
"""
from ratio.models import Ratio
from rest_framework import serializers

class RatioSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = Ratio