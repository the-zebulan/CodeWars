def linked_sort(a_to_sort, a_linked, key=None):
    d = dict(zip(a_linked, a_to_sort))
    a_to_sort.sort(key=key or str)
    a_linked.sort(key=lambda a: a_to_sort.index(d[a]))
    return a_to_sort


a_to_sort = [1, 6, 5, 0]
a_link = ['house', 'car', 'pen', 'jeans']
res = linked_sort(a_to_sort, a_link)
print a_to_sort == [0, 1, 5, 6]
print a_link == ['jeans', 'house', 'pen', 'car']
print res == [0, 1, 5, 6]

a_to_sort = [-71, -6, 35, 0]
a_link = [0, "Hello", 32, True]
res = linked_sort(a_to_sort, a_link)
print a_to_sort == [-6, -71, 0, 35]
print a_link == ["Hello", 0, True, 32]
print res == [-6, -71, 0, 35]
