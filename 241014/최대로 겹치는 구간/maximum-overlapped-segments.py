n = int(input())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

## 음수값도 고려해야함!! -> max_num을 두개의 합은 최대 201까지(0포함)

# 모든 리스트의 원소값 일렬로 정렬, 그리고 max값 찾기
max_num = 0
num_list = []
for n_list in matrix:
    for i in range(n_list[0], n_list[1] + 1):
        num_list.append(i)

    for n in n_list:
        if n > max_num:
            max_num = n 

# 원소마다 값을 카운트
count_list = [ 0 for _ in range(300) ]
for num in num_list:

    if num == -100 or num == 100:
        continue

    count_list[num + 100] += 1



print(max(count_list))