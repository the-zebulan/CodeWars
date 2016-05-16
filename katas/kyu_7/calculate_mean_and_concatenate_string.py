def mean(arr):
    letters = []
    sum_of_digits = total_digits = 0.0
    for a in arr:
        try:
            sum_of_digits += int(a)
            total_digits += 1
        except ValueError:
            letters.append(a)
    return [sum_of_digits / total_digits, ''.join(letters)]
