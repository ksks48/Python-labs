def f1(n):
    list1 = []
    for i in range (1,n+1):
        if i // 10 == 0:
            list1.append(i)
        else:
            while i // 10 > 0:
                a = i % 10
                list1.append(a)
                i = i // 10
            list1.append(i)
    #print(' + '.join(map(str, list1)), '=', sum(list1))

n = int(input("Enter n: "))
f1(n)
"""
def f2(n):
    #n = input("Please input an integer : ")
    n = int(n)
    item = range(1, n + 1)
    for i in item:
        sum = 0
        for j in range(1, i + 1):
            sum = sum + j
    #print(str(sum))

def f3(n):
    #x = input("Please input an integer: ")
    n = int(n)
    for i in range(1, n+1):
        nums = range(1, i+1)
        sum(nums)
        #print(' + '.join(map(str, nums)), '=', sum(nums))

n = 0
assert f1(n) == f2(n) == f3(n)
print('Looks like you pass all tests :)\n')

print('Let\'s check time' )
import time
import random
start = time.time()
f1(random.randint(1,10000))
stop = time.time()
print(f"Time for first function is {round(stop - start,2)} sec")
start = time.time()
f2(random.randint(1,10000))
stop = time.time()
print(f"Time for second function is {round(stop - start,2)} sec")
start = time.time()
f3(random.randint(1,10000))
stop = time.time()
print(f"Time for third function is {round(stop - start,2)} sec")
