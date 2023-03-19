def change_key(dict1, string1, string2):
    sum = 0
    for i in dict1:
        sum += dict1.get(i,0)
    dict1[string1] = sum
    for a,b in dict1.items():
        print(a + ":", end = " ")
        print(b)
    dict1.popitem()
    dict1[string2] = sum
    for a,b in dict1.items():
        print(a + ":", end = " ")
        print(b)

dict1 = dict([
            ('1', 1),
            ('2', 2),
            ('3', 3),
            ('4', 4),
            ('5', 5),
            ('6', 6),
            ('7', 7),
            ('8', 8),
            ('9', 9),
            ('10', 10)])
change_key(dict1, 'total', 'sum')