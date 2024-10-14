N, K = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(K)]

block_list = [ 0 for _ in range(N) ]
for i_list in matrix:
    for i in range(i_list[0], i_list[1] + 1):
        block_list[i - 1] += 1

print(max(block_list))