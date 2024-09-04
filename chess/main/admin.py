from django.contrib import admin
from .models import Players


@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'rank')
    list_filter = ('rank', 'age')

