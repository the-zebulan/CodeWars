from collections import Counter


def most_frequent_item_count(collection):
    return Counter(collection).most_common(1)[0][1] if collection else 0
