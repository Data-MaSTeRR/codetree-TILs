s_list = input()

mapper = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3
}

# 북, 동, 남, 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x, y, t = 0, 0, 0
f_dir = 0
flag = False
for s in s_list:

    if s == 'L':
        f_dir = (f_dir - 1) % 4
    elif s == 'R':
        f_dir = (f_dir + 1) % 4
    else:
        x += dxs[f_dir]
        y += dys[f_dir]
    
    t += 1
    
    if x == 0 and y == 0:
        flag = True
        break

if flag == True:
    print(t)
else:
    print(-1)