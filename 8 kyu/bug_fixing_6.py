def eval_object(v):
    return {'+': v['a'] + v['b'], '-': v['a'] - v['b'],
            '/': v['a'] / v['b'], '*': v['a'] * v['b'],
            '%': v['a'] % v['b'], '**': v['a'] ** v['b']}.get(v['operation'], 1)

assert eval_object({'a': 1, 'b': 1, 'operation': '+'}) == 2
assert eval_object({'a': 1, 'b': 1, 'operation': '-'}) == 0
assert eval_object({'a': 1, 'b': 1, 'operation': '/'}) == 1
assert eval_object({'a': 1, 'b': 1, 'operation': '*'}) == 1
assert eval_object({'a': 1, 'b': 1, 'operation': '%'}) == 0
assert eval_object({'a': 1, 'b': 1, 'operation': '**'}) == 1
