class Block:
    def __init__(self, measurements):
        self.width, self.length, self.height = measurements

    def get_height(self):
        return self.height

    def get_length(self):
        return self.length

    def get_surface_area(self):
        return 2 * (self.height * self.length +
                    self.length * self.width +
                    self.height * self.width)

    def get_volume(self):
        return self.height * self.length * self.width

    def get_width(self):
        return self.width

b = Block([2, 4, 6])
assert b.get_width() == 2
assert b.get_length() == 4
assert b.get_height() == 6
assert b.get_volume() == 48
assert b.get_surface_area() == 88

b2 = Block([2, 2, 2])
assert b2.get_width() == 2
assert b2.get_length() == 2
assert b2.get_height() == 2
assert b2.get_volume() == 8
assert b2.get_surface_area() == 24
