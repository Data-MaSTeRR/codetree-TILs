m1, d1, m2, d2 = list(map(int, input().split()))
A = input()

def daysCount(x, y):

    m = 1
    d = 1

    days_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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

def _7daysCount(m1, d1, m2, d2, A):

    days_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    daycnt = daysCount(m2, d2) - daysCount(m1, d1)
    dayweekcnt = daycnt // 7
    
    if ( daycnt % 7 ) >= days_week.index(A):
        dayweekcnt += 1

    return dayweekcnt

print(_7daysCount(m1, d1, m2, d2, A))