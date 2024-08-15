import requests
import json
from Classes.product import Product_item
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN_PROVERKACHECKA = os.getenv('TOKEN_PROVERKACHECKA')
URL = 'https://proverkacheka.com/api/v1/check/get'

'''Получение данных чека по API'''


def get_check_data_by_qrraw(qrraw: str):
    '''
    Функция для доставания ответа из проверкичеков по чистой инфе.

    :param qrraw:
    :return response:
    '''

    data = {'token': TOKEN_PROVERKACHECKA, 'qrraw': qrraw}
    r = requests.post(URL, data=data)
    response = json.loads(r.text)
    return response


def get_check_data_by_QR_link(QR_link: str):
    '''
    Функция открывает файл, отдает его на API и возвращает назад ответ
    :param QR_link: str - ссылка на файл
    :return:
    '''
    data = {'token': TOKEN_PROVERKACHECKA}
    with open(f'../{QR_link}', 'rb') as f:
        r = requests.post(URL, data=data, files={'qrfile': f})
    response = json.loads(r.text)
    return response
def get_check_data_by_QR(QR_file):
    '''
    Функция открывает файл, отдает его на API и возвращает назад ответ
    :param QR_link: файл
    :return:
    '''
    data = {'token': TOKEN_PROVERKACHECKA}
    r = requests.post(URL, data=data, files={'qrfile': QR_file})
    response = json.loads(r.text)
    return response



def preproc_check_data(response: dict):
    '''
    :param:
    response: str
    :return:
    organization_name: str - название организации в которой произошла сделка,
    total_sum: int - конечная сумма чека,
    date_time_check: str - Дата и время в виде datetime,
    items: list[product] - с информацией о товарах с чека
    '''

    response_data = response['data']['json']
    total_sum = response_data['totalSum']
    organization_name = response_data['user']
    items = response_data['items']
    items = [Product_item(name=el['name'], price=el['price'], quantity=el['quantity'], sum=el['sum']) for el in items]
    date_time_check = response_data['dateTime']

    return organization_name, total_sum, date_time_check, items


def get_data(request: str, type: int):
    '''
    Функция принимает файл и тип файла, достает данные по файлу, проверяет успешно ли выполнен запрос, если нет,
    то возвращает -1 и тектовое описание ошибки

    :param request: str - запрос, [QRRAW | QRcode]
    :param type: int - тип запроса: 2 - QR код, 1 - QRRAW
    :return:
    tuple[str, int, datetime, list[product]] - при успешном запросе
    tuple[int, str] - при неудачном запросе
    '''
    if type == 1:
        responce = get_check_data_by_qrraw(request)
        if responce['code'] == 1:  # Успешный запрос
            data = preproc_check_data(responce)
            return data
        else:
            return -1, 'API не удалось прочитать чек'

    elif type == 2:
        try:
            responce = get_check_data_by_QR(request)
        except:
            return -2, 'Некорректная ссылка на QR код'
        if responce['code'] == 1:  # Успешный запрос
            data = preproc_check_data(responce)
            return data
        elif responce['code'] == 3:
            return -3, 'Превышено количество обращений по чеку'
        else:
            return -1, 'API не удалось прочитать чек'
    else:
        return -1, 'Такой тип запроса не поддерживается'
