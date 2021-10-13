from django.urls import path
from todov1.views import myTodos

urlpatterns = [
    path('todos/',myTodos.as_view(),name = "mytodos")
]
