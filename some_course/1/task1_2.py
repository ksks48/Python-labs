class Cat:
    def __init__(self, color, cat_type):
        self.color = color
        self.cat_type = cat_type

    def set_size(self):
        if(self.cat_type == "indoor"):
            self.size = "small"
        else:
            self.size = "undefined"
        print(self.size)

print("Cat:")
small_cat = Cat("black", "indoor")
small_cat.set_size()
another_cat = Cat("white", "wild")
another_cat.set_size()


class Tiger(Cat):
    def set_size(self):
        if(self.cat_type == "wild"):
            self.size = "big"
        else:
            self.size = "undefined"
        print(self.size)

print("\nTiger:")
small_tiger = Tiger("orange", "pretty")
small_tiger.set_size()
big_tiger = Tiger("orange", "wild")
big_tiger.set_size()