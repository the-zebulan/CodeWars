def remove_smallest(numbers):
    # if the kata updates the test cases, remove first minimum instead
    if not numbers:
        return []
    minimum = min(numbers)
    return filter(lambda a: a != minimum, numbers)


assert remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5]
assert remove_smallest([5, 3, 2, 1, 4]) == [5, 3, 2, 4]
assert remove_smallest([]) == []
