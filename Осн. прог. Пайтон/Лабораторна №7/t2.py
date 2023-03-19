def sum_dict_vals (dict, string):
    sum = 0
    for i in dict1:
        sum += dict1.get(i)
    dict[string] = sum
    for a,b in dict.items():
        print(a + ":", end = " ")
        print(b)

#or
"""def sum_dict_vals (dict, string):
    sum = 0
    list_for_values = dict.values()
    for i in list_for_values:
        sum += int(i)
    dict[string] = sum
    for a,b in dict.items():
        print(a + ":", end = " ")
        print(b)"""

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
sum_dict_vals (dict1, 'total')