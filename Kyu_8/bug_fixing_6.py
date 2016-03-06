def eval_object(v):
    return {'+': v['a'] + v['b'], '-': v['a'] - v['b'],
            '/': v['a'] / v['b'], '*': v['a'] * v['b'],
            '%': v['a'] % v['b'], '**': v['a'] ** v['b']}.\
        get(v['operation'], 1)
