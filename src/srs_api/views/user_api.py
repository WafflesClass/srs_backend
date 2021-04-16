# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import permissions, status
from django.forms.models import model_to_dict

from srs_lib.managers import user_manager
from srs_lib.utils import api_response_data, api_err_handler
from srs_lib.constants import Result

# class UserMain(APIView):
#     permission_classes = (AllowAny, )

#     def post(self, request):
#         email = request.data.get('email', None)
#         password = request.data.get('password', None)
#         user = user_manager.create({
#             'email': email,
#             'password': password,
#         }
#         return api_response_data(Result.SUCCESS, {'user': user})

@permission_classes((AllowAny))
@api_view(["POST"])
@api_err_handler()
def sign_up(request):
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    # TODO: Make this param validation decorator
    if not email or not password:
        res = {'error': 'please provide a email and a password'}
        return api_response_data(status.HTTP_405_METHOD_NOT_ALLOWED, res)
    user = user_manager.create(
        email=email,
        password=password,
    )
    return api_response_data(status.HTTP_200_OK, {'user': model_to_dict(user)})

@permission_classes((AllowAny))
@api_view(["POST"])
@api_err_handler()
def log_in(request):
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    if not email or not password:
        res = {'error': 'please provide a email and a password'}
        return api_response_data(status.HTTP_405_METHOD_NOT_ALLOWED, res)
    is_authenticate, user = user_manager.verify(
        email=email,
        password=password,
    )
    if not is_authenticate:
        return api_response_data(status.HTTP_403_FORBIDDEN, {'error': 'Not authenticated'})
    # user = user_manager.get(email)
    user_details = user_manager.log_in(user, request)    
    return api_response_data(status.HTTP_200_OK, {'user_details': user_details})
