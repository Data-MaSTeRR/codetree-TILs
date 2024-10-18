N = int(input())
n_list = [ int(input()) for _ in range(N) ] 

cnt, max_cnt = 0, 0
for idx in range(N):
    
    # 뒤의 값이 앞의 인덱스보다 큰 경우
    if idx >= 1 and n_list[idx] > n_list[idx - 1] :
        cnt += 1
    else:
        cnt = 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)