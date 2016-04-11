class AddOne(object):
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n + 1


def AddExtra(listOfNumbers):
    return AddOne(len(listOfNumbers))
