from rest_framework import permissions, status
from django.http import JsonResponse

def api_response_data(result_code, reply=None):
    return JsonResponse({'result_code': result_code, 'reply': reply})

def api_err_handler():
    def _handler(func, *args, **kwargs):
        def _func(request, *args, **kwargs):
            try:
                return func(request, *args, **kwargs)
            except Exception as e:
                return JsonResponse({'result_code': status.HTTP_400_BAD_REQUEST, 'error': str(e)} )
        return _func
    return _handler            
