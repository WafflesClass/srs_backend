def api_response_data(result_code, reply=None):
    from django.http import JsonResponse
    return JsonResponse({'result_code': result_code, 'reply': reply})
