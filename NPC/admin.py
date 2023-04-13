from django.contrib import admin

# Register your models here.
from .models import Npc
@admin.register(Npc)
class NpcAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'description', 'job', 'quirk', 'strength','constitution','intelligence','wisdom','charisma','race','alignment','dnd_class')
# ok .through is defining a table that connects the many to many relationship.  through is an intermediary table for many to man
