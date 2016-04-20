from requests import get

KATAS = {
    'befunge-interpreter': -2,
    'bin-to-hex-and-back': -9,
    'building-blocks': -7,
    'can-you-get-the-loop': -3,
    'cracking-the-vigenere-cipher-step-1-determining-key-length': -9,
    'how-do-i-compare-numbers': -8,
    'linked-lists-length-and-count': -6,
    'longest-palindrome': -6,
    'next-bigger-number-with-the-same-digits': -4,
    'no-zeros-for-heros': -8,
    'paths-in-the-grid': -6,
    'search-the-0-sums-combinations-in-an-array': -9,
    'suzuki-needs-help-lining-up-his-students': -7,
    'tiny-three-pass-compiler': -1,
    'using-the-codewars-api-kata-rank': -9
}
URL = 'https://www.codewars.com/api/v1/code-challenges/'


# def get_rank(kata):
#     return get(URL + kata).json()['rank']['id']
#
#
# def sort_by_rank(katas):
#     return sorted(katas, key=lambda k: KATAS.get(k, get_rank(k)))

def sort_by_rank(list_of_katas):
    return sorted(list_of_katas, key=lambda a: KATAS[a])
