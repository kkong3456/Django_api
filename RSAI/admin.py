from django.contrib import admin
from .models import JisaNetIncrease, BonbuNetIncrease,RsaiJojik


# Register your models here.

# class RsaiAdmin(admin.ModelAdmin):

class JisaNetIncreaseAdmin(admin.ModelAdmin):
    list_display = ['date', 'Gangneung_jisa','Goyang_jisa','Gwangin_jisa','Gwanghwamun_jisa'
                    ,'Guri_jisa','Nowon_jisa','Seodaemun_jisa','Wonju_jisa','Uijeongbu_jisa','Chuncheon_jisa']
    # list_display = ['id']
    # list_editable = []


class BonbuNetIncreaseAdmin(admin.ModelAdmin):
    list_display = ['date', 'bugbu_bonbu','dongbu_bonbu']
    # list_display = ['id']
    # list_editable = []

class RsaiJojikAdmin(admin.ModelAdmin):
    list_display=['id','sysdate','product','jojik','this_hj_count','this_hj_ratio','that_hj_count','that_hj_ratio','up_ratio','rank']


admin.site.register(JisaNetIncrease, JisaNetIncreaseAdmin)
admin.site.register(BonbuNetIncrease, BonbuNetIncreaseAdmin)
admin.site.register(RsaiJojik,RsaiJojikAdmin)
