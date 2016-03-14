def linked_sort(a_to_sort, a_linked, key=None):
    merge = zip(a_to_sort, a_linked)
    print merge
    print sorted(merge, key=key)



a_to_sort = [1, 6, 5, 0]
a_linked = ['house', 'car', 'pen', 'jeans']
res = linked_sort(a_to_sort, a_linked)

print a_to_sort == [0, 1, 5, 6]
print a_linked == ['jeans', 'house', 'pen', 'car']
print res == [0, 1, 5, 6]

a_to_sort = [-71, -6, 35, 0]
a_linked = [0, "Hello", 32, True]
res = linked_sort(a_to_sort, a_linked)

print a_to_sort == [-6, -71, 0, 35]
print a_linked == ["Hello", 0, True, 32]
print res == [-6, -71, 0, 35]
