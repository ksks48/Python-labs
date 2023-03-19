print("обчислення добутку суми скінченного ряду")
print("--------------------------------------------")
k = int(input("Введіть k: "))
w = 0
i = -2
l = 1
if (k < 100000000):
    while i <= k:
        if(i == 4 and k == 4):
            break
        elif(i == 4 and k != 4):
            i += 1
            for c in range(1, i + 4):
                l *= c 
            w += (((-1) ** i)*l) / (2 * (i - 4))
        else: 
            for c in range(1, i + 4):
                l *= c 
            w += (((-1) ** i)*l) / (2 * (i - 4))
            i += 1
    print("Сума: " + str(w))
else:
    print("Число завелике!")