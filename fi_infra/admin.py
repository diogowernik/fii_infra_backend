from django.contrib import admin
from . import models

# Register your models here.
class AtivoAdmin(admin.ModelAdmin):
    list_display = ('ticker','nome', 'taxa_adm', 'gestor','juros','inicio')
    list_editable = ['taxa_adm', 'gestor','juros','inicio']

class CotaPatrimonialAdmin(admin.ModelAdmin):
    list_display = ('ticker','date', 'cota_patrimonial','patrimonio_liquido')
    list_editable = ['cota_patrimonial','patrimonio_liquido']

admin.site.register(models.Ativo,AtivoAdmin)
admin.site.register(models.CotaPatrimonial, CotaPatrimonialAdmin)