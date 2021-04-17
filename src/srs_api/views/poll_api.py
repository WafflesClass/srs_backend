# -*- coding: utf-8 -*-
import copy

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import permissions, status
from django.forms.models import model_to_dict

from srs_lib.managers import poll_manager, qa_manager
from srs_lib.utils import api_response_data, api_err_handler


###########################################################################################################
def poll_main(request):
    function_mappings = {
        'POST': create_poll,
        'GET': get_user_polls,
    }

    if request.method in function_mappings:
        return function_mappings[request.method](request)
    return api_response_data(status.HTTP_404_NOT_FOUND, {'err': 'Not supported request method'})

@permission_classes((AllowAny))
@api_view(["POST"])
@api_err_handler()
def create_poll(request):
    poll = poll_manager.create(**request.data)
    return api_response_data(status.HTTP_200_OK, {'poll': model_to_dict(poll)})

@permission_classes((AllowAny))
@api_view(["GET"])
@api_err_handler()
def get_user_polls(request):
    polls = poll_manager.get_for_user(creator_id=request.data['creator_id'])
    polls = [model_to_dict(x) for x in polls]
    return  api_response_data(status.HTTP_200_OK, {'polls': polls})
###########################################################################################################


###########################################################################################################
def qa_main(request, **kwargs):
    function_mappings = {
        'POST': create_qa,
        'GET': get_poll_qas,
    }
        
    if request.method in function_mappings:
            return function_mappings[request.method](request, **kwargs)
    return api_response_data(status.HTTP_404_NOT_FOUND, {'err': 'Not supported request method'})

@permission_classes((AllowAny))
@api_view(["POST"])
@api_err_handler()
def create_qa(request, **kwargs):
    params_dict = copy.deepcopy(request.data)
    params_dict['poll_id'] = kwargs['pk']
    new_question, correct_ans_l, wrong_ans_l = qa_manager.create(**params_dict)
    correct_ans_l = [model_to_dict(x) for x in correct_ans_l] # TODO: Delegate this model_to_dict logic to api_response_data
    wrong_ans_l = [model_to_dict(x) for x in wrong_ans_l] 
    return api_response_data(
        status.HTTP_200_OK, 
        {'new_question': model_to_dict(new_question), 'correct_ans_l': correct_ans_l, 'wrong_ans_l': wrong_ans_l})

@permission_classes((AllowAny))
@api_view(["GET"])
@api_err_handler()
def get_poll_qas(request, **kwargs):
    poll_id = kwargs['pk']
    questions = qa_manager.get_for_poll(poll_id)
    questions = [model_to_dict(x) for x in questions]
    return api_response_data(status.HTTP_200_OK, {'questions': questions})
###########################################################################################################


