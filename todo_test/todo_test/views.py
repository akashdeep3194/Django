from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view(['POST','GET'])
def index(request):
    message = "This is a test GET request"
    print(request.user,request.auth)
    if request.method == "GET":
        return Response(data=message,status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        return Response(data = data,status=status.HTTP_200_OK)
    else:
        return Response(data="Method is incorrect")

class Message(APIView):
    def get(self,request):
        print("Hit by GET",request.auth,request.user)
        return Response(data="This is a class based view",status=status.HTTP_200_OK)
    def post(self,request):
        print("Hit by POST",request.data,request.auth,request.user)
        return Response(data="This is also a class based view",status=status.HTTP_200_OK)
