n = int(input())
matrix = [ [0] * n for _ in range(n) ]

## 북남 부호 유의
# 동, 북, 서, 남
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

y, x, move_dir = n // 2, n // 2, 0

def in_range(y, x):
    return y >= 0 and x >= 0 and y < n and x < n

matrix[y][x] = 1

for i in range(2, n*n + 1):

    ny, nx = y + dys[move_dir], x + dxs[move_dir]

    if in_range(ny, nx) == False or matrix[ny][nx] != 0:
        move_dir = (move_dir + 1) % 4
        ny, nx = y + dys[move_dir], x + dxs[move_dir]

    matrix[ny][nx] = i
    y, x = ny, nx

for row in range(n):
    for column in range(n):
        print(matrix[row][column], end = ' ')
    print()