y, m, d = map(int, input().split())

# 윤년이면 True
def yoon_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    
    return False

def last_day(m):

    ld = 31
    
    if m == 2:
        if yoon_year(y) == True:
            ld = 29
        else:
            ld = 28
    
    elif m == 4 or m == 6 or m == 9 or m == 11:
        ld = 30
    
    return ld

def check_day(m, d):

    if d <= last_day(m):
        return True

    return False

def four_seasons(m, d):

    if check_day(m, d) == False:
        return -1
    
    if m in [3, 4, 5]:
        return "Spring"
    
    elif m in [6, 7, 8]:
        return "Summer"
    
    elif m in [9, 10, 11]:
        return "Fall"
    
    elif m in [12, 1, 2]:
        return "Winter"


print(four_seasons(m, d))