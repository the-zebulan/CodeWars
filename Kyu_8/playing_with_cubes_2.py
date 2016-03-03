class Cube:
    def __init__(self, side=0):
        self._side = side

    def get_side(self):
        """ Return the side of the Cube """
        return self._side

    def set_side(self, new_side):
        """ Set the value of the Cube's side. """
        self._side = abs(new_side)


c = Cube(10)
assert c.get_side() == 10
c = Cube()
assert c.get_side() == 0
