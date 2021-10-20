from todov1.serializers import TodosSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from todov1.models.models import Todos

class TodoService():#TodoService filename-todo_service

    def get_fn(self,request,pk=0):
        
        user=request.user

        if pk != 0:
            queryset = get_object_or_404(Todos,pk=pk,created_by=user)
            serializer = TodosSerializer(queryset)

        else:
            user = request.user
            queryset = Todos.objects.filter(created_by = user)
            serializer = TodosSerializer(queryset,many = True)
            
        return Response(data=serializer.data, status = status.HTTP_200_OK)

    def post_fn(self,request):
        user = request.user.username
        if type(request.data) is list:
            for ele in request.data:
                ele['created_by'] = user
            serialized_payload = TodosSerializer(data=request.data,many=True)

        elif type(request.data) is dict:
            request.data['created_by'] = user
            serialized_payload = TodosSerializer(data=request.data)

        try:
            if serialized_payload.is_valid():
                serialized_payload.save()
                return Response(data = serialized_payload.data,status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(serialized_payload.errors, status= status.HTTP_404_NOT_FOUND)

    def put_fn(self,request,pk):
        user = request.user
        queryset = get_object_or_404(Todos,pk=pk,created_by = user)
        serializer = TodosSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def del_fn(self,request,pk):
        user = request.user
        queryset = get_object_or_404(Todos,pk = pk,created_by = user)
        queryset.delete()
        return Response(data="Deleted",status=status.HTTP_204_NO_CONTENT)

