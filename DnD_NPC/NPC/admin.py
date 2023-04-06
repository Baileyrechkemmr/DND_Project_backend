from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Npc
admin.site.unregister(User)
@admin.register(Npc)
class NpcAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'description', 'job', 'quirk', 'strength','constitution','intelligence','wisdom','charisma','race','alignment','dnd_class')
# ok .through is defining a table that connects the many to many relationship.  through is an intermediary table for many to many
class NpcInline(admin.TabularInline):
    model = Npc.user.through
    extra = 1


class CustomUserAdmin(UserAdmin):
    inlines = [NpcInline]

admin.site.register(User, CustomUserAdmin)