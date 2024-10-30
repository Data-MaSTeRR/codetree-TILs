n, m = map(int, input().split())
matrix = [ [0] * m for _ in range(m) ]

## 남북 부호유의
# 동, 남, 서, 북
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

y, x, move_dir = 0, 0, 0

def in_range(y, x):
    return y >= 0 and x >= 0 and y < n and x < m

matrix[0][0] = chr(65) 

# chr(65) = A / ord(A) = 65
for i in range(66, 64 + (n*m + 1)):

    ny, nx = y + dys[move_dir], x + dxs[move_dir]
    
    if in_range(ny, nx) == False or matrix[ny][nx] != 0:
        move_dir = (move_dir + 1) % 4
        ny, nx = y + dys[move_dir], x + dxs[move_dir]
    
    matrix[ny][nx] = chr(i)
    y, x = ny, nx


for y in range(n):
    for x in range(m):
        print(matrix[y][x], end = ' ')
    print()