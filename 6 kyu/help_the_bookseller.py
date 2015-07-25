from collections import defaultdict

OUTPUT = '({} : {})'.format


def stock_list(books, categories):
    if not books or not categories:
        return ''
    book_quantity = defaultdict(int)
    for book in books:
        code, num = book.split()
        book_quantity[code[0]] += int(num)
    return ' - '.join(OUTPUT(a, book_quantity.get(a, 0)) for a in categories)

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
res = "(A : 200) - (B : 1140)"
assert stock_list(b, c) == res
assert stock_list(b, []) == ''
assert stock_list([], c) == ''
