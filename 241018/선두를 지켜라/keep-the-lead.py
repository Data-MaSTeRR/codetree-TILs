N, M = map(int, input().split())
A_matrix = [ tuple(map(int, input().split())) for _ in range(N) ]
B_matrix = [ tuple(map(int, input().split())) for _ in range(M) ]

MAX = 1000 * 1000
checked_A = [0] * (MAX + 1)
checked_B = [0] * (MAX + 1)

time_a = 1
for v, t in A_matrix:
    for i in range(t):
        checked_A[time_a] = checked_A[time_a - 1] + v
        time_a += 1

time_b = 1
for v, t in B_matrix:
    for i in range(t):
        checked_B[time_b] = checked_B[time_b - 1] + v
        time_b += 1


ans = 0
leader = 0
for idx in range(1, MAX + 1):

    if checked_A[idx] > checked_B[idx]:

        if leader == 2:
            ans += 1
        
        leader = 1

    if checked_A[idx] < checked_B[idx]:
        
        if leader == 1:
            ans += 1

        leader = 2


print(ans)