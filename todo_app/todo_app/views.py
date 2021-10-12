from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def index(request):
    message = "This is a test message"
    return Response(data=message,status=status.HTTP_200_OK)
