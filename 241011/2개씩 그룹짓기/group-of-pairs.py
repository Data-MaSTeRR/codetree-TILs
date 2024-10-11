import itertools as it

N = int(input())
l = list(map(int, input().split()))

l.sort()

# 그룹의 합 중 최댓값을 구하기 위한 변수
max_sum = 0

# 가장 작은 값과 가장 큰 값을 묶어서 그룹을 만듦
for i in range(N):
    # i번째 작은 값과 i번째 큰 값을 짝지음
    group_sum = l[i] + l[2 * N - 1 - i]
    # 그 중에서 가장 큰 그룹 합을 저장
    max_sum = max(max_sum, group_sum)

print(max_sum)