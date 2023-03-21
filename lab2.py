N = ord("K") % 3 + 1
print("Номер варіанта", N)

print("")

#лаба 2(варіант 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)


class Line:
    def __init__(self, k, b):
        self.k = k
        self.b = b
        
    def __str__(self):
        return "y = {} * x + {}".format(self.k, self.b)
    
    def intersection(self, other):
        if self.b == other.b:
            print("прямі збігаються")
            return None
        elif self.k == other.k:
            print("лінії паралельні")
            return None
        else:
            x = (other.b - self.b) / (self.k - other.k)
            y = self.k * x + self.b
            return Point(x, y)
        

print("Code snippet 1:")
a = Point(2,3)
print(a.x, a.y)
print(a)

print("")

print("Code snippet 2:")
line1 = Line(3,3)
line2 = Line(2,5)
print(line1)
print(line2)

print("")

print("Code snippet 3:")
line1 = Line(3,3)
line2 = Line(2,5)
print(line1.intersection(line2))

print("")

print("Code snippet 4:")
line1 = Line(2,3)
line2 = Line(2,5)
print(line1.intersection(line2))
print(line1)
print(line2)