def who_took_the_car_key(message):
    return ''.join(chr(int(a, 2)) for a in message)
