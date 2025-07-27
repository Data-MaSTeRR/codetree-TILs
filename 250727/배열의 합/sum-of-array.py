matrix = [ list(map(int, input().split())) for _ in range(4) ]

for row in range(4):
    tempSum = 0
    for col in range(4):
        tempSum += matrix[row][col]
    print(tempSum)