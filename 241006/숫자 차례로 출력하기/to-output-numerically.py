N = int(input())

def repeat(N):

    if N == 0:
        return
    
    repeat(N-1)
    print(N, end = " ")

def repeat_reverse(N):

    if N == 0:
        return
    
    print(N, end = " ")
    repeat_reverse(N-1)

repeat(N)
print()
repeat_reverse(N)