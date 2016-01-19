def show_me(instname):
    attrs = sorted(instname.__dict__.iterkeys())
    if len(attrs) == 1:
        attrs = attrs[0]
    else:
        attrs = '{} and {}'.format(', '.join(attrs[:-1]), attrs[-1])
    return 'Hi, I\'m one of those {}s! Have a look at my {}.'\
        .format(instname.__class__.__name__, attrs)


# Kata solution is the function above
# Below this line is just for testing
class Vehicle:
    def __init__(self, seats, wheels, engine):
        self.seats = seats
        self.wheels = wheels
        self.engine = engine


class Planet:
    def __init__(self, moon):
        self.moon = moon


porsche = Vehicle(2, 4, 'Gas')
assert show_me(porsche) == "Hi, I'm one of those Vehicles! Have a look " \
                          "at my engine, seats and wheels."

earth = Planet('moon')
assert show_me(earth) == "Hi, I'm one of those Planets! Have a look at my moon."
