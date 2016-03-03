from re import compile, search
from string import ascii_letters, digits

NAME = compile(r'<(.+)>')
PHONE = compile(r'\+(\d\d?-\d{3}-\d{3}-\d{4})')
VALID = set(ascii_letters + digits + ' .-')


def phone(strng, num):
    result = {}
    for a in strng.rstrip().split('\n'):
        name = search(NAME, a).group(1)
        address = a.replace(name, '')
        phone_num = search(PHONE, a).group(1)
        address = ' '.join(''.join(b if b in VALID else ' ' for b in
                                   address.replace(phone_num, '')).split())
        if phone_num in result:
            result[phone_num]['duplicate'] = True
        else:
            result[phone_num] = {
                'name': name, 'address': address, 'duplicate': False}
    try:
        match = result[num]
        if match['duplicate']:
            return 'Error => Too many people: {}'.format(num)
        return 'Phone => {}, Name => {}, Address => {}'.format(
            num, match['name'], match['address'])
    except KeyError:
        return 'Error => Not found: {}'.format(num)
