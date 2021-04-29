from django.shortcuts import render
from rest_framework import generics
from .models import Rsai
from .serializers import RsaiSerializer

class RsaiList(generics.ListCreateAPIView):
    queryset = Rsai.objects.all()
    serializer_class = RsaiSerializer

class RsaiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Rsai.objects.all()
    serializer_class=RsaiSerializer

