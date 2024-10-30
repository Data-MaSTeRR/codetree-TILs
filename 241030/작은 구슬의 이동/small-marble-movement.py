# n x n / t초
n, t = tuple(map(int, input().split()))
# 초기값
y, x, c_dir = tuple(input().split())

# 각 알파벳 별 방향 번호를 설정합니다.
mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

# 행(y), 열(X)에 유의
x, y, move_dir = int(x) - 1, int(y) - 1, mapper[c_dir]

# 북, 동, 서, 남
dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# simulation 진행
for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    # 범위 안에 들어온다면 그대로 진행합니다.
    if in_range(nx, ny):
        x, y = nx, ny
    # 벽에 부딪힌다면, 방향을 바꿔줍니다. -> -3 하는 것의 방향주의
    else:
        move_dir = 3 - move_dir

# 행열로 출력이니 (y, x)
print(y + 1, x + 1)