import logging
from rest_framework.exceptions import ValidationError
from todov1.serializers.todos_serializer import TodosSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from todov1.models.todo_model import Todo
from rest_framework import status
from typing import List

class TodoService():
    
    logger = logging.getLogger(__name__)

    def get_all_todo(self,user_id:int) -> List[Todo]:

        queryset = Todo.objects.filter(user = user_id)
        serializer = TodosSerializer(queryset,many = True)
        return serializer.data

    def get_todo_by_id(self,user_id:int,pk:int) -> Todo:
    
        queryset = get_object_or_404(Todo,pk=pk,user=user_id)
        serializer = TodosSerializer(queryset)
        return serializer.data

    def create_todo(self, payload:dict, user_id:int) -> Todo:


        payload['user'] = user_id
        serialized_payload = TodosSerializer(data=payload)
        if serialized_payload.is_valid():
            serialized_payload.save()
        else:
            raise ValidationError("Bad Request: "+str(serialized_payload.errors))
            # return Response(serialized_payload.errors, status=status.HTTP_400_BAD_REQUEST)

        return serialized_payload

    def create_multiple_todos(self,payload: list, user_id:int) -> Todo:
            
        for ele in payload:
            ele['user'] = user_id

        serialized_payload = TodosSerializer(data=payload,many=True)
        print(serialized_payload)

        if not(serialized_payload.is_valid()):
            return ValidationError("Bad Request: "+str(serialized_payload.errors))
            # return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serialized_payload.save()
        return serialized_payload




    def update_todo(self,payload,user_id:int ,pk:int):

        try:
            queryset = get_object_or_404(Todo,pk=pk, user = user_id)
            payload["user"] = queryset.user.id
            serializer = TodosSerializer(queryset, data=payload)
            if not(serializer.is_valid()):
                raise ValidationError("Bad Request: "+str(serializer.errors))
                # return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise Exception("Something went wrong")
            logger.error(e)
            # return Response(e.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        return serializer


    def delete_todo(self,user_id,pk):
        queryset = get_object_or_404(Todo,pk = pk,user = user_id)
        queryset.delete()


