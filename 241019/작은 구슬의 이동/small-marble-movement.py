n, t = map(int, input().split())
r, c, d = input().split()

### 가장 왼쪽 위의 격자!! 제4사분면
# 각 알파벳 별 방향 번호를 설정합니다.
mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

# x열, y행
y, x = int(r) - 1, int(c) - 1
# 북, 동, 서, 남
dy, dx = [-1, 0, 0, 1], [0, 1, -1, 0]
dir_num = mapper[d]

def in_range(x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        return True

for _ in range(t):
    
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if in_range(nx, ny):
        x, y = nx, ny

    else:
        dir_num = 3 - dir_num
    
print(y + 1, x + 1)