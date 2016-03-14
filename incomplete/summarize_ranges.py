def output(lst):
    start = lst[0]
    end = lst[-1]
    return '{}->{}'.format(start, end) if start != end else str(start)


def summary_ranges(nums):
    result = []
    group = []
    last = nums[0]
    for num in nums:
        if num - last > 1:
            result.append(output(group))
            group = []
        group.append(num)
        last = num
    result.append(output(group))
    return result


print summary_ranges([1, 1, 1, 1])  # == ['1']
print summary_ranges([1, 2, 3, 4])  # == ['1->4']
print summary_ranges([0, 1, 2, 5, 6, 9])  # == ["0->2", "5->6", "9"]
print summary_ranges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7])  # == ["0->7"]
print summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7])  # == ["0->7"]
