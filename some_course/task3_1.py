class Parallelogram:
    def __init__(self, width = None, length = None):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length
    
class Square(Parallelogram):
    def get_area(self):
        return self.width ** 2


p1 = Parallelogram(width = 2, length = 4)
print(p1.get_area())
p2 = Square(3)
print(p2.get_area())


def function(data, new_value):
    if data == list(data):
        data.append(new_value)
    elif data == set(data):
        data.add(new_value)
    elif data == str(data) and new_value == str(new_value):
        data += new_value
    else:
        pass
    return data

print(function({1, 5, 3}, '4'))
print(function({1, 5, 3}, 4))
print(function('{1, 5, 3}', '4'))
print(function('{1, 5, 3}', 4))
print(function('{1, 5, 3}', [4, 3]))
