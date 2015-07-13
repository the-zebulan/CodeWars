OUTPUT = 'Showing {} to {} of {} Products.'.format


def pagination_text(page_num, page_size, total):
    to_y = page_num * page_size
    return OUTPUT(to_y - page_size + 1, to_y if to_y < total else total, total)

assert pagination_text(1, 10, 30) == 'Showing 1 to 10 of 30 Products.'
assert pagination_text(3, 10, 26) == 'Showing 21 to 26 of 26 Products.'
assert pagination_text(1,10,8) == "Showing 1 to 8 of 8 Products."
assert pagination_text(2,30,350) == "Showing 31 to 60 of 350 Products."
assert pagination_text(1,23,30) == "Showing 1 to 23 of 30 Products."
assert pagination_text(2,23,30) == "Showing 24 to 30 of 30 Products."
assert pagination_text(43,15,3456) == "Showing 631 to 645 of 3456 Products."
