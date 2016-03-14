OUTPUT = 'Showing {} to {} of {} Products.'.format


def pagination_text(page_num, page_size, total):
    to_y = page_num * page_size
    return OUTPUT(to_y - page_size + 1, to_y if to_y < total else total, total)
