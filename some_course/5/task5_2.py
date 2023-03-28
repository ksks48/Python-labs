"""type NO or YES if N is pow of 2"""
N = int(input())

def rec(N):
    """recursion"""
    if N == 1:
        print("YES")
    else:
        if N % 2 == 0:
            rec(N // 2)
        else:
            print("NO")
            return

rec(N)
