from string import maketrans

PHONE = maketrans('123789', '789123')


def computer_to_phone(nums):
    return nums.translate(PHONE)
