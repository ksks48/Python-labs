class Parser:
    def __init__(self):
        pass
    @staticmethod
    def __convert_type(value_str):
        result = 0
        if isinstance(value_str, str):
            if "." in value_str:
                result = float(value_str)
            else:
                result = int(value_str)
        return result

    def parse(self, expression):
        packed_values = tuple(expression.split(" "))
        if len(packed_values) < 3:
            print("Wrong indentation, check your expression")
            return 0, 0, "+"
        x, f, y = packed_values
        return self.__convert_type(x), self.__convert_type(y), f


class Core:
    def __init__(self):
        self._parser = Parser()
        self._function = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "/": lambda x, y: x / y,
            "*": lambda x, y: x * y,
        }

    def calculate(self, expression):
        x, y, f = self._parser.parse(expression)
        result = self._function.get(f)(x, y)
        return result


class Interface:
    def __init__(self):
        self._core = Core()

    def run_calculate(self):
        print("Print your expression")
        expression = input()
        result = self._core.calculate(expression)
        print("Result: ", result)


calc = Interface()
calc.run_calculate()
