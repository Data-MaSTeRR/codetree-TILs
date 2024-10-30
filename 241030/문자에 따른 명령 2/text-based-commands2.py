direction_total = input()

'''
direction_list = []
for direction in direction_total:
    direction_list.append(direction)
'''
# 북, 동, 남, 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

d = 4 # 방향
x, y = 0, 0
for direction in direction_total:

    if direction == 'L':
        d = (d - 1) % 4
    elif direction == 'R':
        d = (d + 1) % 4
    
    if direction == 'F':
        x += dxs[d]
        y += dys[d]
            
print(x, y)