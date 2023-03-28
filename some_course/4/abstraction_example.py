class Core:
    def __init__(self):
        self._types = {
            "A": 100,
            "B": 300
        }

    def get_salary(self, class_name):
        return self._types.get(class_name, 0)


class AccountingInterface:
    def __init__(self, data):
        self._core = Core()
        self._database = data

    def get_salary(self, name):
        class_of_employee = self._database.get(name)
        salary = self._core.get_salary(class_of_employee)
        return salary


db = {"John": "A", "Mike": "B"}
interface = AccountingInterface(data=db)
print("John's salary is: {}".format(interface.get_salary(name="John")))
