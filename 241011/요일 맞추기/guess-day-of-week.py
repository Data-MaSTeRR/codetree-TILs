m1, d1, m2, d2 = list(map(int, input().split()))

def daysCount(x, y):

    m = 1
    d = 1
    
    days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    cum_d = 0
    while True:

        if m == x and d == y:
            break
        
        d += 1
        cum_d += 1
        
        if days_month[m] == d:
            m += 1
            d = 0

    return cum_d


def _7daysCheck(m1, d1, m2, d2):
   
    one_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    idx = (daysCount(m2, d2) - daysCount(m1, d1)) % 7

    return one_days[idx]


print(_7daysCheck(m1, d1, m2, d2))