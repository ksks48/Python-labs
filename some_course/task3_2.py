class User:
    def __init__(self, age, name, user_type):
        self.age = age
        self.name = name
        self.__user_type = user_type
    
    def access_database(self):
        if self.__user_type == "superuser":
            print("access granted")
        else:
            print("access denied")

class SuperUser(User):
    def __init__(self, age, name, user_type):
        super().__init__(age, name, user_type)
        self.benefits = "access to whole computer"

u1 = User(age = 20, name = "Mike", user_type = "superuser")
u1.access_database()
u2 = User(age = 25, name = "John", user_type = "anotheruser")
u2.access_database()
u3 = SuperUser(age = 21, name = "Ksenia", user_type = "superuser")
print(u3.benefits)