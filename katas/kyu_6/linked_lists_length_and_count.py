class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    current = node
    result = 0
    while current is not None:
        current = current.next
        result += 1
    return result


def count(node, data):
    current = node
    result = 0
    while current is not None:
        if current.data == data:
            result += 1
        current = current.next
    return result
