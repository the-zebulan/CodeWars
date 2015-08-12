from math import pi


class Sphere:
    def __init__(self, radius, mass):
        self.mass = mass
        self.radius = radius

    def get_density(self):
        return round((self.mass * 1.0) / self.get_volume(), 5)

    def get_mass(self):
        return self.mass

    def get_radius(self):
        return self.radius

    def get_surface_area(self):
        return round(4 * pi * self.radius ** 2, 5)

    def get_volume(self):
        return round(4 / 3.0 * pi * self.radius ** 3, 5)

ball = Sphere(2, 50)
assert ball.get_radius() == 2
assert ball.get_mass() == 50
assert ball.get_volume() == 33.51032
assert ball.get_surface_area() == 50.26548
assert ball.get_density() == 1.49208
