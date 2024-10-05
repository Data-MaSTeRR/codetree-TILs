N = int(input())

def repeat(N):
    
    if N == 0:
        return

    print(N, end= " ")
    repeat(N-1)
    print(N, end= " ")

repeat(N)