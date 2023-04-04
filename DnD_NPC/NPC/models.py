from django.db import models

# Create your models here.
class Npc(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    description = models.CharField(max_length=250)
    job = models.CharField(max_length=30)
    quirk = models.CharField(max_length=150)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    race = models.CharField(max_length=30)
    alignment = models.CharField(max_length=30)
    dnd_class = models.CharField(max_length=30)
    def __str__(self): return self.name 