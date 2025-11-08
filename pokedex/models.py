from django.db import models

# Create your models here.
class Pokemon(models.Model):
    TYPE_CHOICES = [
        ('Fuego', '🔥 Fuego'),
        ('Agua', '💧 Agua'),
        ('Planta', '🌿 Planta'),
        ('Eléctrico', '⚡ Eléctrico'),
        ('Normal', '⚪ Normal'),
    ]

    name = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, null=False)
    weight = models.IntegerField()
    height = models.IntegerField()
    picture = models.ImageField(upload_to='pokemons/', null=True, blank=True)
    trainer = models.ForeignKey('Trainer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
###Trainer
class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birthdate = models.DateField(null=False)
    level = models.IntegerField()

    def __str__(self):
        return self.first_name + self.last_name
    