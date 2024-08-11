from rest_framework import serializers
from task_list import Tarea

# Esta clase contiene el DTO
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
        