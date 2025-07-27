matrix = [ list(map(int, input().split())) for _ in range(2) ]
matrixT = list(map(list, zip(*matrix)))

for rowList in matrix:
    tempSum = 0
    for row in rowList:
        tempSum += row
    print(f'{tempSum/4:.1f}', end=' ')

print()

for colList in matrixT:
    tempSum = 0
    for col in colList:
        tempSum += col
    print(f'{tempSum/2:.1f}', end=' ')

print()

tempSum = 0
for row in range(2):
    for col in range(4):
        tempSum += matrix[row][col]

print(f'{tempSum/8:.1f}')