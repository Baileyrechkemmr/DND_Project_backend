from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Npc(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)  
    description = models.CharField(max_length=250)
    job = models.CharField(max_length=30, blank=True)
    quirk = models.CharField(max_length=150, blank=True)
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    race = models.CharField(max_length=30)
    alignment = models.CharField(max_length=30, blank=True)
    dnd_class = models.CharField(max_length=30, blank=True)
    user = models.ManyToManyField(User)
    def __str__(self): return self.name 
