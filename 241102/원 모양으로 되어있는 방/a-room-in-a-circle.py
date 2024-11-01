import copy
import sys

N = int(input())
vector = [ int(input()) for _ in range(N) ]

min_dist = sys.maxsize

for i in range(N):
    sum_dist = 0
    for idx in range(N):

        dist = (idx + N - i) % N
        sum_dist += dist * vector[idx]

    min_dist = min(min_dist, sum_dist)

print(min_dist)