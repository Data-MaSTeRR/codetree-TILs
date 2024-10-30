N = int(input())
dd_matrix = [ tuple(input().split()) for _ in range(N) ]

# 북, 동, 남, 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x, y = 0, 0
temp = 0
for dd_tuple in dd_matrix:

    direction, distance = dd_tuple[0], int(dd_tuple[1])

    if direction == 'N':
        temp = 0
    elif direction == 'E':
        temp = 1
    elif direction == 'S':
        temp = 2
    elif direction == 'W':
        temp = 3

    x += dxs[temp] * distance
    y += dys[temp] * distance


print(x, y)