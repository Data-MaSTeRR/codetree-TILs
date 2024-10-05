n, m = map(int, input().split())
n_list = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(m)]

idx_list = []
for i in range(m):
    for j in range(matrix[i][0], matrix[i][1] + 1):
        idx_list.append(j)

    list_sum = 0
    for idx in idx_list:
        list_sum += n_list[idx - 1]

    print(list_sum)
    idx_list = []