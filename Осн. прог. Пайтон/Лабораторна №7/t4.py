def f(text):
    lst = []
    for i, char in enumerate(text):
        lst.append(char.lower())
    return ''.join(lst)

def check(my_dict):
    v = my_dict.values()
    v = list(v)
    x = max(v)
    idx1 = v.index(x)
    y = my_dict.keys()
    y = list(y)
    y1 = y.pop(idx1)
    print(str(y1) + ': ' + str(x))

def printed(dict):
    for a,b in dict.items():
        print(a + ":", end = " ")
        print(b)
    print('\n \n')


with open("text.txt") as file:
    text = file.read()
print(text)
text = text.replace('\n',' ')
text = text.replace('.','')
text = text.replace('(','')
text = text.replace(')','')
text = text.replace(':','')
text = text.replace('/','')
text = text.replace(',','')
text = text.replace('\'','')
text = text.replace('вЂ™s','')
text = text.replace('httpswww','')
text = text.replace('org','')
text = f(text).split()


my_dict = {}
for a in text:
    counter = 0
    for b in text:
        if a == b:
            counter += 1
    my_dict[a] = counter
    
print('\n \n')
print("::::::::::::::::::::::::::::::::DICTIONARY::::::::::::::::::::::::::::::::")
printed(my_dict)

print("Найуживаніше слово: ")
check(my_dict)
print('\n \n')

print("Словник у порядку зростання відповідно до ключів: ")
for a,b in sorted(my_dict.items()):
        print(a + ":", end = " ")
        print(b)
print('\n \n')

print("Словник у порядку зростання за значеннями: ")
new_sorted_dict = {}
for i in sorted(my_dict.values()):
    for k in my_dict.keys():
        if my_dict[k] == i:
            new_sorted_dict[k] = my_dict[k]
printed(new_sorted_dict)
