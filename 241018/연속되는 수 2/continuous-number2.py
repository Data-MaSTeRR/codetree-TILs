N = int(input())
n_list = [ int(input()) for _ in range(N) ]


temp, max_cnt = 0, 0
for idx in range(N):
    
    if idx == 0:
        temp += 1
        continue

    if n_list[idx] != n_list[idx - 1]:
        
        if max_cnt < temp:
            max_cnt = temp
        
        temp = 0

    temp += 1

print(max_cnt)