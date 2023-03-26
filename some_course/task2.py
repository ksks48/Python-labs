class User:
    def __init__(self, age, name):
        self.__age = age
        self.name = name

    @property
    def get_age(self):
        return self.__age
    
    @get_age.setter
    def set_age(self, value):
        if value > 0 and value == int(value):
            self.__age = value
        else:
            print("Your age is incorrect!")

u1 = User(age = 19, name = "ksks")
print(u1.get_age)
u1.set_age = 1.5
print(u1.get_age)