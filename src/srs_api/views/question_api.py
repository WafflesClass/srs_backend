# -*- coding: utf-8 -*-
import copy

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import permissions, status
from django.forms.models import model_to_dict

from srs_lib.managers import poll_manager, qa_manager
from srs_lib.utils import api_response_data, api_err_handler

@permission_classes((AllowAny))
@api_view(["POST"])
@api_err_handler()
def reply(request, **kwargs):
    params_dict = copy.deepcopy(request.data)
    params_dict['question_id'] = kwargs['pk']
    reply, is_created = qa_manager.reply_question(**params_dict)
    return api_response_data(status.HTTP_200_OK, {'reply': model_to_dict(reply), 'is_created': is_created})

