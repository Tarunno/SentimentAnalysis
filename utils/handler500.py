from django.http import JsonResponse

def error_500(request):
    message = 'server error'

    response = JsonResponse(data={'message':message, 'status_code': 500})
    response.status_code = 500
     
    return response