from rest_framework import serializers
from django.utils import timezone
from .models import Сurrency, Rate


class CurrencySerializer(serializers.Serializer):
    CharCode = serializers.CharField(max_length=3, source="char_code")
    Name = serializers.CharField(max_length=150, source="name")
    Value = serializers.DecimalField(max_digits=7, decimal_places=4, source="value")

    def create(self, validated_data):
        value = validated_data.pop("value")
        obj, created = Сurrency.objects.get_or_create(**validated_data)
        if not obj.rates.filter(date=timezone.now()).exists():
            obj.rates.create(value=value)
        return obj


class RateSerializer(serializers.ModelSerializer):
    currency = serializers.CharField(source="currency.char_code")

    class Meta:
        model = Rate
        exclude = ["id"]
