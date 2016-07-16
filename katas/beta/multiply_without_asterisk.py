class MyNumber(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return MyNumber(self.num + other)

    def __radd__(self, other):
        return MyNumber(other + self.num)

    def __call__(self, other):
        return MyNumber(self.num * other)

    def __div__(self, other):
        return MyNumber(self.num / other)

    def __rdiv__(self, other):
        return MyNumber(other / self.num)

    def __eq__(self, other):
        return self.num == other

    def __int__(self):
        return int(self.num)

    def __mod__(self, other):
        return MyNumber(self.num % other)

    def __rmod__(self, other):
        return MyNumber(other % self.num)

    def __mul__(self, other):
        return MyNumber(self.num * other)

    def __rmul__(self, other):
        return MyNumber(other * self.num)

    def __pow__(self, other):
        return MyNumber(self.num ** other)

    def __rpow__(self, other):
        return MyNumber(other ** self.num)

    def __str__(self):
        return str(self.num)

    def __sub__(self, other):
        return MyNumber(self.num - other)

    def __rsub__(self, other):
        return MyNumber(other - self.num)

    def __xor__(self, other):
        return MyNumber(self.num ** other)

    def __rxor__(self, other):
        return MyNumber(other ** self.num)


a = MyNumber(7)
b = MyNumber(8)

print a ^ b


# print (a - 1)
# print type(a - 1)
# print a + 1
# print a % 2
# print a / 2
# print a * 2

print (a - 1)(b - 1), 42
print (a)(b), 56
print (1 - a) ^ 2, 36
print (a - 1)(a)(a + 1), 336
