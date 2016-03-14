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
