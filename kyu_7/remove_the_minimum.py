def remove_smallest(numbers):
    if not numbers:
        return []
    numbers.remove(min(numbers))
    return numbers
