class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    current = node
    dex = -1
    while current is not None:
        dex += 1
        if dex == index:
            return current
        current = current.next
    raise Exception
