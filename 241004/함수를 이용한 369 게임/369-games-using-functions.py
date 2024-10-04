a, b = map(int, input().split())

def three_six_nine(n):
    
    str_n = str(n)

    if "3" in str_n or "6" in str_n or "9" in str_n or n % 3 == 0:
        return True

cnt = 0
for n in range(a, b+1):
    if three_six_nine(n) == True:
        cnt += 1

print(cnt)