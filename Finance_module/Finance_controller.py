import FNS_parser

def check_handler_QR(self, request: str, user_id: str, type_id: int):
    '''
    Достает по запросу данные чека.
    Если правильно, сохраняет данные.
    Выдает эти данные для интерфейса.

    :param request: str - Вводные данные, ссылка на QR код
    :param user_id: str - Айди пользователя, который отправил запрос
    :param type_id: int - Тип запроса, 1 QRRAW, 2 QR код
    :return:
    '''
    response = FNS_parser.get_data(request, type_id)
    if response[0] == -1:
        return (response[0], response[1])

    organisation_name, total_sum, DT, products = response
    print(organisation_name, user_id, total_sum, DT, products)
    #TODO: Сюда вставить сохранение в базу данных
    return organisation_name, total_sum, DT, products
