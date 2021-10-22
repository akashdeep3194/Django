from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from todov1.models.todo_model import Todo
from todov1.services.todo_service import TodoService
from rest_framework.response import Response
from todov1.serializers.todos_serializer import TodosSerializer


class allTodos(APIView):

    def get(self, request):

        queryset = Todo.objects.all()

        if queryset.count() == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = TodosSerializer(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):

        queryset = Todo.objects.all()

        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
