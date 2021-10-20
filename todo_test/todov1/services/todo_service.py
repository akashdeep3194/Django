from todov1.serializers import TodosSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from todov1.models.todo_model import Todo

class TodoService():

    def get_all_todo(self,request,pk=0):

        user_id = request.user.id
        
        if pk != 0:
            queryset = get_object_or_404(Todo,pk=pk,user=user_id)
            serializer = TodosSerializer(queryset)
        else:
            queryset = Todo.objects.filter(user = user_id)
            serializer = TodosSerializer(queryset,many = True)
        return serializer.data

    def post_fn(self,request):
        user_id = request.user.id
        print(user_id)
        print(request)

        if type(request.data) is list:
            for ele in request.data:
                ele['user'] = user_id
            serialized_payload = TodosSerializer(data=request.data,many=True)

        elif type(request.data) is dict:
            request.data['user'] = user_id
            serialized_payload = TodosSerializer(data=request.data)

        return serialized_payload


    def put_fn(self,request,pk):
        user_id = request.user.id
        queryset = get_object_or_404(Todo,pk=pk, user = user_id)
        request.data["user"] = queryset.user.id
        serializer = TodosSerializer(queryset, data=request.data)
        return serializer


    def del_fn(self,request,pk):
        user_id = request.user.id
        queryset = get_object_or_404(Todo,pk = pk,user = user_id)
        queryset.delete()

