class Sleigh:
    @staticmethod
    def authenticate(name, password):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'

sleigh = Sleigh()
assert sleigh.authenticate('Santa Claus', 'Ho Ho Ho!') is True
assert sleigh.authenticate('Santa', 'Ho Ho Ho!') is False
assert sleigh.authenticate('Santa Claus', 'Ho Ho!') is False
assert sleigh.authenticate('jhoffner', 'CodeWars') is False
