import copy

N = int(input())
matrix = [ list(map(int, input().split())) for _ in range(N) ]


def manhattan_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# 처음과 마지막을 제외하고 하나씩 빼보자
for idx in range(1, N-1):
    temp_matrix = copy.deepcopy(matrix)
    temp_matrix.pop(idx)
    #print(temp_matrix)
    distance = 0
    for i in range(N-2):
        x1, y1 = temp_matrix[i][0], temp_matrix[i][1]
        x2, y2 = temp_matrix[i+1][0], temp_matrix[i+1][1]
        #print(x1, y1, x2, y2)
        distance += manhattan_distance(x1, x2, y1, y2)
        #print(distance)
        
    if idx == 1:
        min_distance = distance

    min_distance = min(min_distance, distance)

print(min_distance)