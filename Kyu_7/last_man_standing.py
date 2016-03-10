def last_man_standing(n):
    numbers = range(1, n + 1)
    go_right = True
    while len(numbers) > 1:
        numbers = numbers[1::2] if go_right else numbers[-2::-2][::-1]
        go_right = not go_right
    return numbers[0]
