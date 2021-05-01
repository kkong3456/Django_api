from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns=[
    path('jisa-net-increase-list/',JisaNetIncreaseList.as_view()),
    path('jisa-net-increase-detail/<int:pk>/',JisaNetIncreaseDetail.as_view()),
    path('bonbu-net-increase-list/',BonbuNetIncreaseList.as_view()),
    path('bonbu-net-increase-detail/<int:pk>/',BonbuNetIncreaseDetail.as_view()),
]