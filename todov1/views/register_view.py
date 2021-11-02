from logging import raiseExceptions
from django.http import response
from rest_framework import permissions
from rest_framework.views import APIView
from todov1.models.todo_model import Todo
from django.contrib.auth.models import User
from todov1.services.todo_service import TodoService
from rest_framework.response import Response
from todov1.serializers.todos_serializer import TodosSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.

class RegisterView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        payload = request.data

        username = payload['username']
        password = payload['password']

        try:
            user, created = User.objects.get_or_create(username=username)

            if created:
                user.set_password(password)
                user.save()
                # print(user)
                # print(type(user))
                # print("!!!!!!!!!!A")
                # print(created)
                return Response(data = {'username':user.username},status=status.HTTP_201_CREATED)
            else:
                return Response(data="User exists already",status=status.HTTP_409_CONFLICT)

        except Exception as e:

            print(e)
            return Response(data = "Something went wrong!",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
