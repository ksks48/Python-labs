class Base:
    def __init__(self, a):
        self.__a = a

    def print_a(self, square=False, multiplier=None):
        if square and not multiplier:
            print(self.__a ** 2)
        elif not square and multiplier:
            print(self.__a * multiplier)
        elif square and multiplier:
            print((self.__a ** 2) * multiplier)
        else:
            print(self.__a)


base = Base(4)
base.print_a()
