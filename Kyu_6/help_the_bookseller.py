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
