ax1, ay1, ax2, ay2 = tuple(map(int, input().split()))
bx1, by1, bx2, by2 = tuple(map(int, input().split()))

OFFSET = 1000
MAX_K = OFFSET * 2 + 1

ax1 += OFFSET
ay1 += OFFSET
ax2 += OFFSET
ay2 += OFFSET
bx1 += OFFSET
by1 += OFFSET
bx2 += OFFSET
by2 += OFFSET

### 첫번째에서 1만 찾고, (x,y)의 최대최소를 구하고 그것을 최종으로 이용함 (*)

checked = [ [0] * MAX_K for _ in range(MAX_K) ]
for x in range(ax1, ax2):
    for y in range(ay1, ay2):
        checked[x][y] = 1

for x in range(bx1, bx2):
    for y in range(by1, by2):
        if checked[x][y] == 1:
            checked[x][y] = 0

# 최소, 최대 값을 구하기 위한 초기화
min_x, min_y, max_x, max_y = MAX_K, MAX_K, 0, 0

# 남은 1의 영역에서 최소, 최대 좌표를 구함
for x in range(MAX_K):
    for y in range(MAX_K):
        if checked[x][y] == 1:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

# 최소, 최대 값이 바뀌지 않았을 경우 -> 유효한 영역이 없음
if min_x == MAX_K or min_y == MAX_K:
    print(0)
else:
    # X, Y 길이를 계산
    x_len = max_x - min_x + 1  # 마지막 좌표 포함
    y_len = max_y - min_y + 1  # 마지막 좌표 포함
    print(f"{x_len * y_len}")