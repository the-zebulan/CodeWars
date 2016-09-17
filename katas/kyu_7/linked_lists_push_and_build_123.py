class Node(object):
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


def push(head, data):
    return Node(data, head)


def build_one_two_three():
    return Node(1, Node(2, Node(3)))
