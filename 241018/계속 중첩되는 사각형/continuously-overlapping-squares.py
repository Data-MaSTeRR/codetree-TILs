n = int(input())
matrix = [ tuple(map(int, input().split())) for _ in range(n) ]

OFFSET = 100
MAX_K = OFFSET * 2 + 1

checked = [ [0] * MAX_K for _ in range(MAX_K) ]

cnt = 1
for x1, y1, x2, y2 in matrix:

    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):       

            # 홀수면 빨강(1)
            if cnt % 2 != 0:
                checked[x][y] = 1
                
            # 짝수면 파랑(2)
            elif cnt % 2 == 0:
                checked[x][y] = 2
        
    cnt += 1

blue_area = 0
for x in range(MAX_K):
    for y in range(MAX_K):
        if checked[x][y] == 2:
            blue_area += 1

print(blue_area)