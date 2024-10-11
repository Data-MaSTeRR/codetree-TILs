n = int(input())

def sumByrecursion(n):

    if n == 1:
        return 1

    return sumByrecursion(n - 1) + n

print(sumByrecursion(n))