import copy, sys

N, S = map(int, input().split())
n_list = list(map(int, input().split()))

min_n = sys.maxsize
for i in range(N-1):
    for j in range(i+1, N):

        copy_list = copy.deepcopy(n_list)
        copy_list.pop(i)
        copy_list.pop(j-1)

        min_n = min(abs(sum(copy_list) - 20), min_n)
    
print(min_n)