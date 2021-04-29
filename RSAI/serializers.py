from .models import Rsai
from rest_framework import serializers


class RsaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rsai
        fields = '__all__'
