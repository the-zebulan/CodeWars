from re import findall


def sum_from_string(string):
    return sum(int(a) for a in findall(r'\d+', string))


assert sum_from_string(
    'In 2015, I want to know how much does iPhone 6+ cost?') == 2021
assert sum_from_string('1+1=2') == 4
assert sum_from_string('e=mc^2') == 2
