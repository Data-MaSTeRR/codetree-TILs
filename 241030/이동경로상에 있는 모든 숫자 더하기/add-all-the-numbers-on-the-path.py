N, T = map(int, input().split())
d_str = input()
matrix = [ list(map(int, input().split())) for _ in range(N) ]

##  북남 부호유의
# 북, 동, 남, 서
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

y, x, move_dir = N // 2, N // 2, 0

def in_range(y, x):
    if y >= 0 and x >= 0 and y < N and x < N:
        return True
    return False

pass_list = []
pass_list.append(matrix[y][x])
for d in d_str:

    if d == 'R':
        move_dir = ( move_dir + 1 ) % 4

    elif d == 'L':
        move_dir = ( move_dir - 1 ) % 4

    elif d == 'F':

        ny, nx = y + dys[move_dir], x + dxs[move_dir]
        if in_range(ny, nx) == True:
            y, x = ny, nx
            pass_list.append(matrix[y][x])

print(sum(pass_list))