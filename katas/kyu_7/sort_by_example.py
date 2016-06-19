def example_sort(arr, example_arr):
    keys = {k: i for i, k in enumerate(example_arr)}
    return sorted(arr, key=lambda a: keys[a])
