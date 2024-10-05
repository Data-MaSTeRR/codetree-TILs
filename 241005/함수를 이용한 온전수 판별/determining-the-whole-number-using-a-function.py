a, b = map(int, input().split())

# True가 온전수
def check(n):

    if n % 2 == 0 or n % 10 == 5:
        return False
    
    if n % 3 == 0 and n % 9 != 0:
        return False

    return True

cnt = 0
for n in range(a, b+1):

    if check(n) == True:
        cnt += 1

print(cnt)