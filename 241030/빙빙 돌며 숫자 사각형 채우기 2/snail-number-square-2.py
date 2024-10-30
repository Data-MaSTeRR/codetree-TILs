n, m = map(int, input().split())
matrix = [ [0] * m for _ in range(n) ]

## 남 북 부호방향 반대!
# 남, 동, 북, 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x, y, move_dir = 0, 0, 0

def in_range(y, x):
    return y >= 0 and x >= 0 and y < n and x < m

matrix[y][x] = 1

for i in range(2, n * m + 1):

    ny, nx = y + dys[move_dir], x + dxs[move_dir]

    if in_range(ny, nx) and matrix[ny][nx] == 0:
        matrix[ny][nx] = i


    else:
        move_dir = (move_dir + 1) % 4
        ny, nx = y + dys[move_dir], x + dxs[move_dir]
        matrix[ny][nx] = i
    
    y, x = ny, nx 

        

for y in range(n):
    for x in range(m):
        print(matrix[y][x], end = ' ')
    print()