HERO = {'B': 'Batman', 'J': 'Joker', 'R': 'Robin'}
OUTPUT = '{}: {}'.format


class BatmanQuotes(object):
    @staticmethod
    def get_quote(quotes, hero):
        for i, a in enumerate(hero):
            if i == 0:
                hero = HERO[a]
            elif a.isdigit():
                quotes = quotes[int(a)]
                break
        return OUTPUT(hero, quotes)
