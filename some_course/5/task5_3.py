"""sum of numbers"""
N = int(input())

def rec(N, sum = 0):
    """sum"""
    if N > 0:
        rec(N // 10, sum + N % 10)
    else:
        print(sum)

rec(N)
