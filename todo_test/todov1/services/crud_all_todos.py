from todov1.serializers import TodosSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from todov1.models.models import Todos

class apiService():

    def get_fn(self,request,pk=0):

        if pk != 0:
            queryset = get_object_or_404(Todos,pk=pk)
            serializer = TodosSerializer(queryset)

        else:
            queryset = Todos.objects.all()
            serializer = TodosSerializer(queryset,many = True)
            
        return Response(data=serializer.data, status = status.HTTP_200_OK)

    def post_fn(self,request):
        serialized_payload = TodosSerializer(data=request.data,many=True)
        try:
            if serialized_payload.is_valid():
                serialized_payload.save()
                return Response(data = serialized_payload.data,status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(serialized_payload.errors, status= status.HTTP_404_NOT_FOUND)

    def put_fn(self,request,pk):
        queryset = get_object_or_404(Todos,pk=pk)
        serializer = TodosSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def del_fn(self,request,pk):
        queryset = get_object_or_404(Todos,pk = pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
