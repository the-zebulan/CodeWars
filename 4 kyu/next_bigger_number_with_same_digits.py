def next_bigger(n):
    nums = list(str(n))
    length = len(nums) - 1
    suffix = length
    while nums[suffix - 1] >= nums[suffix] and suffix > 0:
        suffix -= 1
    if suffix <= 0:
        return -1

    rightmost = length
    while nums[rightmost] <= nums[suffix - 1]:
        rightmost -= 1
    nums[suffix - 1], nums[rightmost] = nums[rightmost], nums[suffix - 1]

    nums[suffix:] = nums[length:suffix - 1:-1]
    return int(''.join(nums))


assert next_bigger(12) == 21
assert next_bigger(513) == 531
assert next_bigger(2017) == 2071

assert next_bigger(9) == -1
assert next_bigger(111) == -1
assert next_bigger(531) == -1
