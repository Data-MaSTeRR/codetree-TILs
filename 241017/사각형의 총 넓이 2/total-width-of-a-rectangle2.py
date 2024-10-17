N = int(input())
xy_matrix = [ tuple(map(int, input().split())) for _ in range(N) ] 

OFFSET = 100

checked = [ [0] * 201 for _ in range(201) ]

for xy_tuple in xy_matrix:

    x1 = xy_tuple[0] + OFFSET
    y1 = xy_tuple[1] + OFFSET
    x2 = xy_tuple[2] + OFFSET
    y2 = xy_tuple[3] + OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] += 1

cnt = 0
for x in checked:
    for y in x:
        if y >= 1:
            cnt += 1

print(cnt)