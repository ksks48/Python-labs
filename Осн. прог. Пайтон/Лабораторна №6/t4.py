def f(ch):
    print(ch)
    new_list = []
    for i in ch:
        letters = []
        for j in i:
            letters.append(j)
        letters.reverse()
        
        new_list.append("".join(letters))
        new_list.append(" ")
    new_list = new_list[:-1]
    print("".join(new_list))

ch = "Hello world!".split()
f(ch)
