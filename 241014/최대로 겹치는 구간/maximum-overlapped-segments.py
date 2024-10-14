n = int(input())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

## 음수값도 고려해야함!! -> 0~200 구간으로 하기 위해 100을 더해주자

# 모든 리스트의 원소값 일렬로 정렬, 그리고 max값 찾기
max_num = 0
num_list = []
for n_list in matrix:
    for i in range(n_list[0] + 100, n_list[1] + 100 + 1):
        num_list.append(i)

print(num_list)

# 원소마다 값을 카운트
count_list = [ 0 for _ in range(201) ]
for num in num_list:

    count_list[num] += 1

print(count_list)
print(max(count_list))