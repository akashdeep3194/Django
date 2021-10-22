from todov1.serializers.todos_serializer import TodosSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from todov1.models.todo_model import Todo
from rest_framework import status

class TodoService():

    def get_all_todo(self,user_id:int) -> "list[Todo]":
        queryset = Todo.objects.filter(user = user_id)
        serializer = TodosSerializer(queryset,many = True)
        return serializer.data

    def get_todo_by_id(self,user_id:int,pk:int) -> Todo:
    
        queryset = get_object_or_404(Todo,pk=pk,user=user_id)
        serializer = TodosSerializer(queryset)

        return serializer.data

    def post_single_todo(self, payload:dict, user_id:int) -> Todo:


        try:
            payload['user'] = user_id
            print(payload)
            serialized_payload = TodosSerializer(data=payload)
            if serialized_payload.is_valid():
                serialized_payload.save()
            else:
                return Response(serialized_payload.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        return serialized_payload

    def post_multiple_todos(self,payload: list, user_id:int) -> Todo:
        try:
            for ele in payload:
                ele['user'] = user_id
            serialized_payload = TodosSerializer(data=payload,many=True)

            if not(serialized_payload.is_valid()):
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(serialized_payload.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        return serialized_payload




    def put_todo(self,payload,user_id:int ,pk:int):

        try:
            queryset = get_object_or_404(Todo,pk=pk, user = user_id)
            payload["user"] = queryset.user.id
            serializer = TodosSerializer(queryset, data=payload)
            if not(serializer.is_valid()):
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        return serializer


    def del_todo(self,request,pk):
        user_id = request.user.id
        queryset = get_object_or_404(Todo,pk = pk,user = user_id)
        queryset.delete()

