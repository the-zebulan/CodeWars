def remove_smallest(numbers):
    if not numbers:
        return []
    numbers.remove(min(numbers))
    return numbers


assert remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5]
assert remove_smallest([5, 3, 2, 1, 4]) == [5, 3, 2, 4]
assert remove_smallest([1, 2, 3, 1, 1]) == [2, 3, 1, 1]
assert remove_smallest([]) == []
