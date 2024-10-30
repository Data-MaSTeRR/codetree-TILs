N = int(input())
matrix = [ tuple(input().split()) for _ in range(N) ]

mapper = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

# 북, 동, 남, 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x, y, t = 0, 0, 0
flag = False
for direction, distance in matrix:

    if flag == True:
        break

    t_dir = mapper[direction]
    distance = int(distance)

    for i in range(distance):
        x += dxs[t_dir]
        y += dys[t_dir]
        t += 1
        if x == 0 and y == 0:
            flag = True
            break
    
if flag == True:
    print(t)
else:
    print(-1)