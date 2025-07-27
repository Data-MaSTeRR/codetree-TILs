#n, m = map(int, input().split())
matrix = [ list(input().split()) for _ in range(5) ]
#print(matrix)

for row in range(5):
    for col in range(3):
        print(matrix[row][col].upper(), end=' ')
    print()
    