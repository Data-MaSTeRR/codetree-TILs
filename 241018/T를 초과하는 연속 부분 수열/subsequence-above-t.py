n, t = map(int, input().split())
n_list = list(map(int, input().split()))

cnt, max_cnt = 0, 0
for n in n_list:
    
    if n > t:
        cnt += 1
        max_cnt = max(max_cnt, cnt)   
    else:
        cnt = 0
    
    
if max_cnt == 0:
    print(0)
else:
    print(max_cnt)