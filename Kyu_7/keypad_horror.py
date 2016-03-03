from string import maketrans

PHONE = maketrans('123789', '789123')


def computer_to_phone(nums):
    return nums.translate(PHONE)

assert computer_to_phone('94561') == '34567'
assert computer_to_phone('000') == '000'
assert computer_to_phone('0789456123') == '0123456789'
