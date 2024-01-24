from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from .models import History
import time
from .money import money, history


def index(request):
    money()
    time.sleep(10)
    return JsonResponse(history())

