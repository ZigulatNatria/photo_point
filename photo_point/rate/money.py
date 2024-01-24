import requests
import json
from .models import History
import time


def money():
    r = requests.get('https://v6.exchangerate-api.com/v6/7cd5fc1a10c769e9cf7193ec/pair/USD/RUB')
    rq = json.loads(r.content)
    rq_filter = dict(filter(lambda item: item[0] in ('base_code', 'target_code', 'conversion_rate'), rq.items()))
    History.objects.create(history=rq_filter)
    time.sleep(5)


def history():
    response_data = {}
    all_history = History.objects.all()[0:11]
    last_request = all_history[0].id

    for i in all_history:
        response_data[f'request{i.id}'] = i.history
    current_data = response_data[f'request{last_request}']
    last_request_key = list(response_data.keys())[0]
    response_data.pop(last_request_key)
    grate_data = {
        'current_request': current_data,
        'history_request': response_data,
    }

    return grate_data