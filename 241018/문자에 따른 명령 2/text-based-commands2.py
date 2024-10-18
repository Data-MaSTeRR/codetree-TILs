dir_list = list(input())

x, y = 0, 0
# 북, 동, 남, 서
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0


for idx in dir_list:

    if idx == "L":
        dir_num = (dir_num - 1) % 4

    elif idx == "R":
        dir_num = (dir_num + 1) % 4
    
    elif idx == "F":
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)