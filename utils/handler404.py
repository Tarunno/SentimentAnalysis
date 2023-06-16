from django.http import JsonResponse

def error_404(request, exception):
    message = 'invalid endpoint'

    response = JsonResponse(data={'message':message, 'status_code': 404})
    response.status_code = 404 
   
    return response