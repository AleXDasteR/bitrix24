from fast_bitrix24 import Bitrix

my_file = open('B24pars_alls.txt', 'w', encoding='UTF-16')
try:
    b1 = Bitrix('webhook')
    b2 = Bitrix('webhook')
    contacts = b2.get_all('crm.contact.list', params={'select': ['NAME', 'LAST_NAME', 'PHONE', 'EMAIL']})
    contact = []
    for el in contacts:
        new_el = dict()
        for name in el:
            new_el[name] = el[name]
        contact.append(new_el)
finally:
    for i in range(len(contact)):
        try:
            try:
                print(contact[i]['NAME'], contact[i]['LAST_NAME'],
                      contact[i]['PHONE'][0]['VALUE'], contact[i]['EMAIL'][0]['VALUE'], sep=' | ', file=my_file)
            except KeyError:
                print(contact[i]['NAME'], contact[i]['LAST_NAME'], contact[i]['PHONE'][0]['VALUE'], sep=' | ',
                      file=my_file)
        except KeyError:
            print(contact[i]['NAME'], contact[i]['LAST_NAME'], sep=' | ', file=my_file)
my_file.close()
