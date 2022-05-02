"""
Serializers for Auth
"""
from account.serializers import UserSerializer
from account.models import User
from django.db.models import fields
from work.models import Ratio, Sheet, Industry
from rest_framework import serializers


class RatioSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Ratio


class IndustrySerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Industry


class SheetSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    a_profit_category_id = serializers.IntegerField(write_only=True)
    a_profit_category = IndustrySerializer(read_only=True)
    b_profit_category_id = serializers.IntegerField(write_only=True)
    b_profit_category = IndustrySerializer(read_only=True)
    c_profit_category_id = serializers.IntegerField(write_only=True)
    c_profit_category = IndustrySerializer(read_only=True)

    class Meta:
        fields = "__all__"
        model = Sheet

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        a_profit_id = validated_data.pop('a_profit_category_id')
        b_profit_id = validated_data.pop('b_profit_category_id')
        c_profit_id = validated_data.pop('c_profit_category_id')

        new_sheet = Sheet(**validated_data)

        if a_profit_id == 0:
            new_sheet.a_profit_category_id = None
        else:
            new_sheet.a_profit_category_id = a_profit_id

        if b_profit_id == 0:
            new_sheet.b_profit_category_id = None
        else:
            new_sheet.b_profit_category_id = b_profit_id

        if c_profit_id == 0:
            new_sheet.c_profit_category_id = None
        else:
            new_sheet.c_profit_category_id = c_profit_id

        new_sheet.user = User.objects.get(pk=user_id)
        new_sheet.save()
        return new_sheet

    def update(self, instance, validated_data):
        a_profit_id = validated_data.pop('a_profit_category_id')
        b_profit_id = validated_data.pop('b_profit_category_id')
        c_profit_id = validated_data.pop('c_profit_category_id')

        if a_profit_id == 0:
            instance.a_profit_category_id = None
        else:
            instance.a_profit_category_id = a_profit_id

        if b_profit_id == 0:
            instance.b_profit_category_id = None
        else:
            instance.b_profit_category_id = b_profit_id

        if c_profit_id == 0:
            instance.c_profit_category_id = None
        else:
            instance.c_profit_category_id = c_profit_id

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
