from .models import JisaNetIncrease,BonbuNetIncrease,RsaiJojik
from rest_framework import serializers


class JisaNetIncreaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = JisaNetIncrease
        fields = '__all__'

class BonbuNetIncreaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=BonbuNetIncrease
        fields='__all__'

class RsaiJojikSerializer(serializers.ModelSerializer):
    class Meta:
        model=RsaiJojik
        fields='__all__'