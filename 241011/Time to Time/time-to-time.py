a, b, c, d = list(map(int, input().split()))

def cum_times(x, y):

    h = 0
    m = 0

    cum_min = 0
    while True:
        
        if h == x and m == y:
            break

        m += 1
        cum_min += 1

        if m == 60:
            h += 1
            m = 0
    
    return cum_min

print(cum_times(c, d) - cum_times(a, b))