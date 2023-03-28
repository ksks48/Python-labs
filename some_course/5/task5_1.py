"""type numbers from 1 to N"""
N = int(input())

def rec(N, index = 1):
    """recursion"""
    if index > N:
        return
    else:
        print(index)
        rec(N, index + 1)

rec(N)

#another

def rec_2(N, index = 1, list_for_val = []):
    """recursion"""
    if index > N:
        print(list_for_val)
        return
    else:
        list_for_val.append(index)
        rec_2(N, index + 1)

rec_2(N)
