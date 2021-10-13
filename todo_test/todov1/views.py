from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todov1.models import Todos
from todov1.serializers import TodosSerializer

# Create your views here.

class myTodos(APIView):
    def get_objects(self):
        try:
            return Todos.objects.all()
        except Todos.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self,request):
        queryset = self.get_objects()
        serializer = TodosSerializer(queryset,many = True)
        return Response(data=serializer.data, status = status.HTTP_200_OK)
