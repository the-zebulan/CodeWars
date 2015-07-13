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

quotes = ["WHERE IS SHE?!", "Holy haberdashery, Batman!", "Let's put a smile on that faaaceee!"]
assert BatmanQuotes.get_quote(quotes, "Rob1n") == "Robin: Holy haberdashery, Batman!"
