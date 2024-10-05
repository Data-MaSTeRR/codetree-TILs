M, D = map(int, input().split())

def lastday_number(M):
    
    if M == 2:
        return 28
    if M == 4 or M == 6 or M == 9 or M == 11:
        return 30
    
    return 31

def judge_day(M, D):

    if M <= 12 and D <= lastday_number(M):
        return True
    
    return False

if judge_day(M, D) == True:
    print("Yes")

if judge_day(M, D) == False:
    print("No")