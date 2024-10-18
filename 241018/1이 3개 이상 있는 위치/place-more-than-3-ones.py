n = int(input())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

x, y = 0, 0
# 북, 동, 남, 서
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir_list = [0, 1, 2, 3]

def in_range(x, y):
    if x >= 0 and y >= 0 and x < 5 and y < 5:
        return True

cnt = 0
for y in range(n):
    for x in range(n):
        for dir_num in dir_list:
            x += dx[dir_num]
            y += dy[dir_num]
            if matrix[x][y] == 1 and in_range(x, y):
                cnt += 1

print(cnt)