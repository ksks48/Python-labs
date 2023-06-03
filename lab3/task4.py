def change_class_name(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        print("ValueError('Invalid class name')")
    else:
        cls.__name__ = new_name
class MyClass:
    pass

change_class_name(MyClass, "UsefulClass")
print(MyClass.__name__)
change_class_name(MyClass, "secondUsefulClass")
print(MyClass.__name__)