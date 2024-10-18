N = int(input())
go_matrix = [ tuple(input().split()) for _ in range(N) ]

x, y = 0, 0
# 서남북동
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]


for dn_tuple in go_matrix:

    c_dir = dn_tuple[0]
    dist = int(dn_tuple[1])

    # 각 방향에 맞는 번호를 붙여줍니다.
    if c_dir == 'W':
        move_dir = 0
    elif c_dir == 'S':
        move_dir = 1
    elif c_dir == 'N':
        move_dir = 2
    elif c_dir == 'E':
        move_dir = 3

    # 주어진 방향대로 dist 거리만큼 이동했을 경우의
    # 위치를 구해줍니다.
    x += dx[move_dir] * dist
    y += dy[move_dir] * dist
    
print(x, y)