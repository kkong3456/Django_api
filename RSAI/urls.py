from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('api/jisa-net-increase-list/', JisaNetIncreaseList.as_view()),
    path('api/jisa-net-increase-detail/<int:pk>/', JisaNetIncreaseDetail.as_view()),
    path('api/bonbu-net-increase-list/', BonbuNetIncreaseList.as_view()),
    path('api/bonbu-net-increase-detail/<int:pk>/', BonbuNetIncreaseDetail.as_view()),
    path('api/rsai-jojik-list/',RsaiJojikList.as_view()),
]
