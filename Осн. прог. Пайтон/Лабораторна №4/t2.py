num = int(input("How many elements do you want to sort: "))
numbers_first = []
numbers_second = []
for i in range (num):
    var = int(input("Enter the element of list: "))
    numbers_first.append(var)
print("The list: " + str(numbers_first)) 
numbers_second = numbers_first
for i in range (num):
    for j in range (num):
        if numbers_first[i] == numbers_second[j] and i != j:
            print("Ind of the numbers: " + str(i) + ", " + str(j))
            exit()
            