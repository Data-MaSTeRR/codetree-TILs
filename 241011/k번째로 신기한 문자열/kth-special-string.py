n, k, T = input().split()
n, k = int(n), int(k)
matrix = [input() for _ in range(n)]

matrix.sort()
print(matrix[k])