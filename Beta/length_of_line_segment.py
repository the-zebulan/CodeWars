def length_of_line(array):
    (x, y), (x2, y2) = array
    return '{:.2f}'.format(((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5)

assert length_of_line([[0, 0], [1, 1]]) == '1.41'
assert length_of_line([[0, 0], [-5, -6]]) == '7.81'
assert length_of_line([[0, 0], [10, 15]]) == '18.03'
assert length_of_line([[0, 0], [5, 1]]) == '5.10'
assert length_of_line([[0, 0], [5, 4]]) == '6.40'
assert length_of_line([[0, 0], [-7, 4]]) == '8.06'
assert length_of_line([[0, 0], [0, 0]]) == '0.00'
assert length_of_line([[-3, 4], [10, 5]]) == '13.04'
