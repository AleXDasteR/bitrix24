from fast_bitrix24 import Bitrix

my_file = open('B24pars_alls.txt', 'w', encoding='UTF-16')
filtered_result = []
try:
    b1 = Bitrix('webhook')
    b2 = Bitrix('webhook')
    deals = b1.get_all(
        'crm.deal.list',
        params={
            'select': ['ID', 'CONTACT_ID', 'TITLE']})
    contacts = b2.get_by_ID('crm.contact.list', [d['ID'] for d in deals],
                            params={'select': ['NAME', 'LAST_NAME', 'PHONE', 'EMAIL']})
    contact = []
    for el in deals:
        new_el = dict()
        for name in el:
            new_el[name] = el[name]
        filtered_result.append(new_el)
    for el in contacts:
        new_el = dict()
        for name in el:
            new_el[name] = el[name]
        contact.append(new_el)
finally:
    for i in range(len(filtered_result)):
        try:
            print(filtered_result[i]['TITLE'], contact[i]['NAME'],
                  contact[i]['PHONE'][0]['VALUE'], contact[i]['EMAIL'][0]['VALUE'], sep=' | ', file=my_file)
        except KeyError:
            try:
                print(filtered_result[i]['TITLE'], contact[i]['NAME'],
                      contact[i]['PHONE'][0]['VALUE'], sep=' | ', file=my_file)
            except KeyError:
                print(filtered_result[i]['TITLE'], contact[i]['NAME'],
                      sep=' | ', file=my_file)
my_file.close()
