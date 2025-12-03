from django.urls import path, include
from rest_framework import routers
from .views import PokemonViewSet

router = routers.DefaultRouter()
router.register(r'pokemons', PokemonViewSet, basename='pokemon')

urlpatterns = [
    path('', include(router.urls)),
]
