n = int(input())
n_list = list(map(int, input().split()))

sum_n, max_n = 0, 0
for i in range(n-2):
    for j in range(i+2, n):
        sum_n = n_list[i] + n_list[j]
        max_n = max(sum_n, max_n)

print(max_n)