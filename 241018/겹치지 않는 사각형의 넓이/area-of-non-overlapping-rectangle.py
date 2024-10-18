# checked에 a, b 포함하여 1로 작성함 -> m을 참고하여 1로 된것 0 으로 바꿔줌 -> 이후 1로 표시된 것 세기

ax1, ay1, ax2, ay2 = tuple(map(int, input().split()))
bx1, by1, bx2, by2 = tuple(map(int, input().split()))
mx1, my1, mx2, my2 = tuple(map(int, input().split()))

OFFSET = 1000

checked = [ [0] * (OFFSET * 2 + 1) for _ in range(OFFSET * 2 + 1) ] 

def plus_squareArea(x1, y1, x2, y2, checked):

    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            if checked[x][y] == 0:
                checked[x][y] += 1

    return checked

def minus_squareArea(x1, y1, x2, y2, checked):

    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            if checked[x][y] == 1:
                checked[x][y] -= 1

    return checked

checked = plus_squareArea(ax1, ay1, ax2, ay2, checked)
checked = plus_squareArea(bx1, by1, bx2, by2, checked)
checked = minus_squareArea(mx1, my1, mx2, my2, checked)

cnt = 0
for x in range(OFFSET * 2 + 1):
    for y in range(OFFSET * 2 + 1):
        if checked[x][y] == 1:
            cnt += 1

print(cnt)