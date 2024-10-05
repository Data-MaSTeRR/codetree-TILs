a, b = map(int, input().split())

def rule(a, b):

    if a > b:
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25
    
    return a, b

a, b = rule(a, b)
print(a, b)