from django.contrib import admin

# Register your models here.
from aplicacao_cryptomoedas.models import Moeda 
class MoedaAdmin(admin.ModelAdmin):    
    list_display = ('MOEDA_A_ACOMPANHAR', 'MOEDA_BASE', 'VALOR_DA_MOEDA',)

    



admin.site.register(Moeda , MoedaAdmin)
