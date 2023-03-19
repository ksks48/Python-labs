print ("Сума цифр: ")
print ("----------------------------------------------")
Num = int(input("Введіть число: "))
sum = 0
while (Num > 0):
    sum += Num % 10 
    Num //= 10
print ("Сума дорівнює " + str(sum)) 
