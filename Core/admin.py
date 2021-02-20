from django.contrib import admin
from Core.models import Evento
# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento','data_criacao')
    list_filter = ('usuario','titulo',)
admin.site.register(Evento, EventoAdmin)