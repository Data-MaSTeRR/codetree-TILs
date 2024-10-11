n, k, T = input().split()
n, k = int(n), int(k)
matrix = [input() for _ in range(n)]

# 앞자리 같은지 확인
def frontCheck(full_s):
    cnt = 0
    for s in T:
        if full_s[cnt] != s:
            return False
        cnt += 1
    
    return True

T_list = []
for full_s in matrix:
    if frontCheck(full_s) == True:
        T_list.append(full_s)


T_list.sort()

print(T_list[k-1])