class Car:
    def __init__(self, name):
        self._speed_name_map = {
            "BMW": 250,
            "Mercedes": 350
        }
        self._max_speed = self._define_max_speed(name)

    def _define_max_speed(self, name):
        return self._speed_name_map.get(name, 0)

    def distance_on_max_speed(self, distance):
        if self._max_speed == 0:
            print(
                "Speed = 0, select valid car brand: {}".format(
                    list(self._speed_name_map.keys())
                )
            )
            return 0
        return distance / self._max_speed


car1 = Car('BMW')
car2 = Car('Mercedes')
car3 = Car('ABC')

print(car1.distance_on_max_speed(100))
print(car2.distance_on_max_speed(100))
print(car3.distance_on_max_speed(100))


class Animal:
    def __init__(self, name):
        self._name = name

    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        print("Meow")


class Dog(Animal):
    def voice(self):
        print("Bark")


animal = Animal('?')
animal.voice()

cat = Cat('Sarah')
cat.voice()
dog = Dog('Rex')
dog.voice()


class Animal2:
    def __init__(self, name):
        self._name = name

    def voice(self):
        if self._name == 'cat':
            print('Meow')
        elif self._name == "dog":
            print('Bark')
        else:
            print("...")


a1 = Animal2('cat')
a2 = Animal2('dog')
a3 = Animal2('dinosaur')
a1.voice()
a2.voice()
a3.voice()
