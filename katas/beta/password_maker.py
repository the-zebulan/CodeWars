SWAP = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5'}


def make_password(password):
    return ''.join(SWAP.get(a[0], a[0]) for a in password.split())
