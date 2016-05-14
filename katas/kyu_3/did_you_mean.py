class Dictionary:
    def __init__(self, words):
        self.words = words

    def find_most_similar(self, term):
        return min(self.words, key=lambda a: self.levenshtein(term, a))

    @staticmethod
    def levenshtein(s1, s2):
        """ https://en.wikipedia.org/wiki/Levenshtein_distance """
        s1, s2 = sorted((s1, s2), key=len)
        distances = range(len(s1) + 1)
        for i, b in enumerate(s2):
            new_distances = [i + 1]
            for ii, c in enumerate(s1):
                if b == c:
                    new_distances.append(distances[ii])
                    continue
                new_distances.append(1 + min(distances[ii],
                                             distances[ii + 1],
                                             new_distances[-1]))
            distances = new_distances
        return distances[-1]
