class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.first_name + ' ' + self.last_name

person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name())
print(person.age)
