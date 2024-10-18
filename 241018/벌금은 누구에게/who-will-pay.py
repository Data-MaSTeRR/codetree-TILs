N, M, K = map(int, input().split())
n_list = [ int(input()) for _ in range(M) ]

chance_list = [K] * N 

first_student = -1
for n in n_list:

    chance_list[n - 1] -=1

    if 0 in chance_list:
        first_student = chance_list.index(0) + 1
        break

print(first_student)