# coding=utf-8
import jwt, json

from django.contrib.auth import get_user_model, authenticate
from rest_framework_jwt.utils import jwt_payload_handler
from django.contrib.auth.signals import user_logged_in

from myapp.models import *

SECRET_KEY = 's_-aro!sw@)bob$tojdq!s61$+3s22y=dbe!b5y3!p4ch&y3k#'

def generate_token(user):
    payload = jwt_payload_handler(user)
    return jwt.encode(payload, SECRET_KEY)

def create(**kwargs):
    new_user = User.objects.create_user(**kwargs)
    return new_user

# def get(email):
#     user = User.objects.get(email=email)
#     return user

def verify(**kwargs):
    email, password = kwargs['email'], kwargs['password']
    user = User.objects.get(email=email)
    is_authenticate = authenticate(email=email, password=password)
    return is_authenticate, user

def log_in(user, request):
    token = generate_token(user)
    user_details = {}
    user_details['id'] = str(user.id)
    user_details['token'] = token.decode('utf8')
    user_logged_in.send(sender=user.__class__, request=request, user=user)
    return user_details
