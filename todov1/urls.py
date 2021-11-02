from django.urls import path
from todov1.views.todo_view import TodoView
from todov1.views.all_todo_view import allTodos
from todov1.views.register_view import RegisterView

urlpatterns = [
    path('signup/',RegisterView.as_view(),name="RegisterView"),
    path('todos/', TodoView.as_view(), name="TodoView"),
    path('todos/<int:pk>', TodoView.as_view(), name="getTodoById"),
    path('todos/all', allTodos.as_view(), name="alltheTodos"),
]
