N = int(input())
matrix = [ list(map(int, input().split())) for _ in range(N) ]

max_cnt = 0
for i in range(N):
    for j in range(N-3+1):
        max_cnt = max(max_cnt, matrix[i][j] + matrix[i][j+1] + matrix[i][j+2])

print(max_cnt)