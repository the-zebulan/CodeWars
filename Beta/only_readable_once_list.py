class SecureList(object):
    def __init__(self, lst):
        self.lst = list(lst)

    def __getitem__(self, item):
        return self.lst.pop(item)

    def __len__(self):
        return len(self.lst)

    def __repr__(self):
        tmp, self.lst = self.lst, []
        return repr(tmp)

    def __str__(self):
        tmp, self.lst = self.lst, []
        return str(tmp)


base = [1, 2, 3, 4]
a = SecureList(base)
assert a[0] == base[0]
assert a[0] == base[1]
assert len(a) == 2
print 'Current List: {!s}'.format(a)
assert len(a) == 0

a = SecureList(base)
print 'Current List: {!r}'.format(a)
assert len(a) == 0
