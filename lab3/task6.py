class Quark:
    def __init__(self, color, flavor):
        valid_colors = ["red", "blue", "green"]
        valid_flavors = ['up', 'down', 'strange', 'charm', 'top', 'bottom']
        if color not in valid_colors:
            print("ValueError('Invalid color')")
            pass
        if flavor not in valid_flavors:
            print("ValueError('Invalid flavor')")
            pass
        self.color = color
        self.flavor = flavor
        self.baryon_number = 1/3

    def interact(self, other):
        if not isinstance(other, Quark):
            print("ValueError('Can only interact with another quark')")
            pass
        self.color, other.color = other.color, self.color

    def __str__(self):
        return f"Class name is: {self.__class__.__name__}, color: {self.color}, flavor: {self.flavor}, baryon_number: {self.baryon_number}"

q1 = Quark("red", "up")
print(q1.color)
print(q1.flavor)
q2 = Quark("blue", "strange")
print(q2.color)
print(q2.baryon_number)
q1.interact(q2)
print(q1.color)
print(q2.color)
print(q1)