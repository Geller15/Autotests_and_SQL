import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)  # создаем новый заказ


response = post_new_order(data.order_body)
print(response.status_code)
print(response.json())

order_track = (response.json()['track'])  # сохраняем трек нового заказа в переменной
print(order_track)


def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_FROM_TRACK + '?t=' + str(order_track))
# Получаем информацию о заказе по его номеру трека


response = get_order()
print(response.status_code)
print(response.json())
