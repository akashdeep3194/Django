from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from todov1.models.models import Todos
from .services.crud_all_todos import apiService
from rest_framework.response import Response
from todov1.serializers import TodosSerializer

# Create your views here.

class myTodos(APIView):

    def get(self,request,pk=0):
        service = apiService()
        response = apiService.get_fn(self, request,pk)
        return response

    def post(self,request):

        service = apiService()
        response = apiService.post_fn(self, request)
        return response

    def put(self,request,pk):
        service = apiService()
        response = apiService.put_fn(self, request,pk)
        return response

    def delete(self,request,pk):
        service = apiService()
        response = apiService.del_fn(self, request,pk)
        return response

class allTodos(APIView):

    def get(self,request):
        queryset = Todos.objects.all()
        if queryset.count() == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = TodosSerializer(queryset,many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self,request):
        queryset = Todos.objects.all()
        queryset.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
