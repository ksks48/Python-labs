class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name}'s age is {self.age}")

john = Person("John", 34)
john.info()
