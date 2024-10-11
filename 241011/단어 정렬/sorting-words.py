n = int(input())
matrix = [ input() for _ in range(n)]

matrix.sort()
for i in matrix:
    print(i)