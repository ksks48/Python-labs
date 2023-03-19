from random import randint
"""def f1(n):
    x = 1
    list1 = [] 
    for i in range (n):
        status = True
        while status:
            if x % 3 == 0 and x % 5 == 0:
                list1.append(x)
                status = False
                x += 1
            else:
                x += 1  
    return list1

def f2(n):
    list_of_numbers = [i for i in range (n*100)]
    list2 = [x for x in list_of_numbers if (x % 3 == 0 and x % 5 == 0 and x )]
    list2 = list2[0:n]
    return list2

def f3(n):
    list3 = []
    x = 0
    i = 0
    while i < n:
        x += 3*5
        list3.append(x)
        i += 1
    return list3

def f4(n):
    random_list = []
    i = 0
    while i < n:
        x = randint(15, n*15)
        if x not in random_list and x % 15 == 0 and x // 15 == i+1:
            random_list.append(x)
            i += 1
    return random_list
    

n = int(input("Enter n: "))
print(f1(n))
print(f2(n))
print(f3(n))
print(f4(n))
print(" ")
assert f1(n) == f2(n) == f3(n) == f4(n)
print('Looks like you pass all tests :)\n')
"""

def f1(n):
    x = 1
    list1 = [] 
    for i in range (10000,n):
        status = True
        while status:
            if x % 3 == 0 and x % 5 == 0:
                list1.append(x)
                status = False
                x += 1
            else:
                x += 1  
    return list1

def f2(n):
    list_of_numbers = [i for i in range (10000,n*100)]
    list2 = [x for x in list_of_numbers if (x % 3 == 0 and x % 5 == 0 and x )]
    list2 = list2[0:n]
    return list2

def f3(n):
    list3 = []
    x = 0
    i = 10000
    while i < n:
        x += 3*5
        list3.append(x)
        i += 1
    return list3

def f4(n):
    random_list = []
    i = 1000
    while i < n:
        x = randint(15, n*15)
        if x not in random_list and x % 15 == 0 and x // 15 == i+1:
            random_list.append(x)
            i += 1
    return random_list

print('Let\'s check time' )
import time
start = time.time()
f1(randint(10000,100000))
stop = time.time()
print(f"Time for first function is {round(stop - start,2)} sec")
start = time.time()
f2(randint(10000,100000))
stop = time.time()
print(f"Time for second function is {round(stop - start,2)} sec")
start = time.time()
f3(randint(10000,100000))
stop = time.time()
print(f"Time for third function is {round(stop - start,2)} sec")
start = time.time()
f4(1200)
stop = time.time()
print(f"Time for forth function is {round(stop - start,2)} sec")
