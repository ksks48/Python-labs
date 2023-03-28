class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


user = User(name='Alex')
user.name = 'Bob'
print(user.name)

class User2:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("Property was called")
        return self.__name


u2 = User2(name='Mike')
print(u2.name)


class Worker:
    RIGHTS = "Equal"
    SALARY_MAP = {
        "A": 100,
        "B": 200,
        "C": 500
    }

    def __init__(self, working_class):
        self.__salary = self.__get_salary(working_class)

    @staticmethod
    def __get_salary(working_class):
        return Worker.SALARY_MAP.get(working_class, 0)

    @property
    def salary(self):
        return self.__salary


w1 = Worker('A')
print(w1.salary)

w2 = Worker('D')
print(w2.salary)
