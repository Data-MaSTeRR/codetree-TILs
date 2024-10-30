N, M = map(int, input().split())
todo_matrix = [ tuple(map(int, input().split())) for _ in range(M) ]
matrix = [ [0] * N for _ in range(N) ]

# (y, x)
# 북, 동, 남, 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]


def in_range(x, y):
    return x >= 0 and y >= 0 and x < N and y < N


for y, x in todo_matrix:

    # index로 바꿔주기 위함
    y, x = y - 1, x - 1

    matrix[y][x] = 1

    cnt = 0
    for i in range(4):
        nx, ny = 0, 0
        nx = x + dxs[i]
        ny = y + dys[i]
        if in_range(nx, ny) and matrix[ny][nx] == 1:
            cnt += 1
    
        
    if cnt == 3:
        print(1)
    else:
        print(0)