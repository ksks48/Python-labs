a = [4, 5, 6, 3, 2]


def iter_arr(array):
    for elem in array:
        print(elem)


def iter_rec(array, index=0):
    if index < len(array):
        print(array[index])
        index += 1
        iter_rec(array, index)


# def rec_count(index):
#     print(index)
#     index += 1
#     rec_count(index)
#
#
# rec_count(1)
