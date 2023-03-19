def f(ch):
    print(ch)
    n = []
    counter = 0 
    for i in ch:
        if counter < 2:
            for j in i:
                n.append(j)
                counter += 1
                break
        else:
            n.append(i)
    print('. '.join(n))

ch = "Володимир Олександрович Зеленський".split()
f(ch)
ch = "Валерій Федорович Залужний".split()
f(ch)
