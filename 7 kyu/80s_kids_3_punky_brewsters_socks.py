from collections import Counter


def get_socks(name, socks):
    cnt = Counter(socks)
    colors = cnt.keys()
    total_colors = len(colors)
    if not socks or total_colors < 2:
        return []
    color, total = cnt.most_common(1)[0]
    if name == 'Henry':
        return [color, color] if total >= 2 else []
    elif name == 'Punky':
        return colors[:2]


assert get_socks('Punky', ['pink', 'argyle', 'argyle']) == ['pink', 'argyle']
assert get_socks('Henry', ['red', 'blue', 'blue', 'green']) == ['blue', 'blue']
assert get_socks('Punky', ['pink', 'pink', 'pink', 'pink']) == []
assert get_socks('Punky', ['blue', 'blue', 'blue', 'green', 'green']) == ['blue', 'green']
assert get_socks('Henry', ['green', 'blue', 'pink', 'argyle']) == []
assert get_socks('Henry', ['argyle', 'green', 'dirty sock', 'argyle']) == ['argyle', 'argyle']
assert get_socks('Henry', ['green']) == []
assert get_socks('Punky', ['green']) == []
assert get_socks('Henry', []) == []
assert get_socks('Punky', []) == []
