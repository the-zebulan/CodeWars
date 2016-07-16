def valid_card(card_number):
    total = 0
    for i, a in enumerate(reversed(card_number.replace(' ', ''))):
        if i % 2:
            current = int(a) * 2
            total += current - 9 if current > 8 else current
        else:
            total += int(a)
    return total % 10 == 0
