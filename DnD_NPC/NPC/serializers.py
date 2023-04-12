from rest_framework import serializers # use rest_framework's serializer
from .models import Npc # import our Contact model
from django.contrib.auth.models import User

class NpcSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Npc
        fields = ('id', 'name', 'age', 'description', 'job', 'quirk', 'strength','constitution','intelligence','wisdom','charisma','race','alignment','dnd_class') 