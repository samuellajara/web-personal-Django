from django.urls import path
from . import views

urlpatterns = [
    path('',views.bot, name = "bot"),   
    path('PRECIO_ACTUAL', views.PRECIO_ACTUAL, name = "PRECIO_ACTUAL"), 
    path('MEDIA_MOVIL_4HS', views.MEDIA_MOVIL_4HS, name = "MEDIA_MOVIL_4HS"), 
]


      
 

