from django.urls import path
from task_list import views

# Definimos las reglas de navegación 
urlpatterns = [
    path('tareas/', views.TareasAPIView.as_view()),
    path('tarea/<int:pk>', views.TareaAPIView.as_view()),
]