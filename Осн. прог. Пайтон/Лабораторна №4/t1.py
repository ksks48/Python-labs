n = int(input("Enter number of list: "))
numbers = []
count = 0
for i in range (n):
    num = int(input("Enter the element of list: "))
    numbers.append(num)
    if num % 2 == 0:
        count += 1
print("The list: " + str(numbers)) 
print("The number of even elements: " + str(count))   
