from collections import Counter
from string import ascii_lowercase


def decrypt(test_key):
    cnt = Counter(test_key.lower())
    return ''.join(str(cnt[a]) for a in ascii_lowercase)
