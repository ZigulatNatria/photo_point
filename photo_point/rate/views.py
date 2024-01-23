from django.shortcuts import render
from django.http import JsonResponse
from .models import History


def index(request):
    response_data = {}
    # response_data['result'] = 'error'
    # response_data['message'] = 'Some error message'
    all_history = History.objects.all()
    for i in all_history:
        response_data[f'reguest{i.id}'] = i.history
    return JsonResponse(response_data)
