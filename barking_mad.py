class Dog ():
    def __init__(self, breed):
        self.breed = breed

    def bark(self):
        return 'Woof'

snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")

assert snoopy.bark() == 'Woof'
assert scoobydoo.bark() == 'Woof'
assert Dog('Schnauzer').bark() == 'Woof'
