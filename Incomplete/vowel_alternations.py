from collections import defaultdict
VOWELS = 'aeiou'


def find_solutions(words):
    if not words:
        return 0

    d = {k: lambda: defaultdict(list) for k in VOWELS}
    print d


    # # word_cnt = 0
    # # my_dict = defaultdict(set)
    # d = defaultdict(int)
    # d_dex = defaultdict(list)
    # for word in words:  # .lower()
    #     for ii, letter in enumerate(word):
    #         if letter in VOWELS:
    #             d[ii] += 1
    #             d_dex[ii].append(word)
    #     # word_cnt += 1
    # print d
    # print d_dex
    # for k, v in d.iteritems():
    #     if v >= 5:  #word_cnt:
    #         return sorted(d_dex[k], key=lambda a: a[k])


tests = [
    ['last', 'lest', 'list', 'lost', 'lust'],
    ['beryl', 'jigsawed', 'oospheres', 'troweller', 'volcanizes'],
    ['blackcaps', 'blackguard', 'blacks', 'blague', 'blancmange',
     'blander', 'blastular', 'blawort', 'blender', 'blimbing',
     'blinder', 'blistered', 'blocks', 'blonde', 'blonder',
     'blotchier', 'blowlamp', 'blue', 'bluejays', 'blunder'],
]

solutions = [
    [['last', 'lest', 'list', 'lost', 'lust']],
    [],
    [['blander', 'blender', 'blinder', 'blonder', 'blunder']]
]

for test, solution in zip(tests, solutions):
    print find_solutions(test) == solution
    # , \
    # 'There is/are {} solution(s) in this list of words:\n{}'\
    # .format(len(solution), repr(test))
