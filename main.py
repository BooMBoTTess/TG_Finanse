import Finance_module
from Classes import product


'''Главный запускала всего'''

if __name__ == "__main__":
    test_responce = {'code': 1, 'first': 0, 'data': {'json': {'user': 'Акционерное общество "Тандер"', 'items': [
        {'sum': 2599, 'name': 'МОЯ ЦЕНА Уксус столовый 9% 1л пл/б', 'price': 2599, 'quantity': 1, 'modifiers': [],
         'properties': []},
        {'sum': 5499, 'name': 'HEINZ Кетчуп острый дой-пак 350 г(', 'price': 5499, 'quantity': 1, 'modifiers': [],
         'properties': []},
        {'sum': 5999, 'name': 'HEINZ Кетчуп для гриля и шашлыка д', 'price': 5999, 'quantity': 1, 'modifiers': [],
         'properties': []},
        {'sum': 10998, 'name': 'ДОМИК В ДЕРЕВНЕ Сметана 15% 300г п', 'price': 5499, 'quantity': 2, 'modifiers': [],
         'properties': []},
        {'sum': 2899, 'name': 'Хлеб Бабушкин нарез 230г п/уп(Смак', 'price': 2899, 'quantity': 1, 'modifiers': [],
         'properties': []},
        {'sum': 6999, 'name': 'EAT MEAT/СЕМ СЕКР Свинина нежная к', 'price': 6999, 'quantity': 1, 'modifiers': [],
         'properties': []}], 'nds10': 1900, 'nds18': 2350, 'message': [],
                                                              'rawData': 'AwAXAxEEEAA5MjgyNDQwMzAwNjgyODM4DQQUADAwMDAyNjQ5NzEwMDc2NDUgICAg+gMMADIzMTAwMzE0NzUgIBAEBADGtQAA9AMEAEznbF81BAYAMQRL4Lq5DgQEAIgAAAASBAQArwEAAB4EAQAB/AMCALGIIwRKAAYEIgCMjp8gloWNgCCTquHj4SDh4q6rrqLrqSA5JSAxqyCvqy+hNwQCACcK/wMEAAZAQg8TBAIAJwqvBAEAAbAEAgCxAb4EAQAEIwRKAAYEIgBIRUlOWiCKpeLn468gruHi4OupIKSuqS2voKogMzUwIKMoNwQCAHsV/wMEAAZAQg8TBAIAexWvBAEAAbAEAgCVA74EAQAEIwRKAAYEIgBIRUlOWiCKpeLn468gpKvvIKPgqKvvIKgg6KDoq+uqoCCkNwQCAG8X/wMEAAZAQg8TBAIAbxevBAEAAbAEAgDoA74EAQAEIwRKAAYEIgCEjoyIiiCCIISFkIWCjYUgkayl4qCtoCAxNSUgMzAwoyCvNwQCAHsV/wMEAAaAhB4TBAIA9iqvBAEAArAEAgDoA74EAQAEIwRKAAYEIgCVq6WhIIGgoePoqqitIK2g4KWnIDIzMKMgry/jryiRrKCqNwQCAFML/wMEAAZAQg8TBAIAUwuvBAEAArAEAgAIAb4EAQAEIwRKAAYEIgBFQVQgTUVBVC+RhYwgkYWKkCCRoqitqK2gIK2lpq2g7yCqNwQCAFcb/wMEAAZAQg8TBAIAVxuvBAEAArAEAgB8Ar4EAQAE/QMRAI/grqSgoqXmIJGl4KWjqK2gBwQBAAA5BAIAsYi/BAEAAMAEAQAAwQQBAAAkBAwAd3d3Lm5hbG9nLnJ1owQXAIygo6CnqK0gIIygo62o4iAggK2qrq2guQQBAAJOBAIALglPBAIAbAcYBB0AgKrmqK6tpeCtrqUgrqHppeHioq4gIpKgraSl4CLxAz0ANjIyMDAyLCCRoqXgpKuuouGqoO8grqGrLCCNqKatqKkgkqCjqKsgoywggeuqrqKgIOOrLCCkrqwg/CAxOB8EAQABgQYc1e7N9Qc=',
                                                              'userInn': '2310031475',
                                                              'dateTime': '2020-09-24T18:37:00',
                                                              'kktRegId': '0000264971007645', 'metadata': {
            'id': '20200924d8740ba5d19c168802b147b88fca3e497dd24f917677b86547539b38329846ef',
            '_id': {'$oid': '5f6ca111fc8edb088943a68c'}, 'fsId': '9282440300682838', 'ofdId': 'ofd26',
            'subtype': 'receipt', 'kktRegId': '0000264971007645', 'documentId': 46534,
            'receiveDate': {'$date': 1600954641485},
            'v2ValidateErr': '["#/: Additional properties not allowed: receipt"]', 'protocolVersion': '2',
            'protocolSubversion': 1}, 'operator': 'Продавец Серегина', 'totalSum': 34993, 'modifiers': [],
                                                              'fiscalSign': 1273019065, 'properties': [],
                                                              'receiptCode': 3, 'shiftNumber': 136, 'stornoItems': [],
                                                              'cashTotalSum': 0, 'taxationType': 1,
                                                              'ecashTotalSum': 34993, 'operationType': 1,
                                                              'requestNumber': 431, 'senderAddress': 'ofd@magnit.ru',
                                                              'fiscalDriveNumber': '9282440300682838',
                                                              'retailPlaceAddress': '622002, Свердловская обл, Нижний Тагил г, Быкова ул, дом № 18',
                                                              'fiscalDocumentNumber': 46534},
                                                     'html': '<table class="b-check_table table"><tbody><tr class="b-check_vblock-middle b-check_center"><td colspan="5">Акционерное общество "Тандер"</td></tr><tr class="b-check_vblock-middle b-check_center"><td colspan="5">622002, Свердловская обл, Нижний Тагил г, Быкова ул, дом № 18</td></tr><tr class="b-check_vblock-middle b-check_center"><td colspan="5">ИНН 2310031475</td></tr><tr class="b-check_vblock-middle b-check_center"><td colspan="5">&nbsp;</td></tr><tr class="b-check_vblock-middle b-check_center"><td colspan="5">24.09.2020 18:37</td></tr><tr class="b-check_vblock-middle b-check_center"><td colspan="5">Чек № 431</td></tr><tr class="b-check_vblock-middle b-check_center"><td colspan="5">Смена № 136</td></tr><tr class="b-check_vblock-middle b-check_center"><td colspan="5">Кассир Продавец Серегина</td></tr><tr class="b-check_vblock-last b-check_center"><td colspan="5">Приход</td></tr><tr><td><strong>№</strong></td><td><strong>Название</strong></td><td><strong>Цена</strong></td><td><strong>Кол.</strong></td><td><strong>Сумма</strong></td></tr><tr class="b-check_item"><td>1</td><td>МОЯ ЦЕНА Уксус столовый 9% 1л пл/б</td><td>25.99</td><td>1</td><td>25.99</td></tr><tr class="b-check_item"><td>2</td><td>HEINZ Кетчуп острый дой-пак 350 г(</td><td>54.99</td><td>1</td><td>54.99</td></tr><tr class="b-check_item"><td>3</td><td>HEINZ Кетчуп для гриля и шашлыка д</td><td>59.99</td><td>1</td><td>59.99</td></tr><tr class="b-check_item"><td>4</td><td>ДОМИК В ДЕРЕВНЕ Сметана 15% 300г п</td><td>54.99</td><td>2</td><td>109.98</td></tr><tr class="b-check_item"><td>5</td><td>Хлеб Бабушкин нарез 230г п/уп(Смак</td><td>28.99</td><td>1</td><td>28.99</td></tr><tr class="b-check_item"><td>6</td><td>EAT MEAT/СЕМ СЕКР Свинина нежная к</td><td>69.99</td><td>1</td><td>69.99</td></tr><tr class="b-check_vblock-first"><td colspan="3" class="b-check_itogo">ИТОГО:</td><td></td><td class="b-check_itogo">349.93</td></tr><tr class="b-check_vblock-middle"><td colspan="3">Наличные</td><td></td><td>0.00</td></tr><tr class="b-check_vblock-middle"><td colspan="3">Карта</td><td></td><td>349.93</td></tr><tr class="b-check_vblock-middle"><td colspan="3">НДС итога чека со ставкой 20%</td><td></td><td>23.50</td></tr><tr class="b-check_vblock-middle"><td colspan="3">НДС итога чека со ставкой 10%</td><td></td><td>19.00</td></tr><tr class="b-check_vblock-last"><td colspan="5">ВИД НАЛОГООБЛОЖЕНИЯ: ОСН</td></tr><tr class="b-check_vblock-first"><td colspan="5">РЕГ.НОМЕР ККТ: 0000264971007645</td></tr><tr class="b-check_vblock-middle"><td colspan="5">ЗАВОД. №: </td></tr><tr class="b-check_vblock-middle"><td colspan="5">ФН: 9282440300682838</td></tr><tr class="b-check_vblock-middle"><td colspan="5">ФД: 46534</td></tr><tr class="b-check_vblock-middle"><td colspan="5">ФПД#: 1273019065</td></tr><tr class="b-check_vblock-last"><td colspan="5" class="b-check_center"><img Finance_module="/qrcode/generate?text=t%3D20200924T1837%26s%3D349.93%26fn%3D9282440300682838%26i%3D46534%26fp%3D1273019065%26n%3D1" alt="QR код чека" width="35%" loading="lazy" decoding="async"></td></tr></tbody></table>'},
                     'request': {'qrurl': '', 'qrfile': '',
                                 'qrraw': 't=20200924t1837&s=349.93&fn=9282440300682838&i=46534&fp=1273019065&n=1',
                                 'manual': {'fn': '9282440300682838', 'fd': '46534', 'fp': '1273019065',
                                            'check_time': '20200924t1837', 'type': '1', 'sum': '349.93'}}}

    test_preproced_check_data = ('Акционерное общество "Тандер"', 34993, '2020-09-24T18:37:00', ["Название: МОЯ ЦЕНА Уксус столовый 9% 1л пл/б, цена: 2599, количество: 1, стоимость: 2599", "Название: HEINZ Кетчуп острый дой-пак 350 г(, цена: 5499, количество: 1, стоимость: 5499", "Название: HEINZ Кетчуп для гриля и шашлыка д, цена: 5999, количество: 1, стоимость: 5999", "Название: ДОМИК В ДЕРЕВНЕ Сметана 15% 300г п, цена: 5499, количество: 2, стоимость: 10998", "Название: Хлеб Бабушкин нарез 230г п/уп(Смак, цена: 2899, количество: 1, стоимость: 2899", "Название: EAT MEAT/СЕМ СЕКР Свинина нежная к, цена: 6999, количество: 1, стоимость: 6999"])

    print(Finance_module.preproc_check_data(test_responce))

    test_request = 't=20200924T1837&s=349.93&fn=9282440300682838&i=46534&fp=1273019065&n=1'