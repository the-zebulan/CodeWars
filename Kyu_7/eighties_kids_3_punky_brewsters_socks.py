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
