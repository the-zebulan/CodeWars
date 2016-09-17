class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    if head is None:
        return Node(data)
    else:
        n = Node(data)
        n.next = head
        return n


def build_one_two_three(n=3):
    node = None
    for data in xrange(n, 0, -1):
        if node is None:
            node = Node(data)
        else:
            new = Node(data)
            new.next = node
            node = new
    return node
