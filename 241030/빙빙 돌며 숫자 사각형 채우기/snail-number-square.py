n, m = map(int, input().split())
matrix = [ [0] * m for _ in range(n) ]

y, x = 0, 0
matrix[y][x] = 1

# 동, 남, 서, 북 -> 남북 유의 부호
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
f_dir = 0

def in_range(y, x):
    if x >= 0 and y >= 0 and x < m and y < n:
        return True
    return False


# n*m번 진행합니다.
for i in range(2, n * m + 1):
    # 현재 방향 dir를 기준으로 그 다음 위치 값을 계산합니다.
    nx, ny = x + dxs[f_dir], y + dys[f_dir]
    
    # 더 이상 나아갈 수 없다면
    # 시계방향으로 90'를 회전합니다.
    if not in_range(ny, nx) or matrix[ny][nx] != 0:
        f_dir = (f_dir + 1) % 4

    # 그 다음 위치로 이동한 다음 배열에 올바른 값을 채워넣습니다.
    x, y = x + dxs[f_dir], y + dys[f_dir]
    matrix[y][x] = i

for y in range(n):
    for x in range(m):
        print(matrix[y][x], end = ' ')
    print()