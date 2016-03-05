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
