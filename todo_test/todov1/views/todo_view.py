from rest_framework.views import APIView
from todov1.models.todo_model import Todo
from todov1.services.todo_service import TodoService
from rest_framework.response import Response
from todov1.serializers import TodosSerializer
from rest_framework import status


# Create your views here.

class TodoView(APIView):

    todo_service = TodoService()
    
    def get(self, request, pk=0):

        response = self.todo_service.get_all_todo(request,pk)
        return Response(data=response, status = status.HTTP_200_OK)
        

    def post(self, request):

        response = self.todo_service.post_fn(request)

        try:
            if response.is_valid():
                response.save()
                return Response(data = response.data,status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(response.errors, status= status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        response_serial = self.todo_service.put_fn(request, pk)
        try:
            if response_serial.is_valid():
                response_serial.save()
                return Response(data = response_serial.data,status=status.HTTP_200_OK)
            else:
                return Response(response_serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(response_serial.errors, status= status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):

        self.todo_service.del_fn(request, pk)
        return Response(data="Deleted",status=status.HTTP_204_NO_CONTENT)

