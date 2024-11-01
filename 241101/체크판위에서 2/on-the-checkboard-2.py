R, C = map(int, input().split())
matrix = [ input().split() for _ in range(R) ]

# 이동 시에 행과 열이 전부 증가하도록
# 모든 쌍을 다 잡아봅니다.

cnt = 0
# 모든 상태소에 위치할 때
for i in range(1, R):
    for j in range(1, C):
        # 그 외의 부분을 탐색
        for k in range(i+1, R-1):
            for l in range(j+1, C-1):

                if matrix[0][0] != matrix[i][j] and matrix[i][j] != matrix[k][l] and matrix[k][l] != matrix[R-1][C-1]:
                    cnt += 1

print(cnt)