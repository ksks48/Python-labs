class Car:
    def __init__(self, brand, color, vol):
        self.brand = brand
        self.color = color
        self.vol = vol

    def driving_forward(self):
        print("Drive forward!")

    def driving_back(self):
        print("Drive backward!")

class New_car(Car):
    def __init__(self, brand, color, vol):
        super().__init__(brand, color, vol)

    def driving_right(self):
        print("I'm driving right!")

    def driving_left(self):
        print("I'm driving left!")

class Flight:
    def __init__(self, model):
        self.model = model

    def fly(self):
        print("I'm start flying!")

class Some_new_class(New_car,Flight):
    def __init__(self, brand, color, vol, model):
        Car.__init__(self, brand, color, vol)
        Flight.__init__(self, model)


bmw = New_car("lol1", "red", 1.2)
bmw.driving_right()
bmw.driving_forward()
smth = Some_new_class("I", "gray", 5, "1.2.1s")
smth.fly()
smth.driving_forward()