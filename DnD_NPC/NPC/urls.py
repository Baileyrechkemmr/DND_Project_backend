from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('npc', views.NpcList.as_view(), name='npc_list'),  
    path('npc/<int:pk>', views.NpcDetail.as_view(), name='npc_detail'), 
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.authtoken'))
]