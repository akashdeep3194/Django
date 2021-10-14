from django.shortcuts import render, get_object_or_404
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
        sid = request.query_params.get('id',0)
        print(sid)

        if sid != 0:
            queryset = get_object_or_404(Todos,id = sid)
            serializer = TodosSerializer(queryset)
        else:
            queryset = self.get_objects()
            serializer = TodosSerializer(queryset,many = True)

        return Response(data=serializer.data, status = status.HTTP_200_OK)

    def post(self,request):
        serialized_payload = TodosSerializer(data=request.data)
        try:
            if serialized_payload.is_valid():
                serialized_payload.save()
                return Response(data = serialized_payload.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serialized_payload.errors, status= status.HTTP_404_NOT_FOUND)

        queryset = self.get_objects()

