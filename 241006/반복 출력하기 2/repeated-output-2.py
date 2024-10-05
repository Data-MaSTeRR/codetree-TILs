N = int(input())

def repeat(N):
    if N == 0:
        return 
    
    repeat(N - 1)
    print("HelloWorld")

repeat(N)