from django.db import models
from django.conf import settings


# Create your models here.

class JisaNetIncrease(models.Model):
    date = models.DateField()
    Gangneung_jisa = models.IntegerField()
    Goyang_jisa = models.IntegerField()
    Gwangin_jisa = models.IntegerField()
    Gwanghwamun_jisa = models.IntegerField()
    Guri_jisa = models.IntegerField()
    Nowon_jisa = models.IntegerField()
    Seodaemun_jisa = models.IntegerField()
    Wonju_jisa = models.IntegerField()
    Uijeongbu_jisa = models.IntegerField()
    Chuncheon_jisa = models.IntegerField()

    def __str_(self):
        return self.date + '의 ' + self.Nowon_jisa + ' 실적입니다'

    class Meta:
        ordering = ['date']
        db_table = 'jisa_net_increase'


class BonbuNetIncrease(models.Model):
    date = models.DateField()
    bugbu_bonbu = models.IntegerField()
    dongbu_bonbu = models.IntegerField()
    gangnam_bonbu = models.IntegerField()
    daegu_gyeongbug = models.IntegerField()
    busan_gyeongnam = models.IntegerField()
    seobu_bonbu = models.IntegerField()
    jeonnam_jeonbug = models.IntegerField()
    jesu_bonbu = models.IntegerField()
    chungnam_chungbug = models.IntegerField()

    def __str_(self):
        return self.date + '의 ' + self.bugbu_bonbu + ' 실적입니다'

    class Meta:
        ordering = ['date']
        db_table = 'bonbu_net_increase'
