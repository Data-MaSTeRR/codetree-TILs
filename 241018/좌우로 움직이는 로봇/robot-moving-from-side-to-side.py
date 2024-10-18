n, m = map(int, input().split())
matrixA = [ tuple(input().split()) for _ in range(n) ]
matrixB = [ tuple(input().split()) for _ in range(m) ]

OFFSET = 500000
MAX = OFFSET * 2 + 1

checkA = [0] * MAX
checkB = [0] * MAX

time_a = 1
for nd_tuple in matrixA:

    distance = int(nd_tuple[0])
    direction = nd_tuple[1]

    for _ in range(distance):

        if direction == "R":
            checkA[time_a] = checkA[time_a - 1] + 1

        elif direction == "L":
            checkA[time_a] = checkA[time_a - 1] - 1
        
        time_a += 1

time_b = 1
for nd_tuple in matrixB:

    distance = int(nd_tuple[0])
    direction = nd_tuple[1]

    for _ in range(distance):

        if direction == "R":
            checkB[time_b] = checkB[time_b - 1] + 1

        elif direction == "L":
            checkB[time_b] = checkB[time_b - 1] - 1
        
        time_b += 1

cnt = 0
for idx in range(2, MAX):

    if checkA[idx] == checkB[idx] and abs(checkA[idx - 1] - checkB[idx - 1]) == 2:
        cnt += 1

print(cnt)