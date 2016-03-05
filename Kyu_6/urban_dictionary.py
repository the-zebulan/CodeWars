from re import compile, search


class WordDictionary:
    def __init__(self):
        self.words = set()

    def add_word(self, word):
        self.words.add(word)

    def search(self, search_term):
        regex = compile(r'^{}$'.format(search_term))
        return any(search(regex, word) for word in self.words)
