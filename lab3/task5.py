import re

class ReNameAbleClass:
    @classmethod
    def change_class_name(cls, new_name):
        if (not new_name.isalnum() or not new_name[0].isupper()) and not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
            print("ValueError('Invalid class name')")
        else:
            cls.__name__ = new_name

    def __str__(self):
        return f"Class name is: {self.__class__.__name__}"
    
class MyClass(ReNameAbleClass):
    def __init__(self):
        pass

my_obj = MyClass()
print(my_obj)

MyClass.change_class_name('NewClassName')
print(my_obj)
