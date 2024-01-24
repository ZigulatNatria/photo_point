from django.http import JsonResponse
from .money import money, history


def index(request):
    money()
    return JsonResponse(history())

