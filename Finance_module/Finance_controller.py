from Finance_module import FNS_parser

def check_handler_QR(request, user_id: str, type_id: int):
    '''
    Достает по запросу данные чека.
    Если правильно, сохраняет данные.
    Выдает эти данные для интерфейса.

    :param request: str | file - Вводные данные, [QRRAW или файл QR кода]
    :param user_id: str - Айди пользователя, который отправил запрос
    :param type_id: int - Тип запроса, 1 QRRAW, 2 QR код
    :return:
    '''
    response = FNS_parser.get_data(request, type_id)
    print(response)
    if len(response) == 2:
        return (response[0], response[1])

    organisation_name, total_sum, DT, products = response
    #TODO: Сюда вставить сохранение в базу данных
    response_code = 0
    response = {'organisation': organisation_name, 'total_sum': total_sum, 'datetime': DT,
                'products_list': products}
    return response_code, response
