import re
from unicodedata import normalize


def words(s):
    uni_s = normalize('NFKD', unicode(s)).encode('ascii', 'ignore').lower()
    return re.sub(r'[?!.,;:]', ' ', uni_s).split()


def could_be(original, another):
    if not original.strip() or not another.strip():
        return False
    return set(words(another)).issubset(words(original))
