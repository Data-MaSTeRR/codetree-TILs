N = int(input())
matrix = [ tuple(map(int, input().split())) for _ in range(N) ]

OFFSET = 100
MAX_K = OFFSET * 2 + 1

checked = [ [0] * MAX_K for _ in range(MAX_K) ]
for x, y in matrix:

    x += OFFSET
    y += OFFSET

    for i in range(x, x+8):
        for j in range(y, y+8):
            if checked[i][j] == 0:
                checked[i][j] = 1


cnt = 0
for x in range(MAX_K):
    for y in range(MAX_K):
        if checked[x][y] == 1:
            cnt += 1

print(cnt)