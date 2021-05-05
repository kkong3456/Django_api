from django.shortcuts import render
from rest_framework import generics
from .models import JisaNetIncrease, BonbuNetIncrease
from .serializers import JisaNetIncreaseSerializer,BonbuNetIncreaseSerializer


class JisaNetIncreaseList(generics.ListCreateAPIView):
    queryset = JisaNetIncrease.objects.all()
    serializer_class = JisaNetIncreaseSerializer


class JisaNetIncreaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JisaNetIncrease.objects.all()
    serializer_class = JisaNetIncreaseSerializer


class BonbuNetIncreaseList(generics.ListCreateAPIView):
    queryset = BonbuNetIncrease.objects.all()
    serializer_class = BonbuNetIncreaseSerializer


class BonbuNetIncreaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BonbuNetIncrease.objects.all()
    serializer_class = BonbuNetIncreaseSerializer
