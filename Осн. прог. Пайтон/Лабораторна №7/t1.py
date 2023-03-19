def f(n):
    new_dict = {}
    for i in range (1,n + 1):
        new_dict[str(i)] = i
    for a,b in new_dict.items():
        print(a + ":", end = " ")
        print(b)

n = int(input("Enter n: "))
f(n)