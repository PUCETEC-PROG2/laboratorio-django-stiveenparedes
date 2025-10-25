from django.contrib import admin
from .models import Pokemon
from .models import Trainer

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'weight', 'height')
    search_fields = ('name', 'type')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthdate', 'level')
    search_fields = ('first_name', 'last_name')
