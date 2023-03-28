"""
program for database example
"""
class Data:
    """
    class for data
    """
    def __init__(self, country, name, age, gender, height, weight):
        """
        constructor
        """
        self._country = country
        self._name = name
        self._age = age
        self._gender = gender
        self._height = height
        self._weight = weight

    def to_dict(self):
        """
        return all data to the dict
        """
        return {
            "country": self._country,
            "name": self._name,
            "age": self._age,
            "gender": self._gender,
            "height": self._height,
            "weight": self._weight,
        }


class Database:
    """
    class for interface of database
    """
    def __init__(self):
        self._elements = []

    def write_data(self, element):
        """
        method to write data
        """
        if isinstance(element, Data):
            self._elements.append(element)
        else:
            raise ValueError("Element must be an instance of Data class")

    def read_data(self, criteria):
        """
        method to read data
        """
        results = []
        for element in self._elements:
            match = True
            for key, value in criteria.items():
                if element.to_dict().get(key) != value:
                    match = False
                    break
            if match:
                results.append(element)
        return results


db = Database()

data1 = Data("USA", "John", 30, "Male", 180, 75)
db.write_data(data1)

data2 = Data("Canada", "Jane", 25, "Female", 165, 55)
db.write_data(data2)

data3 = Data("USA", "Bob", 40, "Male", 175, 80)
db.write_data(data3)

result = db.read_data({"age": 30, "gender": "Male"})
for data in result:
    print(data.to_dict())

result = db.read_data({"country": "USA"})
for data in result:
    print(data.to_dict())
