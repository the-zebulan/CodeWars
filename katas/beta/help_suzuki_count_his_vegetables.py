from collections import Counter

VEGETABLES = {'cabbage', 'carrots', 'celery', 'cucumber', 'mushrooms',
              'onions', 'pepper', 'potato', 'tofu', 'turnip'}


def count_vegetables(vegetables):
    return sorted(((v, k) for k, v in Counter(vegetables.split()).iteritems()
                   if k in VEGETABLES), reverse=True)
