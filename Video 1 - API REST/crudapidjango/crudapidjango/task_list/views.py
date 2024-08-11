# from django.shortcuts import render
# from rest_framework import generics # importamos el modulo de rest_framework
# from crudapidjango.task_list import TareaSerializer
# from task_list.models import Tarea

from django.shortcuts import render
from rest_framework import generics
from .serializers import TareaSerializer
from .models import Tarea

# Create your views here.

'''
Especificaciones a tener en cuenta (generics):
- ListAPIView: Nos permite mostrar la lista de todas las tareas y puedamos crear
nuevas tareas (Get/ Post).

# Otras cosas...
serializable: Traduce un objeto en formato json() por defecto.
'''
# Especificamos nuestras vistas (endpoint)

# GET
class TareasAPIView(generics.ListAPIView):
    queryset = Tarea.objects.all() # Nos muestra toda la ORM que hay en la BD
    serializer_class = TareaSerializer
    
    
# PUT/ DELETE:
class TareaAPIView(generics.RetrieveUpdateDestroyAPIView):
    query_set = Tarea.objects.all() 
    serializer_class = TareaSerializer