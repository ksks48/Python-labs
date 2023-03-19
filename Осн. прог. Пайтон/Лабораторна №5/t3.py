"""def function(n1,n2):
    list1 = []
    for i in range (n1):
        num1 = int(input("Enter the element of first list: "))
        list1.append(num1)

    list2 = []
    for i in range (n2):
        num2 = int(input("Enter the element of second list: "))
        list2.append(num2)

    print(" ")
    #print("First list: " + str(list1))
    #print("Second list: " + str(list2))

    if n1 > n2:
        n = n1
        for i in range (n2,n):    
            list2.append(0)
    else:
        n = n2
        for i in range (n1,n):    
            list1.append(0)

    list_of_sum = []
    for j in range (n):    
        num = list1[j]+list2[j]
        list_of_sum.append(num)
    print(" ")
    #print("List of sum: " + str(list_of_sum))

n1 = int(input("Enter range of list: "))
n2 = int(input("Enter range of list: "))
function(n1,n2)
"""


def function(n1,n2):
    list1 = []
    for i in range (n1):
        num1 = random.randint(-10,10)
        list1.append(num1)

    list2 = []
    for i in range (n2):
        num2 = random.randint(-10,10)
        list2.append(num2)

    #print(" ")
    #print("First list: " + str(list1))
    #print("Second list: " + str(list2))

    if n1 > n2:
        n = n1
        for i in range (n2,n):    
            list2.append(0)
    else:
        n = n2
        for i in range (n1,n):    
            list1.append(0)

    list_of_sum = []
    for j in range (n):    
        num = list1[j]+list2[j]
        list_of_sum.append(num)
    #print(" ")
    #print("List of sum: " + str(list_of_sum))

def f2(n1,n2):
    #n1=int(input())
    num1 = list(map(int, input(random.randint(-10,10)).split()))
    #n2=int(input())
    num2 = list(map(int, input(random.randint(-10,10)).split()))
    sum=[]

    for i in range(0,n1):
        sum.append(num1[i]+num2[i])

    #for element in sum:
        #print(element, end=" ")

    #print("")
    
print('Let\'s check time' )
import time
import random
start = time.time()
function(random.randint(1,1000),random.randint(1,1000))
stop = time.time()
print(f"Time for first function is {round(stop - start,2)} sec")
start = time.time()
f2(random.randint(1,1000),random.randint(1,1000))
stop = time.time()
print(f"Time for first function is {round(stop - start,2)} sec")
