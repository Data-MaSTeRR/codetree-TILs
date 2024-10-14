n = int(input())
matrix = [ list(input().split()) for _ in range(n) ]

current = 0

n_matrix = []
for nd_list in matrix:

    if nd_list[1] == "R":
       section_right = current + int(nd_list[0])
       section_left = current
       current += int(nd_list[0])

    
    elif nd_list[1] == "L":
        section_left = current - int(nd_list[0])
        section_right = current
        current -= int(nd_list[0])
    
    n_matrix.append([section_left, section_right])



count_list = [ 0 for _ in range(2001)]
for n_list in n_matrix:
    # 양 끝을 신경쓰지 않는이유??? -> 2번 이상 겹치는 양 끝은 구간에서 -1 고려하는 것과 같음
    for i in range(n_list[0] + 1000, n_list[1] + 1000):
        count_list[i - 1] += 1


twoover_sum = 0
for count in count_list:
    if count >= 2:
        twoover_sum += 1

print(twoover_sum)