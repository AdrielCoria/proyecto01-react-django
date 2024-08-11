from django.db import models

# Create your models here.
# Acá definimos todos los modelos que van a ir a la base de datos.

# Tipos de datos
# CharField: Text
# BooleanField: Boleano


# Definimos una clase que contenga los datos de las tareas
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    listo = models.BooleanField(default=False)
    
    
