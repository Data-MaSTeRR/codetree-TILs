a, b, c = list(map(int, input().split()))

def minCheck(x, y, z):

    d = 11
    h = 11
    m = 11

    cum_m = 0

    if x < 11 or (x == 11 and y < 11) or (x == 11 and y == 11 and z < 11):
        return -1

    while True:

        if d == x and h == y and m == z:
            break
        
        m += 1
        cum_m += 1

        if m == 60:
            h += 1
            m = 0
        
        if h == 24:
            d += 1
            h = 0
            m = 0
        
    
    return cum_m


print(minCheck(a, b, c))