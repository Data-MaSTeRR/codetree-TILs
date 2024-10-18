N = int(input())
n_list = [ int(input()) for _ in range(N) ]

cnt, max_cnt = 0, 0
for idx in range(N):
    
    # 부호가 같은 경우
    if idx >= 1 and ( (n_list[idx] > 0 and n_list[idx - 1]) > 0 or (n_list[idx] < 0 and n_list[idx - 1] < 0) ):
        cnt += 1
    else:
        cnt = 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)