# coding=utf-8
import jwt, json

from myapp.models import Poll, Question, Answer, Reply

def create(**kwargs):
    new_question = Question.objects.create(
        content=kwargs['content'][0],
        question_type=kwargs['type'][0],
        poll_id=kwargs['poll_id'][0],
    )
    question_id = new_question.id
    correct_ans_l, wrong_ans_l = [], []
    for correct_answer in kwargs['correct_answers']:
        correct_ans_l.append(
            Answer.objects.create(
                content=correct_answer,
                question_id=question_id,
                is_correct=True,
            )
        )
    for wrong_answer in kwargs['wrong_answers']:
        wrong_ans_l.append(
            Answer.objects.create(
                content=wrong_answer,
                question_id=question_id,
                is_correct=False,
            )
        )   
    return new_question, correct_ans_l, wrong_ans_l

def get_for_poll(poll_id):
    questions = Question.objects.filter(
        poll__id=poll_id
    )
    return questions

def reply_question(**kwargs):
    new_reply, is_created = Reply.objects.update_or_create(
        question_id=kwargs['question_id'][0],
        creator_id=kwargs['creator_id'][0],
        defaults={'content': kwargs['content'][0]},
    )
    return new_reply, is_created
