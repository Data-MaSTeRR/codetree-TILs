N = int(input())
go_matrix = [ tuple(input().split()) for _ in range(N) ]

x, y = 0, 0
# 서남북동
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]


for dn_tuple in go_matrix:

    direction = dn_tuple[0]
    distance = int(dn_tuple[1])

    if direction == "W":
        x, y = x + (dx[0] * distance), y + dy[0]
    
    elif direction == "S":
        x, y = x + dx[1], y + (dy[1] * distance)
     
    elif direction == "N":
        x, y = x + dx[2], y + (dy[2] * distance) 
    
    elif direction == "E":
        x, y = x + (dx[3] * distance), y + dy[3]
    
print(x, y)