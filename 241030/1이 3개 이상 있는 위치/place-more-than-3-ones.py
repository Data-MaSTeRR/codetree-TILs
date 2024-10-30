n = int(input())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

# 북, 동, 남, 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 범위내 있는지 확인하는 함수
def in_range(x, y):
    if x < 0 or y < 0 or x >= n or y>= n:
        return False
    return True

def count(x, y):
    
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) == True and matrix[ny][nx] == 1:
            cnt += 1

    return cnt

ans = 0
for y in range(n):
    for x in range(n):
        if count(x, y) >= 3:
            ans += 1

print(ans)