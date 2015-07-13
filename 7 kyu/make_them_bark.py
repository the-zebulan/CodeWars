class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.age = age
        self.breed = breed
        self.name = name
        self.sex = sex

setattr(Dog, 'bark', lambda a: 'Woof!')  # class is pre-loaded in kata

assert Dog('Apollo', 'Dobermann', 'male', '4').bark() == 'Woof!'
assert Dog('Zeus', 'Dobermann', 'male', '4').bark() == 'Woof!'
