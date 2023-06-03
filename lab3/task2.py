class myList:
    def __init__(self):
        self.items = []
        self.count = 0

    def add(self, item):
        self.items.append(item)
        self.count += 1
        return self

    def __str__(self):
        return str(self.items)

my_list = myList()
my_list.add(0).add(1)
print(my_list)
