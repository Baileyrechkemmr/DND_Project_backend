from rest_framework import generics
from .serializers import NpcSerializer
from .models import Npc

class NpcList(generics.ListCreateAPIView):
    queryset = Npc.objects.all().order_by('id')  
    serializer_class = NpcSerializer    

class NpcDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Npc.objects.all().order_by('id') 
    serializer_class = NpcSerializer