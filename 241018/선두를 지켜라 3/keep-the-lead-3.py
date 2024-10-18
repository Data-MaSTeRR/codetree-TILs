N, M = map(int, input().split())
matrixA = [ map(int, input().split()) for _ in range(N) ]
matrixB = [ map(int, input().split()) for _ in range(M) ]

MAX = 1000000 + 1
checkA = [0] * MAX
checkB = [0] * MAX

time_a = 1
for v, t in matrixA:

    for _ in range(t):
        checkA[time_a] = checkA[time_a - 1] + v
        time_a += 1

time_b = 1
for v, t in matrixB:

    for _ in range(t):
        checkB[time_b] = checkB[time_b - 1] + v
        time_b += 1

leader = 0    
cnt = 0
time_min = min(time_a, time_b)
for idx in range(1, time_min):

    # A가 선두라면
    if checkA[idx] > checkB[idx]:

        if leader != 1:
            cnt += 1

        leader = 1
    
    # B가 선두라면
    elif checkA[idx] < checkB[idx]:

        if leader != 2:
            cnt += 1

        leader = 2

    # 공동선두라면
    else:
        if leader != 3:
            cnt += 1

        leader = 3

print(cnt)