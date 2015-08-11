def sort_array(value):
    return ''.join(sorted(value, key=lambda a: int(a)))

assert sort_array('12345') == '12345'
assert sort_array('54321') == '12345'
assert sort_array('34251') == '12345'
