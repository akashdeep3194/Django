from logging import raiseExceptions
from rest_framework.views import APIView
from todov1.models.todo_model import Todo
from todov1.services.todo_service import TodoService
from rest_framework.response import Response
from todov1.serializers.todos_serializer import TodosSerializer
from rest_framework import status


# Create your views here.

class TodoView(APIView):

    todo_service = TodoService()
    
    def get(self, request, pk=0):
        # raise Exception("Test Error")
        # print("Y")
        user_id = request.user.id
        if pk == 0:
            response = self.todo_service.get_all_todo(user_id)
        else:
            response = self.todo_service.get_todo_by_id(user_id, pk)

        return Response(data=response, status = status.HTTP_200_OK)
        

    def post(self, request):

        payload = request.data
        user_id = request.user.id
        print(type(payload))
        if type(payload) is list:
            response = self.todo_service.create_multiple_todos(payload, user_id)
        elif type(payload) is dict:
            response = self.todo_service.create_todo(payload, user_id)

        if response.is_valid():
            return Response(data = response.data,status=status.HTTP_201_CREATED)

    def put(self, request, pk): # do not use request inside service

        response_serial = self.todo_service.update_todo(payload=request.data,user_id=request.user.id, pk=pk)

        if response_serial.is_valid():
            response_serial.save()
            return Response(data = response_serial.data,status=status.HTTP_200_OK)
        else:
            return Response(response_serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        self.todo_service.delete_todo(request.user.id,pk)
        return Response(data="Deleted",status=status.HTTP_204_NO_CONTENT)

