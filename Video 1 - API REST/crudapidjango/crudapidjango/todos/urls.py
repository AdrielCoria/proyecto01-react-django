from todos import views
from django.urls import path
urlpatterns = [
    path('todos/', views.TodosAPIView.as_view()),
    path('todo/<int:pk>/', views.TodoAPIView.as_view()),
]