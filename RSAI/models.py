from django.db import models
from django.conf import settings


# Create your models here.

class Rsai(models.Model):
    jisa = models.CharField(max_length=20)
    day = models.DateField('일자')
    sales = models.CharField(max_length=30)
    etc = models.CharField(max_length=200, null=True,blank=True)

    def __str_(self):
        return self.jisa + '의 ' + self.day + '일 매출은 ' + self.sales + '입니다.'

    class Meta:
        ordering = ['jisa']
