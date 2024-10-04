def special_sum(N):

    special_sum = 0
    for n in range(1, N+1):
        special_sum += n 

    return special_sum


N = int(input())
special_sum = special_sum(N)
print(special_sum // 10)