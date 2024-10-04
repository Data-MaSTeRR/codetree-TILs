a, b = map(int, input().split())

def three_six_nine(n):
    
    ten = n // 10
    one = n % 10

    if ten in [3, 6, 9] or one in [3, 6, 9] or n % 3 == 0:
        return True

cnt = 0
for n in range(a, b+1):
    if three_six_nine(n) == True:
        cnt += 1

print(cnt)