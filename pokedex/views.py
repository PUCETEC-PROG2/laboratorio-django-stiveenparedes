from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.decorators import login_required

from pokedex.models import Pokemon, Trainer
from pokedex.forms import PokemonForm


def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons, 'trainers': trainers}, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    template = loader.get_template('display_trainers.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()

    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:pokemon', pokemon_id=pokemon.id)
    else:
        form = PokemonForm(instance=pokemon)

    return render(request, 'pokemon_form.html', {'form': form, 'pokemon': pokemon})

@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')

class CustomLoginView (LoginView):
    template_name = 'login_form.html'

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')