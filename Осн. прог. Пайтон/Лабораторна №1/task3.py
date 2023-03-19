print ("Яблука:")
print ("----------------------------------------------")
n = int(input("Скільки учнів: "))
k = int(input("Скільки яблук: "))

u_kojnogo = k // n
zalyshok = k % n

print ("У кожного учня по " + str(u_kojnogo) + " яблук")
print ("У кошику залишилось " + str(zalyshok) + " яблука")
