# Татьяна Дробина, 18-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


# Функция создания заказа и сохранения трек-номера заказа
# Функция для создание заказа
def create_order(body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
# Cохраняем трек-номера заказа
track_number = create_order(data.order_body).json()["track"]

# Функция для получение заказа по номеру трекера
def get_order(track_number):
    response = requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH + str(track_number))
    return response
