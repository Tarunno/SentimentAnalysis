from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed, NotFound


def custom_exception_handler(exc, context):
    if isinstance(exc, MethodNotAllowed):
        response_data = {
            'message': 'Http method not allowed',
            'status_code': 405
        }
        return Response(response_data, status=405)
    
    return exception_handler(exc, context)