from django.contrib import admin
from .models import Rsai

# Register your models here.

class RsaiAdmin(admin.ModelAdmin):
    list_display=['id','jisa','day','sales','etc']
    list_editable = ['jisa']

admin.site.register(Rsai,RsaiAdmin)