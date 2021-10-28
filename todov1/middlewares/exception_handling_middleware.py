from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
import logging


def exception_handler_middleware(get_response):
    
    def exception_handling(request):
        # try:
        print("Alpha!!!!!!!!")
        response = get_response(request)
        print(response)
        print("Beta!!!!!!!")

        # except ValidationError as e:
        #     return Response("Bad Request"+e,status=status.HTTP_400_BAD_REQUEST)

        # except Exception as e:
        #     print("Done!!!!!!!!!")
        #     logger.error(e)
        #     return Response("Something went wrong",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response

    def process_exception(request, exception:Exception):
        print("Exception can be handled here!")
        logger = logging.getLogger(__name__)
        # logger.error(exception)
        # return Response("Something went Wrong!",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return HttpResponse("Something went wrong",status=500)

    exception_handling.process_exception = process_exception

    return exception_handling
