from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns=[
    path('rsai/',RsaiList.as_view()),
    path('rsai/<int:pk>/',RsaiDetail.as_view()),
]