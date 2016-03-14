class Animal(object):  # this class is hidden in CodeWars
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Some other message?!?!'


class Cat(Animal):  # this is the solution
    def speak(self):
        return '{} meows.'.format(self.name)
