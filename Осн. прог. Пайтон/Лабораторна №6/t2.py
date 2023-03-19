def f(ch):
    print(ch)
    if ch.isalpha() == False:
        print("ERROR")
        exit()
    list_for_new_items = []
    for i in ch:
        if i == 'я':
            i1 = 'а'   
            list_for_new_items.append(i1) 
        if ch == 'Я':
            i1 = 'А'   
            list_for_new_items.append(i1)
        else:
            i1 = chr(ord(i) + 1)
            list_for_new_items.append(i1)   
    if "я" in ch:        
        return list_for_new_items[:-1]
    else:
        return list_for_new_items

ch = ' абвгдя  '.strip()
print(f(ch))
assert f(ch) == ['б','в','г','д','е','а']
print("SUCCESS")