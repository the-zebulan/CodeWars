from collections import Counter
from operator import le, lt, ge, gt, eq, ne


def string_evaluation(s, conditions):
    cnt = Counter(s)
    ops = {'<=': le, '<': lt, '>=': ge, '>': gt, '==': eq, '!=': ne}
    result = []
    for condition in conditions:
        left = condition[0]
        right = condition[-1]
        result.append(ops[condition[1:-1]](
            cnt[left] if not left.isdigit() else int(left),
            cnt[right] if not right.isdigit() else int(right)
        ))
    return result
