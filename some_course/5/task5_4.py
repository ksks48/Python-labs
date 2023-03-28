"""2. Напишіть функцію, яка рекурсивно шукає у складному об'єкті значення. Складний об'єкт 
– це буде список списків списків і т.д. Наприклад, [1, 2, [3, 4, [5, [6, []]]]]]. Функція має 
рекурсивно заходити всередину вкладених масивів, і якщо це інший тип даних 
ігнорувати його"""

def rec(some_list, n):
    """checking"""
    for item in some_list:
        if type(item) == list:
            result = rec(item, n)
            if result is not None:
                print(result,"in list")
        elif item == n:
            return item
    return None


n = 9
some_list = [1, 2, [3, 4, [5, [6, []]]]]
rec(some_list, n)
if rec(some_list, n) == None:
    print(n, "not in list")