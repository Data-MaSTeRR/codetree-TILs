a, b = map(int, input().split())

def some_sqaure(a, b):

    result = 1
    for _ in range(b):
        result *= a
    
    return result

print(some_sqaure(a, b))