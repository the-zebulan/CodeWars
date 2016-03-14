def check_valid_tr_number(number):
    number = str(number)
    if len(number) != 11 or not number.isdigit() or number[0] == '0':
        return False
    return str(sum(map(int, number)[:-1]))[-1] == number[-1]


# def check_valid_tr_number(number):
#     string = str(number)
#     if string[0] == '0' or isinstance(number, str) or not len(string) == 11:
#         return False
#     odd = 0
#     even = 0
#     tenth = 0
#     eleventh = 0
#     first_ten = 0
#     for i, a in enumerate(string):
#         current = int(a)
#         if i < 9:
#             first_ten += current
#             if i % 2 == 0:
#                 even += current
#             else:
#                 odd += current
#         elif i == 9:
#             tenth = current
#             first_ten += current
#         else:
#             eleventh = current
#     return tenth == ((even * 7) - odd) % 10 and first_ten % 10 == eleventh
