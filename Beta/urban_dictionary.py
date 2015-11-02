from re import compile, search


class WordDictionary:
    def __init__(self):
        self.words = set()

    def add_word(self, word):
        self.words.add(word)

    def search(self, search_term):
        regex = compile(r'^{}$'.format(search_term))
        return any(search(regex, word) for word in self.words)


wd = WordDictionary()
wd.add_word('a')
wd.add_word('at')
wd.add_word('ate')
wd.add_word('ear')
assert wd.search('a') is True
assert wd.search('a.') is True
assert wd.search('a.e') is True
assert wd.search('b') is False
assert wd.search('e.') is False
assert wd.search('ea.') is True
assert wd.search('ea..') is False

wd.add_word('co')
wd.add_word('cod')
wd.add_word('code')
wd.add_word('codewars')
assert wd.search('........') is True
assert wd.search('c.o') is False
assert wd.search('cod.') is True
assert wd.search('c.o') is False
assert wd.search('co..w..s') is True
assert wd.search('co..w..') is False
