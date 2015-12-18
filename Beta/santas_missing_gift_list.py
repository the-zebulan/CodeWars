SANTA = ((512, "Rubik's Cube"), (256, 'Doll'), (128, 'Football'),
         (64, 'Lego'), (32, 'Teddy'), (16, 'Horse'), (8, 'Chess Board'),
         (4, 'Hoop'), (2, 'Wooden Train'), (1, 'Toy Soldier'))


def gifts(number):
    result = []
    for k, v in SANTA:
        q, number = divmod(number, k)
        if q:
            result.append(v)
    result.sort()
    return result


assert gifts(1) == ['Toy Soldier']
assert gifts(2) == ['Wooden Train']
assert gifts(3) == ['Toy Soldier', 'Wooden Train']
assert gifts(22) == ['Hoop', 'Horse', 'Wooden Train']
assert gifts(160) == ['Football', 'Teddy']
