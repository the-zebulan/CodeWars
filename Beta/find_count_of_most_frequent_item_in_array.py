from collections import Counter


def most_frequent_item_count(collection):
    return Counter(collection).most_common(1)[0][1] if collection else 0


assert most_frequent_item_count([3, -1, -1]) == 2
assert most_frequent_item_count(
    [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]) == 5
assert most_frequent_item_count([]) == 0
assert most_frequent_item_count([9]) == 1
