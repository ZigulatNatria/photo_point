import requests
import json
from .models import History
import datetime
from django.core.cache import cache


def money():
    if not cache.get('time_10'):   # если кэш чист делаем запрос
        cache.set('time_10', 1, 10)  # закидываем данные в кэш (можно вообще любые) и ставим таймер очистки на 10 секунд
        r = requests.get('https://v6.exchangerate-api.com/v6/7cd5fc1a10c769e9cf7193ec/pair/USD/RUB')
        rq = json.loads(r.content)  # получаем JSON
        rq_filter = dict(filter(lambda item: item[0] in ('base_code', 'target_code', 'conversion_rate'), rq.items())) # фильтруем только нужные данные
        rq_filter['time_request'] = str(datetime.datetime.now())  # добавляем дату и время преобразованную в строку в JSON
        History.objects.create(history=rq_filter)   # записываем данные в базу


def history():
    response_data = {}
    all_history = History.objects.all()[0:11]    # делаем срез 11 записей из базы данных (десять для истории и одинацатый текущий)
    last_request = all_history[0].id             # получаем id последнего запроса (он всегда первый т.е. order_by = '-id')

# делаем красивый словарик :)
    for i in all_history:
        response_data[f'request{i.id}'] = i.history
    current_data = response_data[f'request{last_request}']
    last_request_key = list(response_data.keys())[0]
    response_data.pop(last_request_key)     # убираем из истории последний(текущий запрос)
    grate_data = {
        'current_request': current_data,    # текущий запрос
        'history_request': response_data,   # история запросов последние 10 не считая текущего
    }

    return grate_data