def password(pw):
    dig = length = low = up = 0
    for a in pw:
        if a.isdigit():
            dig += 1
        elif a.isupper():
            up += 1
        elif a.islower():
            low += 1
        length += 1
    return dig >= 1 and length >= 8 and low >= 1 and up >= 1


assert password("Abcd1234") is True
assert password("Abcd123") is False
assert password("abcd1234") is False
assert password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890") is True
assert password("ABCD1234") is False
assert password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,") is True
assert password("!@#$%^&*()-_+={}[]|\:;?/>.<,") is False
