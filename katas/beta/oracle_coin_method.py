ORDER = ('six', 'five', 'four', 'three', 'two', 'one')
YIN_YANG = {'hhh': '----o----', 'hht': '---- ----',
            'htt': '---------', 'ttt': '----x----'}


def oracle(arr):
    return '\n'.join(YIN_YANG[''.join(sorted(a[1:]))] for a in
                     sorted(arr, key=lambda b: ORDER.index(b[0])))
