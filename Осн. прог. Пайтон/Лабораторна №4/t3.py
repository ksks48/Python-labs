num = int(input("How many elements do you want to sort: "))
numbers = []
ind = -1
for i in range (num):
    var = int(input("Enter the element of list: "))
    numbers.append(var)
print("The list: " + str(numbers)) 
d = int(input("Enter the element of list that you want to delete: "))
for i in range (num):
    if numbers[i] == d:
        ind = i
        break
for i in range (num):
    if ind > -1:
        if i < ind:
            del numbers[0]
print("The list: " + str(numbers))