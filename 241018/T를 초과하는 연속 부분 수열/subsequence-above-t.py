n, t = map(int, input().split())
n_list = list(map(int, input().split()))

cnt, max_cnt = 0, 0
for idx in range(n):

    if idx >= 1 and n_list[idx] > t and n_list[idx] > n_list[idx - 1]:
        cnt += 1
    elif idx == 0:
        cnt = 0
    else:
        cnt = 1
    
    max_cnt = max(max_cnt, cnt)


if cnt == 1:
    print(0)
else:
    print(max_cnt)