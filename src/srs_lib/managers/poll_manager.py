# coding=utf-8
import jwt, json

from myapp.models import Poll

def create(**kwargs):
    new_poll = Poll.objects.create(
        name=kwargs['name'][0],
        description=kwargs['description'][0],
        creator_id=kwargs['creator_id'][0]
    )
    return new_poll

def get_for_user(creator_id):
    polls = Poll.objects.filter(
        creator__id=creator_id
    )
    return polls

