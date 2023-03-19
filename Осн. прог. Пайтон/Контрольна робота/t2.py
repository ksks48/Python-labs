def f(my_list):
    first_list = []
    second_list = []
    for i in my_list:
        if i < 0:
            first_list.append(i)
        else:
            second_list.append(i)
    first_list.sort()
    second_list.sort()
    second_list.reverse()
    new_list = []
    for a in first_list:
        new_list.append(a)
    for b in second_list:
        new_list.append(b)
    return new_list

my_list = [53, -1, -45, 1, -3, 726, 20, -3, 0] 
print(f(my_list))
my_list = [53, -1, -45, 1, -3, 726, 20, -3, 0]
assert f(my_list) == [-45, -3, -3, -1, 726, 53, 20, 1, 0]
my_list = [-1, -835, 1, 36, -3, 0]
assert f(my_list) == [-835, -3, -1, 36, 1, 0]
print("SUCCESS")