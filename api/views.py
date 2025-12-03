from rest_framework import viewsets
from pokedex.models import Pokemon, Trainer
from .serializers import PokemonSerializer, TrainerSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    required_scopes = ['write']

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    required_scopes = ['write']