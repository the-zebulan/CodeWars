# from re import escape, findall, split
#
#
# def find(needle, haystack):
#     if '_' not in needle:
#         return haystack.find(needle)
#     reg = [escape(a) if '_' not in a else '.{{{}}}'.format(len(a))
#            for a in split('(_+)', needle)]
#     matches = findall('({})'.format(''.join(reg)), haystack)
#     return haystack.find(matches[0]) if matches else -1

import re


def find(needle, haystack):
    """ Solution from 'knight07' on CodeWars """
    compiled = re.compile(re.escape(needle).replace("\\_", "\S"))
    searched = re.search(compiled, haystack)
    return searched.start() if searched else -1

test = "Once upon a midnight dreary, while I pondered, weak and weary"
assert find("Once", test) == 0
assert find("midnight", test) == 12
assert find("codewars", test) == -1
assert find("_po_", test) == 5
assert find("___night", test) == 12
assert find('_lexe', 'googgoogleggggoooglxeplexhexflexmexkex') == -1
assert find('--_.,', '-..,.44$&%$--,.,') == 11
assert find('-..,.44$&%$--,.,', '-..,.44$&%$--,.,') == 0
assert find('___4$&%$--___', '-..,.44$&%$--,.,') == 3
