def small_enough(array, limit):
    return all(a <= limit for a in array)
