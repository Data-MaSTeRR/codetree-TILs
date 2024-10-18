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

### 첫번째에서 1만 찾고, 가로세로를 각각 비교하고 더 큰 값을 구해 그것을 곱함

checked = [ [0] * MAX_K for _ in range(MAX_K) ]
for x in range(ax1, ax2):
    for y in range(ay1, ay2):
        checked[x][y] = 1

for x in range(bx1, bx2):
    for y in range(by1, by2):
        if checked[x][y] == 1:
            checked[x][y] = 0
            
max_x_len = 0
max_y_len = 0
# X축 선분 최대 길이 구하기 -> ok
for i in range(MAX_K):
    temp = 0  # 매 행에 대해 초기화
    for j in range(MAX_K):
        if checked[i][j] == 1:
            temp += 1
        else:
            if temp > max_x_len:
        max_x_len = temp
        
    if temp > max_x_len:
        max_x_len = temp

# Y축 선분 최대 길이 구하기 -> 어렵네 공부좀 해야할 듯
for j in range(MAX_K):  # 열 순회
    temp = 0  # 매 열에 대해 초기화
    for i in range(MAX_K):  # 각 열에서 모든 행을 순회
        if checked[i][j] == 1:
            temp += 1
        else:
            if temp > max_y_len:
                max_y_len = temp
            temp = 0  # 연속이 끊겼으므로 temp를 초기화
    # 끝난 후 마지막으로 최대 값을 확인
    if temp > max_y_len:
        max_y_len = temp

# 결과 출력
print(f"{max_x_len * max_y_len}")