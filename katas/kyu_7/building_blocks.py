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
