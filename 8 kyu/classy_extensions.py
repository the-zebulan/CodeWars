class Animal(object):  # this class is hidden in CodeWars
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Some other message?!?!'


class Cat(Animal):  # this is the solution
    def speak(self):
        return '{} meows.'.format(self.name)


cat = Cat('Mr Whiskers')
assert cat.speak() == 'Mr Whiskers meows.'
cat = Cat('Lamp')
assert cat.speak() == 'Lamp meows.'
cat = Cat('$$Money Bags$$')
assert cat.speak() == '$$Money Bags$$ meows.'
