n = int(input())
matrix = [ tuple(input().split()) for _ in range(n) ]

MAX_K = 100000
cur_loc = MAX_K
cur_color = [0] * (MAX_K * 2 + 1)
cnt_black, cnt_white = 0, 0

for nd_tuple in matrix:

    distance = int(nd_tuple[0])
    direction = nd_tuple[1]

    x = distance

    if direction == "R":

        while x > 0:

            cur_color[cur_loc] = 2
            x -= 1 

            if x:
                cur_loc += 1

    elif direction == "L":

        while x > 0:

            cur_color[cur_loc] = 1
            x -= 1

            if x:
                cur_loc -= 1

for loc in cur_color:

    if loc == 2:
        cnt_black += 1
    
    elif loc == 1:
        cnt_white += 1

print(cnt_white, cnt_black)