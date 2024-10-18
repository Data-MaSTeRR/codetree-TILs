N = int(input())
n_list = [ int(input()) for _ in range(N) ]


cnt, max_cnt = 0, 0
for idx in range(N):

    # idx가 1보다 크고 전의 원소와 같은 경우 에는 하나씩 더함
    if idx >= 1 and n_list[idx] == n_list[idx - 1]:
        cnt += 1
    # idx가 0이거나, 전의 원소와 다른 경우 1로 초기화
    else:
        cnt = 1
    
    # 최댓값을 초기화
    max_cnt = max(max_cnt, cnt)


print(max_cnt)