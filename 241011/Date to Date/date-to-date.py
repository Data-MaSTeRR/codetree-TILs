m1, d1, m2, d2 = list(map(int, input().split()))

def daysCheck(x, y):

    m = 1
    d = 0

    num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    cum_d = 1
    while True:
        
        if m == x and d == y:
            break

        d += 1
        cum_d += 1

        if num_of_days[m] == d:
            m += 1
            d = 0


    return cum_d

print(daysCheck(m2, d2) - daysCheck(m1, d1))