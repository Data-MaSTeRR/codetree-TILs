n = int(input())

def repeat(n):

    if n == 0:
        return
    
    repeat(n-1)
    print("*" * n)

repeat(n)