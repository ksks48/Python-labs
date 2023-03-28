class Multiplier:
    def __init__(self, a):
        self._a = a

    def print_a(self, x):
        print(self._a * x)


m = Multiplier(5)
m.print_a(2)


class Exponent(Multiplier):
    def print_a(self, x):
        print(self._a ** x)


e = Exponent(4)
e.print_a(2)
