n = int(input())
matrix = [ list(map(int, input().split())) for _ in range(n) ]

num_list = []
max_num = 0
for n_list in matrix:
    for i in range(n_list[0], n_list[1] + 1):
        num_list.append(i)
        if i > max_num:
            max_num = i 
    
count_list = [ 0 for i in range(max_num) ]
for num in num_list:
    count_list[num - 1] += 1

print(max(count_list))