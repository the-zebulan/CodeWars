class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, other_name):
        return "Hi {}, my name is {}".format(other_name, self.name)
