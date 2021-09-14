"""
Serializers for Auth
"""
from rest_framework import serializers

class EmailRegisterSerializer(serializers.Serializer):
    """Serializer for Email Register"""
    email = serializers.EmailField()
    username = serializers.CharField(min_length=3)
    password = serializers.CharField(min_length=8, max_length=30)
