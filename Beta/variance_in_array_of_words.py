def variance(array):
    nums = map(len, array)
    length = float(len(nums))
    average = sum(nums) / length
    return round(sum((average - a) ** 2 for a in nums) / length, 4)
