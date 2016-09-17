class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    if node is None or index < 0:
        raise Exception
    current = node
    dex = 0
    while True:
        if dex == index:
            return current
        current = current.next
        if current is None:
            break
        dex += 1
    if dex != index:
        raise Exception
    return current
