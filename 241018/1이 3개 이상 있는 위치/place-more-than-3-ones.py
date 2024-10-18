n = int(input())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

x, y = 0, 0
# 북, 동, 남, 서
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir_list = [0, 1, 2, 3]

def in_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True

cnt = 0
for x in range(n):
    for y in range(n):
  
        overcnt = 0
        for dir_num in dir_list:
            tempx, tempy = x, y
            tempx += dx[dir_num]
            tempy += dy[dir_num]
            if in_range(tempx, tempy) == True and matrix[tempx][tempy] == 1:
                overcnt += 1
           
        
        if overcnt >= 3:
            cnt += 1

print(cnt)