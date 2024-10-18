N, M = map(int, input().split())
A_matrix = [ tuple(input().split()) for _ in range(N) ]
B_matrix = [ tuple(input().split()) for _ in range(M) ]

MAX = 1000000 + 1

checked_A, checked_B = [0] * MAX , [0] * MAX

# A에 정렬해보자
time_a = 1
for nd_tuple in A_matrix:

    direction = nd_tuple[0]
    distance = int(nd_tuple[1])

    for _ in range(distance):
      
        if direction == "R":
            checked_A[time_a] = checked_A[time_a - 1] + 1
        
        elif direction == "L":
            checked_A[time_a] = checked_A[time_a - 1] - 1
        
        time_a += 1


time_b = 1
for nd_tuple in B_matrix:

    direction = nd_tuple[0]
    distance = int(nd_tuple[1])

    for _ in range(distance):
      
        if direction == "R":
            checked_B[time_b] = checked_B[time_b - 1] + 1
        
        elif direction == "L":
            checked_B[time_b] = checked_B[time_b - 1] - 1
        
        time_b += 1


ans = -1
time_min = min(time_a, time_b)
for idx in range(1, time_min):
    if checked_A[idx] == checked_B[idx]:
        ans = idx
        break

print(ans)