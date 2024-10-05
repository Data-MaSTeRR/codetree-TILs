n, m = map(int, input().split())
n_list = list(map(int, input.split()))
matrix = [list(map(int, input().split())) for _ in range(m)]

list_sum = 0
for i in range(m):
    for j in range(2):
        list_sum += n_list[matrix[i][j] - 1]

print(list_sum)