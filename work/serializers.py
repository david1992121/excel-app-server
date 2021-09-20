"""
Serializers for Auth
"""
from account.serializers import UserSerializer
from account.models import User
from django.db.models import fields
from work.models import Ratio, Sheet
from rest_framework import serializers

class RatioSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = Ratio

class SheetSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        fields = "__all__"
        model = Sheet

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        new_sheet = Sheet(**validated_data)
        new_sheet.user = User.objects.get(pk = user_id)
        new_sheet.save()
        return new_sheet