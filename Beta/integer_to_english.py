WORDS = ((10 ** 24, 'septillion'), (10 ** 21, 'sextillion'),
         (10 ** 18, 'quintillion'), (10 ** 15, 'quadrillion'),
         (10 ** 12, 'trillion'), (10 ** 9, 'billion'), (10 ** 6, 'million'),
         (10 ** 3, 'thousand'), (10 ** 2, 'hundred'), (90, 'ninety'),
         (80, 'eighty'), (70, 'seventy'), (60, 'sixty'), (50, 'fifty'),
         (40, 'forty'), (30, 'thirty'), (20, 'twenty'), (19, 'nineteen'),
         (18, 'eighteen'), (17, 'seventeen'), (16, 'sixteen'), (15, 'fifteen'),
         (14, 'fourteen'), (13, 'thirteen'), (12, 'twelve'), (11, 'eleven'),
         (10, 'ten'), (9, 'nine'), (8, 'eight'), (7, 'seven'), (6, 'six'),
         (5, 'five'), (4, 'four'), (3, 'three'), (2, 'two'), (1, 'one'))


def int_to_english(num):
    result = []
    for word_value, word_name in WORDS:
        q, num = divmod(num, word_value)
        if q:
            if word_value >= 100:
                result.append(int_to_english(q))
            result.append(word_name)
        if not num:
            return ' '.join(result)
