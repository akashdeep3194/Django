from django.urls import path
from todov1.views.todo_view import TodoView
from todov1.views.all_todo_view import allTodos

urlpatterns = [
    path('todos/',TodoView.as_view(),name = "TodoView"),
    path('todos/<int:pk>',TodoView.as_view(),name = "getTodoById"),
    path('todos/all',allTodos.as_view(),name = "alltheTodos"),
]
