from django.shortcuts import render
from rest_framework import generics
from todos.models import Todo
from todos import serializer

# Create your views here.
class TodosAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = serializer.TodoSerializer

class TodoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = serializer.TodoSerializer