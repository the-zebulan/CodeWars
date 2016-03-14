from math import ceil


class PaginationHelper(object):
    def __init__(self, collection, items_per_page):
        self.total_items = len(collection)
        self.total_pages = int(ceil(self.total_items / float(items_per_page)))
        self.items_per_page = items_per_page  # maximum per page

    def item_count(self):
        return self.total_items

    def page_count(self):
        return self.total_pages

    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.total_items:
            return -1
        page = item_index / self.items_per_page
        return page if page < self.total_pages else -1

    def page_item_count(self, page_index):
        current = self.items_per_page * page_index
        if current >= self.total_items:
            return -1
        elif self.total_items >= current + self.items_per_page:
            return self.items_per_page
        return self.total_items - current


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
assert helper.page_count() == 2
assert helper.item_count() == 6
assert helper.page_item_count(0) == 4
assert helper.page_item_count(1) == 2
assert helper.page_item_count(2) == -1  # since the page is invalid

# page_index takes an item index and returns the page that it belongs on
assert helper.page_index(5) == 1  # (zero based index)
assert helper.page_index(2) == 0
assert helper.page_index(20) == -1
assert helper.page_index(-10) == -1  # because negative indexes are invalid

collection = range(1, 25)
helper = PaginationHelper(collection, 10)
assert helper.page_count() == 3
assert helper.page_index(23) == 2
assert helper.item_count() == 24
print helper.page_index(24)
