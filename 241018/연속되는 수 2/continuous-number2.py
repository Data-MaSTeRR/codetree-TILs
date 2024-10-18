N = int(input())
n_list = [ int(input()) for _ in range(N) ]

cnt = 0
for idx in range(N):
    if idx == 0:
        cnt += 1
        continue
    if n_list[idx] != n_list[idx - 1]:
        cnt += 1

print(cnt)